#!/usr/bin/env python3
"""Reproduce finite channel diagnostics, without a quantum-circuit simulation.

The generator exponential, event-grid Kraus maps, and analytic fixtures are
constructed separately. Floating-point checks are not interval certificates,
diamond-norm optimizations, asymptotic proofs, or compiled quantum circuits.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import eigh, expm


TOL = 3e-11


def opnorm(matrix):
    return float(np.linalg.norm(matrix, 2))


def spectral_function(matrix, function):
    values, vectors = eigh(matrix)
    return (vectors * function(np.maximum(values, 0))) @ vectors.conj().T


def kraus_channel(kraus):
    # Column-vectorization: vec(K rho K*) = (conj(K) tensor K) vec(rho).
    return sum(np.kron(k.conj(), k) for k in kraus)


def lindblad_generator(jumps):
    dim = jumps[0].shape[0]
    rate = sum(j.conj().T @ j for j in jumps)
    identity = np.eye(dim)
    return (sum(np.kron(j.conj(), j) for j in jumps)
            - (np.kron(identity, rate) + np.kron(rate.T, identity)) / 2)


def normalized_choi(channel, dim):
    # Build by applying the map to matrix units, independently of Kraus form.
    result = np.empty((dim * dim, dim * dim), dtype=complex)
    for left in range(dim):
        for right in range(dim):
            unit = np.zeros((dim, dim), dtype=complex)
            unit[left, right] = 1
            output = (channel @ unit.reshape(-1, order="F")).reshape(
                (dim, dim), order="F")
            result[left*dim:(left+1)*dim, right*dim:(right+1)*dim] = output / dim
    return (result + result.conj().T) / 2


def tp_residual(channel, dim):
    trace_row = np.eye(dim).reshape(-1, order="F")
    return float(np.linalg.norm(trace_row @ channel - trace_row))


def f_delta(rate, delta):
    def values(eigenvalues):
        result = np.full_like(eigenvalues, np.sqrt(delta))
        positive = eigenvalues > 1e-14
        result[positive] = np.sqrt(
            -np.expm1(-delta * eigenvalues[positive]) / eigenvalues[positive])
        return result
    return spectral_function(rate, values)


def grid_channel(jumps, delta):
    rate = sum(j.conj().T @ j for j in jumps)
    survival = expm(-delta * rate / 2)
    correction = f_delta(rate, delta)
    kraus = [survival] + [j @ correction for j in jumps]
    return kraus_channel(kraus), opnorm(
        sum(k.conj().T @ k for k in kraus) - np.eye(rate.shape[0]))


def julia_unitary(sigma):
    # Top-left projected block is J_sigma = sigma |0><1|, scale exactly 1.
    jump = np.array([[0., sigma], [0., 0.]])
    left_defect = np.diag([np.sqrt(1 - sigma*sigma), 1.])
    right_defect = np.diag([1., np.sqrt(1 - sigma*sigma)])
    return np.block([[jump, left_defect], [right_defect, -jump.T]])


def scalar_oracle_checks():
    records = []
    base = julia_unitary(0.)
    alpha = 1 - np.exp(-1.)
    for horizon in [1., 4., 16., 64., 256.]:
        sigma = 1 / np.sqrt(horizon)
        unitary = julia_unitary(sigma)
        distance = opnorm(unitary - base)
        formula = np.sqrt(2 - 2*np.sqrt(1 - sigma*sigma))
        controlled = np.block([[np.eye(4), np.zeros((4, 4))],
                               [np.zeros((4, 4)), unitary]])
        controlled_base = np.block([[np.eye(4), np.zeros((4, 4))],
                                    [np.zeros((4, 4)), base]])
        assert opnorm(unitary.T @ unitary - np.eye(4)) < TOL
        assert abs(distance - formula) < TOL
        assert distance <= np.sqrt(2/horizon) + TOL
        assert abs(opnorm(unitary.T - base.T) - distance) < TOL
        assert abs(opnorm(controlled - controlled_base) - distance) < TOL
        records.append({"time": horizon, "sigma": sigma,
                        "oracle_operator_distance": distance,
                        "ideal_output_half_trace_distance": float(alpha),
                        "hybrid_query_lower_at_unhalved_error_0_1":
                            float((alpha - .1) / distance)})
    return records


def unequal_rate_checks():
    dim = 4
    rates = np.array([.25, 1.])
    jump = np.zeros((dim, dim), dtype=complex)
    jump[0, 2], jump[1, 3] = np.sqrt(rates)
    generator = lindblad_generator([jump])
    coherence = np.zeros((dim, dim), dtype=complex)
    coherence[2, 3] = 1
    records = []
    for horizon in [1., 4., 16., 64.]:
        exact_output = (expm(horizon * generator) @ coherence.reshape(-1, order="F"))
        exact_output = exact_output.reshape((dim, dim), order="F")
        mean_rate = float(np.mean(rates))
        analytic = float(np.sqrt(np.prod(rates)) *
                         (-np.expm1(-horizon * mean_rate)) / mean_rate)
        collapsed = float(np.sqrt(np.prod(-np.expm1(-horizon * rates))))
        error = abs(exact_output[0, 1] - analytic)
        assert error < TOL
        assert collapsed > analytic + 1e-4
        records.append({"time": horizon, "exact_jump_coherence": analytic,
                        "generator_formula_residual": float(error),
                        "collapsed_one_kraus_coherence": collapsed,
                        "collapsed_coherence_excess": collapsed - analytic})
    return {"rates": rates.tolist(), "records": records}


def graded_cascade_fixture():
    # Two two-dimensional excitation ladders, with two homogeneous jumps.
    jump_one = np.zeros((6, 6), dtype=complex)
    jump_two = np.zeros((6, 6), dtype=complex)
    jump_one[0:2, 2:4] = np.array([[4, 1], [0, 2]]) / 6
    jump_one[2:4, 4:6] = np.array([[2, 1], [-1, 3]]) / 6
    jump_two[0:2, 2:4] = np.array([[1, -1], [2, 1]]) / 6
    jump_two[2:4, 4:6] = np.array([[1, 2], [1, -1]]) / 6
    return [jump_one, jump_two]


def polar_grid_channel(jumps, delta, cells, depth):
    """Exact finite left-grid/polar recursion, in an A eigenbasis.

    Classical diagonalization only accelerates this diagnostic. The proposed
    quantum algorithm implements the polar isometry without diagonalizing A.
    An exponential-kernel convolution reduces the diagnostic from O(M^2) to
    O(M) small-matrix products per event depth.
    """
    dim = jumps[0].shape[0]
    rate = sum(j.conj().T @ j for j in jumps)
    eigenvalues, eigenvectors = eigh(rate)
    eigenvalues = np.maximum(eigenvalues, 0)
    diagonal_jumps = [eigenvectors.conj().T @ j @ eigenvectors for j in jumps]
    jump_channel = kraus_channel(diagonal_jumps)
    beta = ((eigenvalues[:, None] + eigenvalues[None, :]) / 2).reshape(-1, order="F")
    decay = np.exp(-delta * beta)
    identity = np.eye(dim * dim, dtype=complex)
    previous = np.broadcast_to(identity, (cells + 1, dim*dim, dim*dim)).copy()
    positive = eigenvalues > 1e-14
    for _ in range(depth):
        current = np.empty_like(previous)
        current[0] = identity
        convolution = np.zeros_like(identity)
        for count in range(1, cells + 1):
            convolution = convolution * decay[None, :] + previous[count] @ jump_channel
            survival_eigenvalues = np.exp(-count * delta * eigenvalues)
            gram = np.ones(dim)
            gram[positive] = (survival_eigenvalues[positive] + delta * eigenvalues[positive]
                              * (-np.expm1(-count * delta * eigenvalues[positive]))
                              / (-np.expm1(-delta * eigenvalues[positive])))
            inverse_root = 1 / np.sqrt(gram)
            polar_super = (inverse_root[:, None] * inverse_root[None, :]).reshape(-1, order="F")
            current[count] = (np.diag(np.exp(-count * delta * beta))
                              + delta * convolution) * polar_super[None, :]
        previous = current
    change_basis = np.kron(eigenvectors.conj(), eigenvectors)
    return change_basis @ previous[cells] @ change_basis.conj().T


def polar_grid_channel_direct(jumps, delta, cells, depth):
    """Small independent enumeration: no eigenbasis convolution."""
    from functools import lru_cache
    dim = jumps[0].shape[0]
    rate = sum(j.conj().T @ j for j in jumps)

    @lru_cache(None)
    def recurse(count, remaining_depth):
        if count == 0 or remaining_depth == 0:
            return np.eye(dim * dim, dtype=complex)
        survival = expm(-count * delta * rate / 2)
        events = [(index, np.sqrt(delta) * jump @ expm(-index * delta * rate / 2))
                  for index in range(count) for jump in jumps]
        gram = survival.conj().T @ survival + sum(k.conj().T @ k for _, k in events)
        polar = spectral_function(gram, lambda values: 1 / np.sqrt(values))
        result = kraus_channel([survival @ polar])
        for index, event in events:
            result += recurse(count - index, remaining_depth - 1) @ kraus_channel([event @ polar])
        return result
    return recurse(cells, depth)


def polar_cascade_checks():
    jumps = graded_cascade_fixture()
    generator = lindblad_generator(jumps)
    direct = polar_grid_channel_direct(jumps, .25, 4, 2)
    fast = polar_grid_channel(jumps, .25, 4, 2)
    direct_residual = opnorm(direct - fast)
    assert direct_residual < TOL
    records = []
    for horizon in [1., 4., 16., 64.]:
        exact = expm(horizon * generator)
        errors = []
        for delta in [.25, .125, .0625]:
            approximation = polar_grid_channel(jumps, delta, round(horizon / delta), 2)
            choi = normalized_choi(approximation, 6)
            difference = normalized_choi(approximation - exact, 6)
            distance = float(np.sum(np.abs(np.linalg.eigvalsh(difference))))
            minimum_eigenvalue = float(np.linalg.eigvalsh(choi)[0])
            assert tp_residual(approximation, 6) < TOL
            assert minimum_eigenvalue > -TOL
            errors.append(distance)
            records.append({"time": horizon, "grid_step": delta, "event_depth": 2,
                            "channel_tp_residual": tp_residual(approximation, 6),
                            "minimum_normalized_choi_eigenvalue": minimum_eigenvalue,
                            "normalized_choi_unhalved_distance": distance,
                            "diamond_norm_upper_bound": 6 * distance})
        assert all(errors[i] > 1.4 * errors[i+1] for i in range(2))
    return {"direct_enumeration_convolution_residual": direct_residual,
            "records": records}


def cascade_checks():
    jumps = graded_cascade_fixture()
    rate_matrices = [j.conj().T @ j for j in jumps]
    rate = sum(rate_matrices)
    grade = np.diag([0, 0, 1, 1, 2, 2])
    generator = lindblad_generator(jumps)
    commutator = opnorm(rate_matrices[0] @ rate_matrices[1]
                        - rate_matrices[1] @ rate_matrices[0])
    assert opnorm(rate) < 1
    assert opnorm(rate @ grade - grade @ rate) < TOL
    assert commutator > 1e-3
    for jump in jumps:
        assert opnorm(grade @ jump - jump @ grade + jump) < TOL
    for first in jumps:
        for second in jumps:
            for third in jumps:
                assert opnorm(third @ second @ first) < TOL
    records = []
    for horizon in [1., 4., 16., 64.]:
        exact = expm(horizon * generator)
        exact_choi = normalized_choi(exact, 6)
        assert tp_residual(exact, 6) < TOL
        assert np.linalg.eigvalsh(exact_choi)[0] > -TOL
        errors = []
        for delta in [.125, .0625, .03125, .015625]:
            one_step, kraus_tp = grid_channel(jumps, delta)
            approximation = np.linalg.matrix_power(one_step, round(horizon / delta))
            approximate_choi = normalized_choi(approximation, 6)
            difference = normalized_choi(approximation - exact, 6)
            choi_distance = float(np.sum(np.abs(np.linalg.eigvalsh(difference))))
            min_eigenvalue = float(np.linalg.eigvalsh(approximate_choi)[0])
            assert kraus_tp < TOL
            assert tp_residual(approximation, 6) < TOL
            assert min_eigenvalue > -TOL
            errors.append(choi_distance)
            records.append({"time": horizon, "grid_step": delta,
                            "step_kraus_tp_residual": kraus_tp,
                            "channel_tp_residual": tp_residual(approximation, 6),
                            "minimum_normalized_choi_eigenvalue": min_eigenvalue,
                            "normalized_choi_unhalved_distance": choi_distance,
                            "diamond_norm_upper_bound": 6 * choi_distance})
        # A material convergence check, not a fitted universal exponent.
        assert all(1.5 < errors[i] / errors[i+1] < 3 for i in range(3))
        assert 1.7 < errors[-2] / errors[-1] < 2.3
    return {"dimension": 6, "grades": [0, 0, 1, 1, 2, 2],
            "number_of_jumps": 2, "rate_norm": opnorm(rate),
            "rate_grade_commutator": opnorm(rate @ grade - grade @ rate),
            "individual_rate_commutator": commutator,
            "generator_on_identity_norm": float(np.linalg.norm(
                generator @ np.eye(6).reshape(-1, order="F"))),
            "records": records}


def event_stack_checks():
    jumps = graded_cascade_fixture()
    rate = sum(j.conj().T @ j for j in jumps)
    records = []
    for horizon in [1., 4., 16.]:
        delta = .0625
        cells = round(horizon / delta)
        correction = f_delta(rate, delta)
        survival = expm(-horizon * rate / 2)
        exact_gram = survival.conj().T @ survival
        raw_gram = exact_gram.copy()
        envelope_norms = []
        # Bins [0,1), [1,2), [2,4), ...; last is comparator-truncated.
        bins = [(0., 1.)]
        start = 1.
        while start < horizon:
            bins.append((start, start))
            start *= 2
        for index in range(cells):
            time = index * delta
            even = expm(-time * rate / 2)
            for jump in jumps:
                corrected = jump @ even @ correction
                raw = np.sqrt(delta) * jump @ even
                exact_gram += corrected.conj().T @ corrected
                raw_gram += raw.conj().T @ raw
        for start, length in bins:
            stacked = np.vstack([np.sqrt(length) * j @ expm(-start * rate / 2)
                                  for j in jumps])
            envelope_norms.append(opnorm(stacked))
        normalization_squared = len(bins) + 1
        accepted_gram = exact_gram / normalization_squared
        polar = spectral_function(raw_gram, lambda values: 1 / np.sqrt(values))
        raw_eigenvalues = np.linalg.eigvalsh(raw_gram)
        polar_gram_residual = opnorm(polar @ raw_gram @ polar - np.eye(6))
        gram_residual = opnorm(exact_gram - np.eye(6))
        assert gram_residual < TOL
        assert opnorm(raw_gram - np.eye(6)) > 1e-4
        assert raw_eigenvalues[0] >= 1 - TOL
        assert raw_eigenvalues[-1] <= 1 + delta + TOL
        assert polar_gram_residual < TOL
        assert envelope_norms[0] <= 1 + TOL
        assert all(value <= np.exp(-.5) + TOL for value in envelope_norms[1:])
        records.append({"time": horizon, "grid_step": delta,
                        "number_of_time_bins": len(bins),
                        "stack_normalization_squared": normalization_squared,
                        "corrected_stack_gram_residual": gram_residual,
                        "uncorrected_riemann_gram_error": opnorm(raw_gram - np.eye(6)),
                        "actual_left_grid_gram_eigenvalue_min": float(raw_eigenvalues[0]),
                        "actual_left_grid_gram_eigenvalue_max": float(raw_eigenvalues[-1]),
                        "actual_polar_stack_gram_residual": polar_gram_residual,
                        "accepted_gram_target_residual": opnorm(
                            accepted_gram - np.eye(6) / normalization_squared),
                        "dyadic_envelope_operator_norms": envelope_norms})
    return records


def strict_lowering_counterexample():
    jump = np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]], dtype=complex) / 2
    rate = jump.conj().T @ jump
    grade = np.diag([0, 1, 2])
    top = np.array([0, 0, 1.], dtype=complex)
    separated = jump @ expm(-rate / 2)  # Equal unit no-jump waits.
    three_density = float(np.linalg.norm(np.linalg.matrix_power(separated, 3) @ top)**2)
    five_density = float(np.linalg.norm(np.linalg.matrix_power(separated, 5) @ top)**2)
    assert opnorm(np.linalg.matrix_power(jump, 3)) < TOL
    assert opnorm(rate @ grade - grade @ rate) > .1
    assert three_density > 1e-6
    assert five_density > 1e-10
    return {"jump_matrix": jump.real.tolist(), "rate_norm": opnorm(rate),
            "jump_cube_norm": opnorm(np.linalg.matrix_power(jump, 3)),
            "rate_grade_commutator": opnorm(rate @ grade - grade @ rate),
            "three_jump_density_at_unit_waits": three_density,
            "five_jump_density_at_unit_waits": five_density}


def compute():
    return {"schema_version": 1,
            "environment": {"python": platform.python_version(),
                            "numpy": np.__version__, "scipy": scipy.__version__},
            "scalar_oracle": scalar_oracle_checks(),
            "unequal_rate_coherence": unequal_rate_checks(),
            "noncommuting_graded_cascade": cascade_checks(),
            "actual_polar_grid_cascade": polar_cascade_checks(),
            "dyadic_first_event_stack": event_stack_checks(),
            "strict_lowering_counterexample": strict_lowering_counterexample()}


def compare(current, expected, path="results"):
    if path == "results.environment":
        return  # Versions are reported; numeric/invariant checks govern portability.
    if isinstance(expected, dict):
        if set(current) != set(expected):
            raise AssertionError(f"{path}: keys differ")
        for key in expected:
            compare(current[key], expected[key], path + "." + key)
    elif isinstance(expected, list):
        if len(current) != len(expected):
            raise AssertionError(f"{path}: list lengths differ")
        for index, value in enumerate(expected):
            compare(current[index], value, f"{path}[{index}]")
    elif isinstance(expected, (int, float)) and not isinstance(expected, bool):
        if not np.isclose(current, expected, rtol=2e-7, atol=5e-11):
            raise AssertionError(f"{path}: {current!r} differs from {expected!r}")
    elif current != expected:
        raise AssertionError(f"{path}: values differ")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare with saved finite results.")
    parser.add_argument("--output", type=Path, help="Write current results to this JSON path.")
    args = parser.parse_args()
    result = compute()
    if args.check:
        expected = json.loads(Path(__file__).with_name("expected_results.json").read_text())
        compare(result, expected)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    if not args.check and not args.output:
        print(json.dumps(result, indent=2, allow_nan=False))
    else:
        print("PASS: scalar oracle distance; unequal-rate coherence; grade-2 polar-grid "
              "and microchannel convergence; event-stack normalization; strict-lowering counterexample.")
        if args.check:
            print("PASS: saved finite results agree within numerical tolerances.")


if __name__ == "__main__":
    main()

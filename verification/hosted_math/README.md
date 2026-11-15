# Check actual hosted mathematics

The repository workflow runs the finite scientific checks, then compares the
actual commit-pinned GitHub rendering with the mathematical source at wide
and narrow viewport widths. It runs only for same-repository pull requests
with read-only repository permissions and no persisted checkout credentials.

The three scripts in this directory are a matching collector/checker bundle.
The probe checks one representative page, including inline, display and
table-cell mathematics. The full collector inventories every tracked
Markdown page and compares all recognized expressions with their actual
accessible MathML. HTML and screenshots are retained with the reports for
source and visual inspection.

A compatible local runtime can run the same read-only check:

```bash
npm install --prefix /tmp/decay-math-runtime playwright@1.56.1 mathjax-full@3.2.1
node /tmp/decay-math-runtime/node_modules/playwright/cli.js install chromium
NODE_PATH=/tmp/decay-math-runtime/node_modules node verification/hosted_math/capture_hosted_math.cjs \
  --root "$PWD" --repository GoGoKo699/Quantum-Decay-Fast-Forwarding \
  --revision FULL_COMMIT_SHA --output /tmp/new-empty-decay-captures
```

Use an observed full commit SHA and a new empty output directory. The source
must be present as exact local Git objects. The command opens a fresh unsigned
browser context on the public GitHub pages; it neither changes access settings
nor authenticates to a private repository.

Automated expression comparison does not establish scientific truth or replace
looking at the screenshots, including narrow-width layout and nonmathematical
navigation. Workflow artifacts expire; they are reproducible diagnostic
outputs rather than permanent scientific sources. The analytical proof and
finite scientific checks remain separately documented in the parent
[verification guide](../README.md).

The explicit text contract checks the headline query bound, diamond-error norm,
and the catalyst and diagonal-rate expressions that were reviewed during hosted
rendering. Structural comparison still applies to every expression.

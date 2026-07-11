# Code Signing Policy

LocalDrop signs and distributes its Windows release artifacts.

## Windows — SignPath Foundation (pending approval)

We have applied to the SignPath Foundation program for free code signing.

**Attribution (required by the program once approved):**
> "Free code signing provided by SignPath.io, certificate by SignPath Foundation"

**Status:** Pending approval.

### What will be signed
- Windows MSI installer (`*.msi`), built via the Tauri v2 WiX bundler.
- Windows NSIS installer (`*-setup.exe`), if enabled.

### Build and signing process
- Artifacts are built from this repository using GitHub Actions
  (`.github/workflows/release.yml`).
- Only CI-built artifacts triggered by version tags (`vX.Y.Z`) are submitted
  to SignPath for signing.
- The private signing key is held by SignPath (HSM-backed). This project does
  not store or have access to the private key.

### Team roles (single-maintainer project)
- **Author / Approver** (commit access, approves signing requests):
  - https://github.com/Chauhan-saab2006

### Distribution
- https://github.com/Chauhan-saab2006/LocalDropt-APP/releases
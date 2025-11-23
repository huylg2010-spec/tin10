<!-- Auto-generated guidance for AI coding agents working in this repo. -->
# Repository-specific Copilot instructions

Purpose: give an AI coding agent immediate, actionable context for making small, safe changes in this exam-style Python repo.

- **Project shape:** single-script exam harness: `exam.py` is the canonical entrypoint. Top-level example files include `input.inp` and `output.out`.
- **Core conventions:**
  - The script uses three helper readers: `read_all()`, `read_tokens()`, `read_lines()` and a single writer `write_output(result)` in `exam.py`.
  - Input / output filenames are configured by the module-level constants `INPUT_FILE` and `OUTPUT_FILE` (defaults: `"INPUT.INP"`, `"OUTPUT.OUT"`). Agents should prefer updating those constants rather than changing I/O logic.
  - Files are opened with `encoding="utf-8"` — preserve this unless explicitly required.
  - `write_output` accepts either a scalar or a `list` (joins list items with `\n`). Keep that contract when changing output formatting.

- **Big picture / why:** this repo is an exam/hard-competition scaffold. The intended workflow is small, self-contained scripts that read from a single input file (or STDIN) and write a single output file. Changes should be minimal and focused on the problem logic inside `solve()`.

- **Where to modify:** put problem-solving logic inside `solve()` in `exam.py`. Do not restructure project layout; keep helper functions and I/O at top-level so they remain reusable across problems.

- **Run / debug (PowerShell on Windows):** follow `README.MD` but the minimal commands used by developers here are:

  - Activate venv (PowerShell):
    - `Set-Location D:\Tin10\Stud`
    - `& .\.venv\Scripts\Activate.ps1`

  - Run normally:
    - `python exam.py`
  - Run with redirected input file (shell redirect):
    - `python exam.py < input.inp`

  - VS Code debug: repository README includes a recommended `.vscode/launch.json`. The launcher uses `integratedTerminal`; if you need to debug with input redirection, either run the program in the terminal or modify `exam.py` to accept a filename via `sys.argv`.

- **Agent-specific rules (do this):**
  - Keep edits minimal and localized to `exam.py` unless adding tests or docs.
  - When changing I/O behavior, update `INPUT_FILE` / `OUTPUT_FILE` constants and document the change in `README.MD`.
  - Preserve UTF-8 encoding and the `write_output` list-vs-scalar contract.
  - If adding new files, add brief notes to `README.MD` describing how to run them.

- **What to avoid:**
  - Do not introduce external dependencies without updating `requirements.txt` and noting install steps in `README.MD`.
  - Avoid globally changing project layout (no new packages/subpackages needed here).
  - Avoid printing debug logs to stdout; use comments or conditional logging that does not affect `write_output` results.

- **Examples from this repo:**
  - `exam.py` constants: `INPUT_FILE = "INPUT.INP"`, `OUTPUT_FILE = "OUTPUT.OUT"` — change these to match sample files like `input.inp` when preparing a runnable example.
  - Reader patterns: use `tokens = read_tokens()` for whitespace-separated numeric input; use `lines = read_lines()` for line-oriented input.

If anything is unclear or you want the instructions to be stricter (for example, enforce a `sys.argv` file parameter pattern or add a test harness), tell me and I will update this guide.

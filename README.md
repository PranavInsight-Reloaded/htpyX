# htpyX Prototype

This is a small prototype of **htpyX** — a Python-first micro-transpiler to build single-file HTML+CSS+JS apps.

## Quickstart
1. unzip the package.
2. `cd htpyX`
3. `python3 main.py`
4. Open `http://127.0.0.1:8000` in your browser.

The server will serve a demo page (ultra_test) which demonstrates:
- theme toggle
- a server-backed counter (button click updates server state)
- glassmorphic card styling

## Files
- `core/` : core engine & element definitions
- `examples/` : demo site builders
- `main.py` : tiny dev server to serve pages and dispatch events

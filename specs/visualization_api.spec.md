# Visualization API Integration

This spec describes the expected interface between the Python backend and the
React diagrams contained under `frontend/`.

## Goals
- Provide JSON endpoints for trend overviews and indicator data
- Enable React components like `TrendDiagram` and `IntentStackUI` to fetch
  realtime values
- Serve as the foundation for more advanced visualization modules

## Endpoints

- `GET /trends` → returns a list of `{label, trend}` objects representing
  timeframe trends. Initially mocked, later sourced from analysis modules.
- `GET /mfi` → returns MFI signal data with timestamps and component flags.

The server should be powered by **FastAPI** and launched with `uvicorn`. Other
packages may consume the same endpoints for integration tests.

## Affected Areas
- New module `fts/api/server.py`
- README instructions for running the server
- Frontend fetch logic (to be implemented) that consumes these endpoints


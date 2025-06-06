# Database Schema Integration

## Purpose
Describe table structures for fractal patterns, shape attributes, indicators, and trade signals. Provide guidelines on how new data models connect to existing Python code.

## Expected Deliverables
- SQL migration scripts or SQLAlchemy models for pattern tables
- Data access utilities for querying patterns and signals

## Integration Steps
1. Place migration scripts under `db/migrations/`.
2. Update Python package under `fts/` to include new data access layer.
3. Document schemas in `docs/` and link from README.

## Affected Areas
- `fts/` package
- `db/` migrations
- Documentation under `docs/`

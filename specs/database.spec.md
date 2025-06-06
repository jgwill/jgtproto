# Database Schema Integration

## Purpose
Describe table structures for fractal patterns, shape attributes, indicators, and trade signals. Provide guidelines on how new data models connect to existing Python code. Research favors **QuestDB** as the primary time-series database for pattern storage due to its sub-millisecond latency. Vector similarity search will be handled separately (see `vector_db.spec.md`).

## Expected Deliverables
- SQL migration scripts or SQLAlchemy models for QuestDB-backed pattern tables
- Data access utilities for querying patterns and signals
- Configuration examples for connecting to QuestDB instances

## Integration Steps
1. Place migration scripts under `db/migrations/`.
2. Update Python package under `fts/` to include new data access layer.
3. Configure QuestDB connection settings in a shared config file.
4. Document schemas in `docs/` and link from README.

## Affected Areas
- `fts/` package
- `db/` migrations
- Documentation under `docs/`
- Configuration under `config/` (QuestDB settings)

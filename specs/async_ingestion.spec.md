# Asynchronous Ingestion Layer

## Purpose
Design a scalable ingestion engine capable of consuming multiple exchange feeds concurrently with minimal latency. The layer will serve as the entry point for real-time market data in the Echo phase.

## Expected Deliverables
- AsyncIO-based feed handlers with uvloop for performance
- Optional Ray actors to scale ingestion across CPU cores
- Connection pooling and backpressure mechanisms
- Configuration examples for stream sources and buffer sizes

## Integration Steps
1. Implement core ingestion service under `fts/ingestion/`.
2. Expose a CLI entry for launching feed collectors.
3. Store incoming data in the chosen database (QuestDB) via batched inserts.
4. Document environment requirements and monitoring hooks.

## Affected Areas
- `fts/ingestion/`
- `scripts/` for helper commands
- Documentation and specs

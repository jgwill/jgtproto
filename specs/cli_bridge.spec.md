# CLI Bridge Specification

## Purpose
Describe how command-line tools will connect jgtpy and jgtml workflows.

## Expected Deliverables
- `fts/cli/jgtpy_jgtml_bridge.py` providing `scan-and-validate` command
- Click-based commands with async execution
- Output formats: pretty, json, csv

## Integration Steps
1. Add CLI module under `fts/cli/`
2. Document usage in README
3. Provide setup script for environment validation

## Affected Areas
- `fts/cli/`
- `scripts/`
- Documentation

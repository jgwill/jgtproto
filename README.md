# jgtproto

This repository collects prototypes and experiments around the **JGT** agentic systems.

## Frontend

A minimal React setup lives under `frontend/`. It uses [Vite](https://vitejs.dev/) and TypeScript. Example UI components such as `IntentStackUI` and `TrendDiagram` showcase how strategy diagrams can be represented in the browser.

Install dependencies and start the dev server:

```bash
cd frontend
npm install
npm run dev
```

If you encounter an `ENOSPC` error about file watchers, increase the system
limit or run Vite with polling:

```bash
sudo sysctl fs.inotify.max_user_watches=524288
VITE_FS_WATCH_POLLING=true npm run dev
```

## Python Scripts

Example data analysis scripts are placed in `scripts/`. `mfi_plot.py` demonstrates how to plot Money Flow Index signal components using `matplotlib`.

Run with your Python environment:

```bash
python scripts/mfi_plot.py
```

## FTS Package Scaffold

Python modules under `fts/` outline the seven-step trading process and provide placeholders for data collection, feature engineering, model training, signal generation, automated execution, and feedback loops. New subpackages have been prepared for reinforcement learning (`fts/rl`), strategy definitions (`fts/strategies`), and backtesting utilities (`fts/backtest`). Database migrations live under `db/migrations`, while documentation sources sit in `docs/` and tests in `tests/`. Additional packages handle vector similarity search (`fts/vector_db`) and Redis-based caching (`fts/cache`). These modules will evolve as new components arrive from the companion repository.

An asynchronous ingestion layer under `fts/ingestion` collects multiple exchange feeds using `asyncio` and can scale with Ray for higher throughput. A small runner is provided for quick experimentation:

```bash
python -m fts.ingestion.service
```

This launches the service with dummy sources. Real feed handlers can be added by registering factories in `IngestionService`.

## Intent Flow Components

Trader intents can be transformed into executable strategies through a chain of modules under `fts/intent_flow/`. These include:

- `LLMTranslationEngine` – converts natural language into `.jgtml-spec` text
- `IntentSpecParser` – builds signal packages from the spec
- `JGTMLExecutionCore` – runs the strategy logic
- `EntryScriptGen` – produces runnable scripts
- `EchoLattice` – records outcomes for later analysis

Sample React components (`IntentStackUI`, `TrendDiagram`) visualize this flow under the `frontend/` app.

## Specifications

Design documents live in `specs/`. Each `*.spec.md` describes expectations for upcoming implementations—database schemas, reinforcement learning agents, intent flow modules, and more. Contributors should consult these files when adding new features.

## CLI Integration

Use the enhanced CLI to scan and validate signals via `jgtpy` and `jgtml`:

```bash
# Check environment, install Python and frontend packages
bash scripts/setup_enhanced_fts.sh

# Run a quick analysis
python -m fts.cli.jgtpy_jgtml_bridge scan-and-validate --symbol EURUSD --timeframes H1 H4
```

The CLI outputs analysis results in pretty or JSON formats. See `--help` for options.

## Example Workflow

The `examples/complete_workflow_example.py` script demonstrates how to run the resilient pipeline programmatically:

```bash
python examples/complete_workflow_example.py
```

## Version Compatibility

The integration expects specific package versions. A table of tested versions is maintained in the documentation.


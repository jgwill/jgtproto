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

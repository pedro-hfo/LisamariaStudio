# Getting started

## Install once

Requirements: Node 22.12+ (24 recommended for this repository), npm, uv and Python 3 to run the installer. On macOS: `brew install node@24 uv`. uv downloads the project's Python 3.13 and creates `.venv/`.

From the repository root:

```bash
npm run setup
npm run dev -- --port 3000
```

| Address | Service |
|---|---|
| `http://127.0.0.1:3000` | React application |
| `http://127.0.0.1:3001` | PT/EN Sphinx documentation |
| `http://127.0.0.1:3000/api/docs` | FastAPI interactive HTTP contract |

`--port x` places documentation on `x+1`. The backend uses a free internal port, exposed to the browser through `/api`. The two user-facing addresses remain `x` and `x+1`. The command prints the addresses after verifying that all four entry points respond.

**Ctrl+C stops every process**, including reload workers. If a port is occupied, startup fails with a message; it never silently changes ports. Logs are stored in `.cache/dev/<process>/`.

## Try it

Book a future appointment. Repeat the same time to see a conflict rejected. An example session lasts 60 minutes with 15 minutes for preparation. These values await a business decision. The input uses the device timezone, displayed next to the field; the API requires a timezone-aware instant.

The example stores data in memory. Restarting or editing the backend clears the schedule. Do not enter customer data: the example does not request any.

## Verify

```bash
npm run check
.venv/bin/pytest acceptance/backend -v
npm test
npm run docs:build
npm run dev -- --port 4100 --check
```

The last command starts, verifies and stops the services. `npm run check` verifies Python style, types, architecture rules, BDD, React components, the build and strict documentation. Use `uv.lock` and `package-lock.json` to reproduce dependencies.

## Reloading

Vite updates the frontend; Uvicorn restarts the backend; Sphinx rebuilds documentation when guides, code or scenarios change. Changes to `docs/conf.py` or the launcher scripts require restarting the command.

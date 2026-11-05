# GitHub Pages deployment

## What is published

[Open the website](https://pedro-hfo.github.io/LisamariaStudio/).
The public repository is [pedro-hfo/LisamariaStudio](https://github.com/pedro-hfo/LisamariaStudio).

Pages serves the static React presentation and the Sphinx guides in `docs/pt/` and `docs/en/`. Python does not run on Pages. The hosted presentation links to the local setup guide instead of mounting the booking form or requesting `/api`. Run the [local application](getting-started.md) to experiment with appointments.

## Follow a release

1. Implement a step on a named branch and make descriptive commits.
2. Before merging, update the README and affected PT/EN guides.
3. Merge into `main` with `--no-ff`, then push.
4. Open the repository's **Actions → Validate and deploy GitHub Pages** run. A successful `build` job is followed by `deploy`, which exposes the site URL.

Pull requests run the same checks and build without deploying. A manual run is available through **Run workflow**. The repository's **Settings → Pages → Source** must be **GitHub Actions**. For a private repository, GitHub requires a plan that supports Pages; this repository is public with the owner's authorization.

## Understand the build

`.github/workflows/pages.yml` installs Node 24 and uv, restores dependencies from both lockfiles, and runs `npm run check`. It then runs:

```bash
npm run build:pages
```

`scripts/build_pages.py` builds Vite in `pages` mode and generates fresh Sphinx output. It combines the frontend and documentation in `build/pages`, excluding Sphinx's build cache. The workflow uploads only that folder, then deploys it using short-lived GitHub credentials; no personal token is stored in the repository.

`PAGES_BASE_PATH` defaults to `/LisamariaStudio/`; CI derives it from the repository name. Vite's `BASE_URL` keeps assets and links inside that path. The normal `npm run dev` and `npm run build` keep the local booking interface. If adding a custom domain, update this base path to `/` in the workflow as well as configuring the domain in Pages.

## Verification

`frontend/tests/pages.test.tsx` checks that the published mode offers PT/EN guides under the repository path and makes no backend request. Existing acceptance tests still cover local booking. Strict Sphinx checks validate references and the documentation parity test requires matching PT/EN guide paths.

Hint: **build** produces files; **deploy** publishes those files. A passing build alone does not confirm publication. GitHub documents the [custom workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

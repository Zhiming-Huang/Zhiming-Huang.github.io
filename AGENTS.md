# Repository Guidelines

## Project Structure & Module Organization

This is a Pelican static site. Source content lives in `content/`, with main pages in `content/index.md`, `content/news.md`, `content/teaching.md`, `content/service.md`, and `content/pages/`. Publication data is edited in `content/pages/publications.md`. The publications plugin syncs it into `themes/modern-academic/static/data/publications.json` during builds. Static files belong in `content/files/`, images in `content/images/`, custom plugins in `plugins/`, and theme templates, CSS, and JavaScript in `themes/modern-academic/`. The generated site goes to `output/` and should not be committed.

## Build, Test, and Development Commands

Set up a local environment before building:

```bash
python -m venv pelican-env
source pelican-env/bin/activate
pip install -r requirements.txt pyyaml beautifulsoup4
```

Use `make devserver PORT=8000` for local autoreload development. Use `make html` for a development build and `make publish` for a production build. The known production build command for this checkout is:

```bash
pelican-env/bin/pelican content -s publishconf.py
```

Run `python sync_publications.py` only when debugging publication YAML to JSON sync.

## Coding Style & Naming Conventions

Use 4-space indentation for Python and keep plugin functions in `snake_case`. Keep Markdown metadata names consistent with Pelican conventions, for example `Title:`, `Slug:`, `Publish: false`, and `Menu: true`. Prefer lowercase, descriptive asset filenames, with hyphens or underscores. Keep Jinja templates focused on layout and avoid moving content strings out of Markdown unless they are theme-level labels. Use semicolons sparingly. In theory-related prose, name the concrete proof object directly, such as a regret bound, oracle condition, or window inequality.

## Testing Guidelines

There is no dedicated unit test suite. Treat a clean production build as the required validation step. For content-only edits, run `make publish` or the explicit `pelican-env/bin/pelican content -s publishconf.py` command. For template, CSS, JavaScript, plugin, or publication changes, also inspect the local site through `make devserver PORT=8000`. Confirm that publication edits update `themes/modern-academic/static/data/publications.json`.

## Commit & Pull Request Guidelines

Recent history uses short, direct commit messages such as `Control page visibility from markdown` and `Update publications.md`. Prefer specific imperative messages over vague `update` commits. Stage only intended files. Do not commit `output/`, `.DS_Store`, `__pycache__/`, or local virtual environments. Pull requests should describe the changed pages or theme areas, list the build command run, link relevant issues when available, and include screenshots for visible layout changes.

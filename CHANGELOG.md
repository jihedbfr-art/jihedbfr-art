# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-08-14
### Added
- Phase 1: Bilingual English/French READMEs.
- Phase 1: `jihedailabs` brand assets (dark, light, mark SVG logos).
- Phase 1: `og-preview.png` generator.
- Phase 1: Linting architecture for documentation i18n (`scripts/lint_i18n.py`).
- Phase 2: Python scripts to auto-generate the profile `README.md` and `README.fr.md` using `Jinja2`.
- Phase 2: Data fed from `docs/NOW.yml`, GitHub API (flagship repos), and Dev.to RSS.
- Phase 2: GitHub Action `refresh-profile.yml` running daily cron and validating with MarkdownLint before committing.
- Phase 2: Local SVG generator for GitHub profile statistics.

### Changed
- Removed Arabic (RTL) support from all documents.
- Refactored `README` files into `templates/README.en.j2` and `templates/README.fr.j2`.

### Removed
- Removed legacy language switcher format and missing Arabic checks.

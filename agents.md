# Agent Guidelines for JihedAiLabs Ecosystem

This repository (`jihedbfr-art`) serves as the central machine-readable discovery index for the JihedAiLabs ecosystem.

## Exposed Resources
The following index files are automatically generated and exposed. Their `raw.githubusercontent.com` URLs are stable and guaranteed not to break.

1. **`skills-index.json`**: The primary, structured JSON catalog of all repositories.
   - URL: `https://raw.githubusercontent.com/jihedbfr-art/jihedbfr-art/main/skills-index.json`
2. **`llms.txt`**: A concise, markdown-formatted list of repositories.
   - URL: `https://raw.githubusercontent.com/jihedbfr-art/jihedbfr-art/main/llms.txt`
3. **`llms-full.txt`**: A detailed markdown catalog including full descriptions.
   - URL: `https://raw.githubusercontent.com/jihedbfr-art/jihedbfr-art/main/llms-full.txt`

## Consumption Preference
Agents should query the ecosystem index in the following order of preference:
1. `skills-index.json` (Structured, parsable data)
2. `llms.txt` (Compact context injection)
3. `llms-full.txt` (Deep context injection when token limits allow)

## Versioning Contract (skills-index.json)
The `skills-index.json` adheres to Semantic Versioning (SemVer):
- **MAJOR**: Schema changes (e.g., structural redesign, removal of keys).
- **MINOR**: Addition of new fields in the JSON structure.
- **PATCH**: Data updates (e.g., new repositories added, descriptions updated, metadata refreshed).

## Ecosystem `.meta.yml` Coverage
The central index aggregates `.meta.yml` files present in the `main` branch of ecosystem repositories.
- If a repository contains a `.meta.yml`, its data is extracted directly (`metadata: "explicit"`).
- If a repository lacks a `.meta.yml`, metadata is inferred via the GitHub API (`metadata: "inferred"`).
- Currently, fallback inference ensures 100% coverage across public repositories, even if `.meta.yml` adoption is partial.

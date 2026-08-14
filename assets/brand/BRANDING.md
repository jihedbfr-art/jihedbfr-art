# JihedAiLabs Branding Guidelines

This document outlines the official brand guidelines for the **JihedAiLabs** ecosystem.

## Logo Assets

The brand uses a dynamic SVGs logo system located in `assets/brand/`:
- `jihedailabs-logo-dark.svg`: Primary logo for dark themes (e.g. GitHub dark mode).
- `jihedailabs-logo-light.svg`: Variant optimized for light themes.
- `jihedailabs-mark.svg`: Square monogram (AI) used as an avatar or favicon.

## Colors
- **Primary Gold**: `#d4af37`
- **Secondary Blue**: `#4fc0ff`
- **Dark Background**: `#0a1420`

## Safe Space (Zone de respiration)
The logo must always have a minimum safe space equal to 20% of its width to ensure visual clarity. Do not crowd the logo with text or other graphics.

## Usage Rules

### Authorized Uses
- The logo is strictly authorized in the root `README.md` and `README.fr.md` of the project.
- It must be integrated using the `<picture>` element to respect the user's `prefers-color-scheme`.

### Forbidden Uses
- **DO NOT** use the logo in any agent `SKILL.md` file. `SKILL.md` files must remain purely text-based and technical to minimize token consumption for LLMs.
- **DO NOT** distort, stretch, or alter the colors of the provided SVG files.
- **DO NOT** use the PNG fallback unless SVG rendering is completely unsupported.

# Style Guide & Editorial Standards

This repository follows strict engineering documentation and branding standards. All content must adhere to the rules defined below.

## 1. Writing Rules (Non-Negotiable)

Content must read as if written by a senior engineer, not a language model.

### Banned Practices
- Do not use hollow marketing words (e.g., `delve`, `leverage`, `seamless`, `robust`, `cutting-edge`, `unlock`, `harness`, `elevate`, `game-changer`, `in today's fast-paced world`).
- Avoid systematic lists of exactly three elements unless technically justified.
- Do not use decorative emojis in bursts (e.g., 🚀✨🔥). Use a maximum of one emoji per list item, and only if it conveys information (like a category).
- Eliminate empty phrases that bring no verifiable facts.
- Avoid unproven superlatives (`world-class`, `the best`).

### Required Practices
- Use short sentences, concrete facts, and verifiable figures.
- Use natural variation in sentence length.
- Prefer the active voice.
- English is the canonical language. French and Arabic versions must be faithful translations, not loose paraphrases.

## 2. Directory Standard

Every new directory created in this repository must contain the following structure:

```text
<directory>/
├── README.md         # English — canonical version
├── README.fr.md      # French
└── .meta.yml         # Machine metadata (for Vague 3)
```

Each README must start with:
1. The JihedAiLabs logo block (`<picture>` light/dark).
2. The language toggle line.
3. The H1 title.
4. A one-line summary sentence describing what the directory provides.

### Logo Rule
**The logo is allowed in human-facing READMEs and documentation; it is strictly FORBIDDEN in `SKILL.md` files.** These files are read by agents, not humans, and image tags pollute their parsing.

## 3. Glossary (EN / FR)

To ensure consistency across translations, use the following technical glossary:

| English | French |
| --- | --- |
| Microservices | Microservices |
| Distributed Systems | Systèmes distribués |
| Saga Pattern | Pattern Saga |
| Transactional Outbox | Transactional Outbox |
| Orchestration | Orchestration |
| Telecommunications | Télécommunications |
| Provisioning | Provisioning |
| Framework | Framework |
| Repository | Dépôt |
| Pull Request | Pull Request |

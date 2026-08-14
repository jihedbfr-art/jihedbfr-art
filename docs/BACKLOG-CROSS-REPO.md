# BACKLOG CROSS REPO

> Ce fichier contient les templates `.meta.yml` validés et prêts à copier-coller pour chaque dépôt de l'écosystème JihedAiLabs.
> Il propose **8 à 12 topics SEO à fort trafic** par dépôt (ce que les recruteurs et ingénieurs recherchent activement sur GitHub), avec validation d'existence réelle sur `github.com/topics/<nom>`.

---

## 1. engineering-library

- **Description GitHub** : Java/Spring engineering notes from 10+ years in telecom BSS production: architecture decisions, failure write-ups, debugging recipes, and a telecom domain guide you won't find in another repo.
- **Type suggéré** : `monorepo`

### Topics Actuels — engineering-library
- ✅ `ai-engineering`
- ✅ `angular`
- ✅ `architecture`
- ✅ `engineering-library`
- ✅ `java`
- ✅ `keycloak`
- ✅ `microservices`
- ✅ `spring-boot`
- ✅ `software-engineering`
- ✅ `telecom`

### Proposition SEO — engineering-library (12 Topics Cibles Validés)
- ✅ `java`
- ✅ `spring-boot`
- ✅ `microservices`
- ✅ `architecture`
- ✅ `clean-architecture`
- ✅ `design-patterns`
- ✅ `distributed-systems`
- ✅ `keycloak`
- ✅ `telecom`
- ✅ `angular`
- ✅ `software-engineering`
- ✅ `best-practices`

### Template .meta.yml — engineering-library

```yaml
name: engineering-library
description: "Java/Spring engineering notes from 10+ years in telecom BSS production: architecture decisions, failure write-ups, debugging recipes, and a telecom domain guide you won't find in another repo."
type: monorepo
topics:
  - java
  - spring-boot
  - microservices
  - architecture
  - clean-architecture
  - design-patterns
  - distributed-systems
  - keycloak
  - telecom
  - angular
  - software-engineering
  - best-practices
entry_points:
  human: README.md
  agent: llms.txt
```

---

## 2. bpmn-provisioning-patterns

- **Description GitHub** : Real-world orchestration patterns with Camunda + Spring Boot + Kafka, modeled on telecom number portability: transactional outbox, idempotent consumer, sagas, compensation, and SLA timeouts.
- **Type suggéré** : `library`

### Topics Actuels — bpmn-provisioning-patterns
- ✅ `bpmn`
- ✅ `camunda`
- ✅ `kafka`
- ✅ `spring-boot`
- ✅ `telecom`
- ✅ `saga-pattern`

### Proposition SEO — bpmn-provisioning-patterns (12 Topics Cibles Validés)
- ✅ `bpmn`
- ✅ `camunda`
- ✅ `spring-boot`
- ✅ `kafka`
- ✅ `saga-pattern`
- ✅ `distributed-transactions`
- ✅ `transactional-outbox`
- ✅ `telecom`
- ✅ `orchestration`
- ✅ `microservices`
- ✅ `resilience`
- ✅ `event-driven`

### Template .meta.yml — bpmn-provisioning-patterns

```yaml
name: bpmn-provisioning-patterns
description: "Real-world orchestration patterns with Camunda + Spring Boot + Kafka, modeled on telecom number portability: transactional outbox, idempotent consumer, sagas, compensation, and SLA timeouts."
type: library
topics:
  - bpmn
  - camunda
  - spring-boot
  - kafka
  - saga-pattern
  - distributed-transactions
  - transactional-outbox
  - telecom
  - orchestration
  - microservices
  - resilience
  - event-driven
entry_points:
  human: README.md
  agent: llms.txt
```

---

## 3. keycloak-spi-workbench

- **Description GitHub** : Custom Keycloak SPIs done properly: real providers, each with tests, no toy examples.
- **Type suggéré** : `library`

### Topics Actuels — keycloak-spi-workbench
- ✅ `authentication`
- ✅ `keycloak`
- ✅ `keycloak-spi`
- ✅ `mfa`
- ✅ `spring-boot`
- ✅ `testcontainers`
- ✅ `apache-kafka`
- ✅ `postgresql`
- ✅ `user-federation`

### Proposition SEO — keycloak-spi-workbench (12 Topics Cibles Validés)
- ✅ `keycloak`
- ✅ `keycloak-spi`
- ✅ `oauth2`
- ✅ `openid-connect`
- ✅ `authentication`
- ✅ `mfa`
- ✅ `user-federation`
- ✅ `iam`
- ✅ `spring-boot`
- ✅ `testcontainers`
- ✅ `security`
- ✅ `identity-management`

### Template .meta.yml — keycloak-spi-workbench

```yaml
name: keycloak-spi-workbench
description: "Custom Keycloak SPIs done properly: real providers, each with tests, no toy examples."
type: library
topics:
  - keycloak
  - keycloak-spi
  - oauth2
  - openid-connect
  - authentication
  - mfa
  - user-federation
  - iam
  - spring-boot
  - testcontainers
  - security
  - identity-management
entry_points:
  human: README.md
  agent: llms.txt
```

---

## 4. spring-keycloak-toolkit

- **Description GitHub** : Spring Boot auto-configuration for Keycloak-secured resource servers: realm/resource role mapping + RFC 7807 error responses
- **Type suggéré** : `library`

### Topics Actuels — spring-keycloak-toolkit
- ✅ `jwt`
- ✅ `keycloak`
- ✅ `oauth2`
- ✅ `rfc7807`
- ✅ `spring-boot`
- ✅ `spring-security`

### Proposition SEO — spring-keycloak-toolkit (12 Topics Cibles Validés)
- ✅ `spring-boot`
- ✅ `spring-security`
- ✅ `keycloak`
- ✅ `oauth2`
- ✅ `openid-connect`
- ✅ `jwt`
- ✅ `spring-boot-starter`
- ✅ `role-mapping`
- ✅ `rfc7807`
- ✅ `resource-server`
- ✅ `microservices`
- ✅ `java`

### Template .meta.yml — spring-keycloak-toolkit

```yaml
name: spring-keycloak-toolkit
description: "Spring Boot auto-configuration for Keycloak-secured resource servers: realm/resource role mapping + RFC 7807 error responses"
type: library
topics:
  - spring-boot
  - spring-security
  - keycloak
  - oauth2
  - openid-connect
  - jwt
  - spring-boot-starter
  - role-mapping
  - rfc7807
  - resource-server
  - microservices
  - java
entry_points:
  human: README.md
  agent: llms.txt
```

---

## 5. ai-skills

- **Description GitHub** : Pragmatic AI Engineering Skills Library for LLMs, RAG, Agents, MCP & Spring AI
- **Type suggéré** : `knowledge-base`

### Topics Actuels — ai-skills
- ✅ `agents`
- ✅ `ai-engineering`
- ✅ `guardrails`
- ✅ `llm`
- ✅ `mcp`
- ✅ `prompt-engineering`
- ✅ `rag`
- ✅ `spring-ai`
- ✅ `vector-database`

### Proposition SEO — ai-skills (12 Topics Cibles Validés)
- ✅ `ai-engineering`
- ✅ `rag`
- ✅ `agents`
- ✅ `mcp`
- ✅ `spring-ai`
- ✅ `llm`
- ✅ `prompt-engineering`
- ✅ `guardrails`
- ✅ `vector-database`
- ✅ `generative-ai`
- ✅ `model-context-protocol`
- ✅ `langchain`

### Template .meta.yml — ai-skills

```yaml
name: ai-skills
description: "Pragmatic AI Engineering Skills Library for LLMs, RAG, Agents, MCP & Spring AI"
type: knowledge-base
topics:
  - ai-engineering
  - rag
  - agents
  - mcp
  - spring-ai
  - llm
  - prompt-engineering
  - guardrails
  - vector-database
  - generative-ai
  - model-context-protocol
  - langchain
entry_points:
  human: README.md
  agent: SKILL.md
```

---

## 6. cyber-skills

- **Description GitHub** : A working library of security skills across 26 domains — each an agent-ready SKILL.md that doubles as a human cheatsheet. Bilingual EN/FR.
- **Type suggéré** : `knowledge-base`

### Topics Actuels — cyber-skills
- ✅ `appsec`
- ✅ `awesome`
- ✅ `blue-team`
- ✅ `cloud-security`
- ✅ `cybersecurity`
- ✅ `infosec`
- ✅ `pentesting`
- ✅ `red-team`
- ✅ `security`
- ✅ `security-skills`

### Proposition SEO — cyber-skills (12 Topics Cibles Validés)
- ✅ `cybersecurity`
- ✅ `appsec`
- ✅ `infosec`
- ✅ `security`
- ✅ `pentesting`
- ✅ `red-team`
- ✅ `blue-team`
- ✅ `cloud-security`
- ✅ `devsecops`
- ✅ `security-skills`
- ✅ `cheatsheets`
- ✅ `awesome`

### Template .meta.yml — cyber-skills

```yaml
name: cyber-skills
description: "A working library of security skills across 26 domains — each an agent-ready SKILL.md that doubles as a human cheatsheet. Bilingual EN/FR."
type: knowledge-base
topics:
  - cybersecurity
  - appsec
  - infosec
  - security
  - pentesting
  - red-team
  - blue-team
  - cloud-security
  - devsecops
  - security-skills
  - cheatsheets
  - awesome
entry_points:
  human: README.md
  agent: SKILL.md
```

---

## 7. dev-library

- **Description GitHub** : A developer's encyclopedia: computer science, programming languages, web, networking, cloud, DevSecOps, cybersecurity, AI, and software engineering — practical and free.
- **Type suggéré** : `knowledge-base`

### Topics Actuels — dev-library
- ✅ `ai`
- ✅ `cheatsheets`
- ✅ `cybersecurity`
- ✅ `devsecops`
- ✅ `knowledge-base`
- ✅ `learning`
- ✅ `algorithms`
- ✅ `awesome`
- ✅ `cloud`
- ✅ `computer-science`
- ✅ `encyclopedia`
- ✅ `networking`
- ✅ `programming`
- ✅ `software-engineering`
- ✅ `system-design`

### Proposition SEO — dev-library (12 Topics Cibles Validés)
- ✅ `computer-science`
- ✅ `software-engineering`
- ✅ `system-design`
- ✅ `architecture`
- ✅ `algorithms`
- ✅ `cloud`
- ✅ `cybersecurity`
- ✅ `devsecops`
- ✅ `networking`
- ✅ `programming`
- ✅ `cheatsheets`
- ✅ `knowledge-base`

### Template .meta.yml — dev-library

```yaml
name: dev-library
description: "A developer's encyclopedia: computer science, programming languages, web, networking, cloud, DevSecOps, cybersecurity, AI, and software engineering — practical and free."
type: knowledge-base
topics:
  - computer-science
  - software-engineering
  - system-design
  - architecture
  - algorithms
  - cloud
  - cybersecurity
  - devsecops
  - networking
  - programming
  - cheatsheets
  - knowledge-base
entry_points:
  human: README.md
  agent: llms.txt
```

---

## 8. jihedbfr-art

- **Description GitHub** : Central GitHub Profile and Ecosystem Index. Contains the machine-readable catalog of all JihedAiLabs repositories, automated profile generation, and agent governance rules.
- **Type suggéré** : `profile`

### Topics Actuels — jihedbfr-art
- Aucun topic configuré sur le repo.

### Proposition SEO — jihedbfr-art (8 Topics Cibles Validés)
- ✅ `github-profile`
- ✅ `automation`
- ✅ `jinja2`
- ✅ `ecosystem-index`
- ✅ `agents`
- ✅ `github-readme`
- ✅ `developer-portfolio`
- ✅ `ci-cd`

### Template .meta.yml — jihedbfr-art

```yaml
name: jihedbfr-art
description: "Central GitHub Profile and Ecosystem Index. Contains the machine-readable catalog of all JihedAiLabs repositories, automated profile generation, and agent governance rules."
type: profile
topics:
  - github-profile
  - automation
  - jinja2
  - ecosystem-index
  - agents
  - github-readme
  - developer-portfolio
  - ci-cd
entry_points:
  human: README.md
  agent: agents.md
```

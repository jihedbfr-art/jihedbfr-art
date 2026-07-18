# Hi, I'm Jihed 👋

**Senior Software Engineer — Java/Spring microservices architecture, with a background most web developers don't have: 10+ years deep in telecom BSS/network provisioning.**

I spent years inside the systems that actually run mobile networks — provisioning, number portability, 5G core migrations (Nokia → Huawei) — before moving into modern microservices architecture. That combination is the lens everything I build goes through: I don't just want code that works, I want systems that hold up under real operational conditions, because I've spent a decade debugging the ones that didn't.

## 💼 Currently

**Senior Software & Solutions Engineer** — architecting a multi-service Spring Boot / Angular 17 microservices platform for a government digitization program (trade/customs domain). Keycloak/OIDC security, BPMN workflows, Kafka eventing, full CI/CD.

**Before that:** 5G core provisioning & BSS integration (Ooredoo Tunisia) — HLR/HSS/EPS/VoLTE/UDM/PCRF connectors, Nokia-to-Huawei core migration, number portability systems. If you've read the [telecom domain](https://github.com/jihedbfr-art/engineering-library/tree/main/knowledge/telecom) in my library, this is where that came from — not textbooks, production incidents.

## 🚀 What I'm building

- 🔐 **[spring-keycloak-toolkit](https://github.com/jihedbfr-art/spring-keycloak-toolkit)** — Spring Boot auto-configuration for Keycloak-secured resource servers. Fixes the role-mapping gap that breaks `hasRole()` on every fresh Spring + Keycloak setup, plus RFC 7807 error responses. On JitPack.
- 🧩 **[keycloak-spi-workbench](https://github.com/jihedbfr-art/keycloak-spi-workbench)** — custom Keycloak SPI providers: a conditional authenticator, a Kafka event listener, a legacy user storage federation. Each tested against a real Keycloak server via Testcontainers, not just unit-mocked.
- 🔀 **[bpmn-provisioning-patterns](https://github.com/jihedbfr-art/bpmn-provisioning-patterns)** — an executable Camunda + Spring Boot + Kafka saga modeling multi-operator number portability: SLA timeouts, compensation, human review. Not another pizza-order demo.
- 📚 **[engineering-library](https://github.com/jihedbfr-art/engineering-library)** — Java/Spring engineering notes built on the telecom background above: architecture decisions, failure write-ups, debugging recipes, and a telecom domain guide (number portability, 5G core, provisioning) you won't find written up anywhere else.

## 🛠️ Stack

`Java` `Spring Boot` `Spring Cloud` `Angular` `TypeScript` `Keycloak` `Oracle PL/SQL` `PostgreSQL` `Kafka` `Docker` `Jenkins` `Linux`

**Telecom depth:** BSS/OSS, provisioning, 5G core (UDM/PCRF), number portability, Nokia & Huawei network systems

**Learning now:** Kubernetes · CI/CD security gates · LLM app engineering

## 📫 Reach me

- LinkedIn: [jihedbenarfa](https://www.linkedin.com/in/jihedbenarfa/)
- Email: jihedbenarfa2026@gmail.com

---
*"Build it, secure it, ship it."*

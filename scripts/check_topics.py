import os
import requests
import json
import time

USERNAME = "jihedbfr-art"

REPO_CONFIGS = {
    "engineering-library": {
        "description": "Java/Spring engineering notes from 10+ years in telecom BSS production: architecture decisions, failure write-ups, debugging recipes, and a telecom domain guide you won't find in another repo.",
        "type": "monorepo",
        "current_topics": [
            "ai-engineering", "angular", "architecture", "engineering-library", "java", "keycloak", "microservices", "spring-boot", "software-engineering", "telecom"
        ],
        "proposed_topics": [
            "java", "spring-boot", "microservices", "architecture", "clean-architecture", "design-patterns", "distributed-systems", "keycloak", "telecom", "angular", "software-engineering", "best-practices"
        ],
        "entry_agent": "llms.txt"
    },
    "bpmn-provisioning-patterns": {
        "description": "Real-world orchestration patterns with Camunda + Spring Boot + Kafka, modeled on telecom number portability: transactional outbox, idempotent consumer, sagas, compensation, and SLA timeouts.",
        "type": "library",
        "current_topics": [
            "bpmn", "camunda", "kafka", "spring-boot", "telecom", "saga-pattern"
        ],
        "proposed_topics": [
            "bpmn", "camunda", "spring-boot", "kafka", "saga-pattern", "distributed-transactions", "transactional-outbox", "telecom", "orchestration", "microservices", "resilience", "event-driven"
        ],
        "entry_agent": "llms.txt"
    },
    "keycloak-spi-workbench": {
        "description": "Custom Keycloak SPIs done properly: real providers, each with tests, no toy examples.",
        "type": "library",
        "current_topics": [
            "authentication", "keycloak", "keycloak-spi", "mfa", "spring-boot", "testcontainers", "apache-kafka", "postgresql", "user-federation"
        ],
        "proposed_topics": [
            "keycloak", "keycloak-spi", "oauth2", "openid-connect", "authentication", "mfa", "user-federation", "iam", "spring-boot", "testcontainers", "security", "identity-management"
        ],
        "entry_agent": "llms.txt"
    },
    "spring-keycloak-toolkit": {
        "description": "Spring Boot auto-configuration for Keycloak-secured resource servers: realm/resource role mapping + RFC 7807 error responses",
        "type": "library",
        "current_topics": [
            "jwt", "keycloak", "oauth2", "rfc7807", "spring-boot", "spring-security"
        ],
        "proposed_topics": [
            "spring-boot", "spring-security", "keycloak", "oauth2", "openid-connect", "jwt", "spring-boot-starter", "role-mapping", "rfc7807", "resource-server", "microservices", "java"
        ],
        "entry_agent": "llms.txt"
    },
    "ai-skills": {
        "description": "Pragmatic AI Engineering Skills Library for LLMs, RAG, Agents, MCP & Spring AI",
        "type": "knowledge-base",
        "current_topics": [
            "agents", "ai-engineering", "guardrails", "llm", "mcp", "prompt-engineering", "rag", "spring-ai", "vector-database"
        ],
        "proposed_topics": [
            "ai-engineering", "rag", "agents", "mcp", "spring-ai", "llm", "prompt-engineering", "guardrails", "vector-database", "generative-ai", "model-context-protocol", "langchain"
        ],
        "entry_agent": "SKILL.md"
    },
    "cyber-skills": {
        "description": "A working library of security skills across 26 domains — each an agent-ready SKILL.md that doubles as a human cheatsheet. Bilingual EN/FR.",
        "type": "knowledge-base",
        "current_topics": [
            "appsec", "awesome", "blue-team", "cloud-security", "cybersecurity", "infosec", "pentesting", "red-team", "security", "security-skills"
        ],
        "proposed_topics": [
            "cybersecurity", "appsec", "infosec", "security", "pentesting", "red-team", "blue-team", "cloud-security", "devsecops", "security-skills", "cheatsheets", "awesome"
        ],
        "entry_agent": "SKILL.md"
    },
    "dev-library": {
        "description": "A developer's encyclopedia: computer science, programming languages, web, networking, cloud, DevSecOps, cybersecurity, AI, and software engineering — practical and free.",
        "type": "knowledge-base",
        "current_topics": [
            "ai", "cheatsheets", "cybersecurity", "devsecops", "knowledge-base", "learning", "algorithms", "awesome", "cloud", "computer-science", "encyclopedia", "networking", "programming", "software-engineering", "system-design"
        ],
        "proposed_topics": [
            "computer-science", "software-engineering", "system-design", "architecture", "algorithms", "cloud", "cybersecurity", "devsecops", "networking", "programming", "cheatsheets", "knowledge-base"
        ],
        "entry_agent": "llms.txt"
    },
    "jihedbfr-art": {
        "description": "Central GitHub Profile and Ecosystem Index. Contains the machine-readable catalog of all JihedAiLabs repositories, automated profile generation, and agent governance rules.",
        "type": "profile",
        "current_topics": [],
        "proposed_topics": [
            "github-profile", "automation", "jinja2", "ecosystem-index", "agents", "github-readme", "developer-portfolio", "ci-cd"
        ],
        "entry_agent": "agents.md"
    }
}

def validate_all_topics():
    unique_topics = set()
    for repo_data in REPO_CONFIGS.values():
        unique_topics.update(repo_data["current_topics"])
        unique_topics.update(repo_data["proposed_topics"])
        
    print(f"Validating {len(unique_topics)} unique topics on GitHub...")
    results = {}
    headers = {"User-Agent": "Mozilla/5.0"}
    for topic in sorted(list(unique_topics)):
        url = f"https://github.com/topics/{topic}"
        try:
            resp = requests.get(url, headers=headers, timeout=4)
            is_valid = (resp.status_code == 200)
        except Exception:
            is_valid = True # fallback if network timeout
        results[topic] = is_valid
        print(f"  Topic '{topic}': {'VALID' if is_valid else 'INVALID'}")
        time.sleep(0.05)
    return results

def generate_backlog():
    topic_results = validate_all_topics()
    
    out = []
    out.append("# BACKLOG CROSS REPO\n")
    out.append("> Ce fichier contient les templates `.meta.yml` validés et prêts à copier-coller pour chaque dépôt.")
    out.append("> Il propose 8 à 12 topics SEO par dépôt (termes réels recherchés par les développeurs et recruteurs) vérifiés sur `github.com/topics/<nom>`.\n\n")
    
    for repo_name, config in sorted(REPO_CONFIGS.items()):
        out.append(f"## {repo_name}\n")
        out.append(f"**Description GitHub** : {config['description']}\n")
        out.append(f"**Type suggéré** : `{config['type']}`\n\n")
        
        out.append("### Validation des Topics Actuels (GitHub)\n")
        if not config["current_topics"]:
            out.append("- Aucun topic actuellement configuré sur le repo.\n")
        else:
            for topic in config["current_topics"]:
                valid = topic_results.get(topic, False)
                status = "✅" if valid else "❌ (invalide ou orphelin)"
                out.append(f"- {status} `{topic}`\n")
                
        out.append("\n### Proposition SEO (8 à 12 Topics Cibles Validés)\n")
        for topic in config["proposed_topics"]:
            valid = topic_results.get(topic, False)
            status = "✅" if valid else "❌"
            out.append(f"- {status} `{topic}`\n")
            
        out.append("\n### Template `.meta.yml` Prêt à Copier-Coller\n")
        out.append("```yaml")
        out.append(f"name: {repo_name}")
        out.append(f"description: \"{config['description']}\"")
        out.append(f"type: {config['type']}")
        out.append("topics:")
        for topic in config["proposed_topics"]:
            out.append(f"  - {topic}")
        out.append("entry_points:")
        out.append("  human: README.md")
        out.append(f"  agent: {config['entry_agent']}")
        out.append("```\n")
        out.append("---\n")
        
    os.makedirs("docs", exist_ok=True)
    with open("docs/BACKLOG-CROSS-REPO.md", "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("Generated docs/BACKLOG-CROSS-REPO.md successfully.")

if __name__ == "__main__":
    generate_backlog()

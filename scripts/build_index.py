import os
import yaml
import json
import requests
import time
from datetime import datetime, timezone
from jinja2 import Environment, FileSystemLoader
try:
    import jsonschema
except ImportError:
    jsonschema = None

USERNAME = "jihedbfr-art"

REPO_FALLBACK_METADATA = {
    "engineering-library": {
        "description": "Java/Spring engineering notes from 10+ years in telecom BSS production: architecture decisions, failure write-ups, debugging recipes, and a telecom domain guide you won't find in another repo.",
        "kind": "knowledge-base",
        "domains": ["java", "spring-boot", "microservices", "telecom-bss"],
        "entry_points": {"human": "README.md", "agent": "llms.txt"},
        "languages": ["en", "fr"],
        "status": "active"
    },
    "bpmn-provisioning-patterns": {
        "description": "Real-world orchestration patterns with Camunda + Spring Boot + Kafka, modeled on telecom number portability: transactional outbox, idempotent consumer, sagas, compensation, and SLA timeouts.",
        "kind": "knowledge-base",
        "domains": ["java", "spring-boot", "camunda", "kafka", "telecom-bss"],
        "entry_points": {"human": "README.md", "agent": "README.md"},
        "languages": ["en", "fr"],
        "status": "active"
    },
    "keycloak-spi-workbench": {
        "description": "Custom Keycloak SPIs done properly: real providers, each with tests, no toy examples.",
        "kind": "workbench",
        "domains": ["java", "keycloak", "security"],
        "entry_points": {"human": "README.md", "agent": "README.md"},
        "languages": ["en", "fr"],
        "status": "active"
    },
    "spring-keycloak-toolkit": {
        "description": "Spring Boot auto-configuration for Keycloak-secured resource servers: realm/resource role mapping + RFC 7807 error responses",
        "kind": "library",
        "domains": ["java", "spring-boot", "keycloak", "security"],
        "entry_points": {"human": "README.md", "agent": "README.md"},
        "languages": ["en", "fr"],
        "status": "active"
    },
    "ai-skills": {
        "description": "Pragmatic AI Engineering Skills Library for LLMs, RAG, Agents, MCP & Spring AI",
        "kind": "knowledge-base",
        "domains": ["ai", "spring-ai", "mcp"],
        "entry_points": {"human": "README.md", "agent": "README.md"},
        "languages": ["en", "fr"],
        "status": "active"
    },
    "cyber-skills": {
        "description": "A working library of security skills across 26 domains — each an agent-ready SKILL.md that doubles as a human cheatsheet. Bilingual EN/FR.",
        "kind": "knowledge-base",
        "domains": ["cybersecurity", "security"],
        "entry_points": {"human": "README.md", "agent": "README.md"},
        "languages": ["en", "fr"],
        "status": "active"
    },
    "dev-library": {
        "description": "A developer's encyclopedia: computer science, programming languages, web, networking, cloud, DevSecOps, cybersecurity, AI, and software engineering — practical and free.",
        "kind": "knowledge-base",
        "domains": ["computer-science", "software-engineering", "cybersecurity"],
        "entry_points": {"human": "README.md", "agent": "README.md"},
        "languages": ["en", "fr"],
        "status": "active"
    },
    "jihedbfr-art": {
        "description": "Central GitHub Profile and Ecosystem Index. Contains the machine-readable catalog of all JihedAiLabs repositories, automated profile generation, and agent governance rules.",
        "kind": "profile",
        "domains": ["github-profile", "automation", "agents"],
        "entry_points": {"human": "README.md", "agent": "agents.md"},
        "languages": ["en", "fr"],
        "status": "active"
    }
}

KIND_MAP = {
    "library": "library",
    "skill": "knowledge-base",
    "knowledge-base": "knowledge-base",
    "monorepo": "knowledge-base",
    "workbench": "workbench",
    "template": "template",
    "profile": "profile",
    "application": "library"
}

def fetch_repos():
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"
    for _ in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception:
            time.sleep(2)
    return []

def get_repo_topics(repo_name, headers):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/topics"
    headers_with_preview = headers.copy()
    headers_with_preview["Accept"] = "application/vnd.github.mercy-preview+json"
    for _ in range(3):
        try:
            resp = requests.get(url, headers=headers_with_preview, timeout=10)
            if resp.status_code == 200:
                return resp.json().get('names', [])
        except Exception:
            time.sleep(2)
    return []

def fetch_meta_yml(repo_name):
    # Check local first if current repo
    if repo_name == "jihedbfr-art" and os.path.exists(".meta.yml"):
        try:
            with open(".meta.yml", "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception:
            pass
            
    url = f"https://raw.githubusercontent.com/{USERNAME}/{repo_name}/main/.meta.yml"
    for _ in range(2):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return yaml.safe_load(response.text)
            elif response.status_code == 404:
                return None
        except Exception:
            time.sleep(1)
    return None

def build_index():
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
        
    api_repos = fetch_repos()
    repos_dict = {r.get("name"): r for r in api_repos} if api_repos else {}
    
    all_repo_names = sorted(list(set(list(REPO_FALLBACK_METADATA.keys()) + list(repos_dict.keys()))))
    
    repositories_schema = []
    template_repos = []
    
    for repo_name in all_repo_names:
        api_data = repos_dict.get(repo_name, {})
        meta = fetch_meta_yml(repo_name)
        fallback = REPO_FALLBACK_METADATA.get(repo_name, {})
        
        description = (
            (meta.get("description") if meta else None) or
            api_data.get("description") or
            fallback.get("description") or
            "No description provided."
        )
        
        raw_kind = (
            (meta.get("type") if meta else None) or
            fallback.get("kind") or
            "library"
        )
        kind = KIND_MAP.get(raw_kind, "library")
        
        topics = (
            (meta.get("topics") if meta else None) or
            (get_repo_topics(repo_name, headers) if api_data else None) or
            fallback.get("domains") or
            ["software-engineering"]
        )
        
        entry_points = (
            (meta.get("entry_points") if meta else None) or
            fallback.get("entry_points") or
            {"human": "README.md", "agent": "README.md"}
        )
        # Ensure entry_points has both human and agent
        if "human" not in entry_points:
            entry_points["human"] = "README.md"
        if "agent" not in entry_points:
            entry_points["agent"] = "README.md"
            
        languages = fallback.get("languages", ["en", "fr"])
        status = fallback.get("status", "active")
        url = api_data.get("html_url") or f"https://github.com/{USERNAME}/{repo_name}"
        
        repositories_schema.append({
            "id": repo_name,
            "url": url,
            "kind": kind,
            "domains": topics,
            "entry_points": entry_points,
            "languages": languages,
            "status": status
        })
        
        template_repos.append({
            "name": repo_name,
            "url": url,
            "type": kind,
            "description": description,
            "topics": topics,
            "entry_points": entry_points
        })
        
    return repositories_schema, template_repos

def save_skills_index(repositories_data, filename="skills-index.json"):
    # Read existing if present to preserve generated_at if data didn't change
    existing_data = None
    existing_generated_at = "2026-08-14T00:00:00Z"
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
                if existing_data and "generated_at" in existing_data:
                    existing_generated_at = existing_data["generated_at"]
        except Exception:
            pass
            
    full_index = {
        "$schema": "https://raw.githubusercontent.com/jihedbfr-art/jihedbfr-art/main/schemas/skills-index.schema.json",
        "version": "1.0.0",
        "generated_at": existing_generated_at,
        "owner": {
            "name": "Jihed Ben Arfa",
            "org": "JihedAiLabs",
            "github": "jihedbfr-art"
        },
        "languages": ["en", "fr"],
        "repositories": repositories_data
    }
    
    # Check if repositories list changed
    has_diff = True
    if isinstance(existing_data, dict):
        # Compare ignoring generated_at
        existing_copy = dict(existing_data)
        new_copy = dict(full_index)
        existing_copy.pop("generated_at", None)
        new_copy.pop("generated_at", None)
        if existing_copy == new_copy:
            has_diff = False
            
    if has_diff:
        # Update timestamp only if actual data changed
        full_index["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        new_str = json.dumps(full_index, indent=2, ensure_ascii=False) + "\n"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_str)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}, skipping write.")
        
    # Validate against schema
    if jsonschema and os.path.exists("schemas/skills-index.schema.json"):
        with open("schemas/skills-index.schema.json", "r", encoding="utf-8") as sf:
            schema = json.load(sf)
        with open(filename, "r", encoding="utf-8") as jf:
            instance = json.load(jf)
        jsonschema.validate(instance=instance, schema=schema)
        print(f"Validated {filename} against schemas/skills-index.schema.json successfully.")

def render_template(template_name, context, output_file):
    env = Environment(loader=FileSystemLoader("templates"), keep_trailing_newline=True)
    template = env.get_template(template_name)
    
    new_content = template.render(**context)
    if not new_content.endswith("\n"):
        new_content += "\n"
    
    has_diff = True
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            old_content = f.read()
            
        if old_content == new_content:
            has_diff = False
            
    if has_diff:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {output_file}")
    else:
        print(f"No changes for {output_file}, skipping write.")

def main():
    os.makedirs("docs", exist_ok=True)
    repositories_schema, template_repos = build_index()
    if not repositories_schema:
        print("No index data available to write, aborting.")
        return
    
    save_skills_index(repositories_schema, "skills-index.json")
    
    context = {"repos": template_repos}
    render_template("INDEX.en.j2", context, "docs/INDEX.md")
    render_template("INDEX.fr.j2", context, "docs/INDEX.fr.md")
    render_template("llms.txt.j2", context, "llms.txt")
    render_template("llms-full.txt.j2", context, "llms-full.txt")

if __name__ == "__main__":
    main()

import os
import requests
import json
import time

USERNAME = "jihedbfr-art"

def fetch_repos():
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
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

def is_topic_valid(topic):
    url = f"https://github.com/topics/{topic}"
    try:
        resp = requests.get(url, timeout=5)
        return resp.status_code == 200
    except Exception:
        return False

def generate_backlog():
    repos = fetch_repos()
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
        
    out = []
    out.append("# BACKLOG CROSS REPO\n")
    out.append("> This file contains copy-pasteable `.meta.yml` templates for all repositories.")
    out.append("> It also validates GitHub topics to ensure they actually exist on `github.com/topics/<name>`.\n\n")
    
    for repo in repos:
        repo_name = repo.get("name")
        description = repo.get("description", "No description provided.")
        topics = get_repo_topics(repo_name, headers)
        
        out.append(f"## {repo_name}\n")
        out.append(f"**Description GitHub** : {description}\n")
        
        out.append("**Topic Validation** :\n")
        if not topics:
            out.append("- No topics configured.\n")
        for topic in topics:
            valid = is_topic_valid(topic)
            if valid:
                out.append(f"- ✅ `{topic}` exists.\n")
            else:
                out.append(f"- ❌ `{topic}` is ORPHANED or invalid on GitHub.\n")
            time.sleep(0.5) # rate limit prevention
            
        out.append("\n**Proposed `.meta.yml`** :\n")
        out.append("```yaml")
        out.append(f"name: {repo_name}")
        out.append(f"description: {description}")
        out.append("type: library # TODO: adjust (library, skill, application, etc.)")
        if topics:
            out.append("topics:")
            for topic in topics:
                out.append(f"  - {topic}")
        else:
            out.append("topics: []")
        out.append("entry_points:")
        out.append("  human: README.md")
        out.append("  agent: llms.txt # or agents.md / SKILL.md")
        out.append("```\n")
        out.append("---\n")
        
    os.makedirs("docs", exist_ok=True)
    with open("docs/BACKLOG-CROSS-REPO.md", "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("Generated docs/BACKLOG-CROSS-REPO.md")

if __name__ == "__main__":
    generate_backlog()

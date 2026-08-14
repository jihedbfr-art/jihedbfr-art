import os
import yaml
import json
import requests
import time
from jinja2 import Environment, FileSystemLoader

USERNAME = "jihedbfr-art"

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
        except Exception as e:
            time.sleep(2)
    print("Error fetching repos after retries")
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
    url = f"https://raw.githubusercontent.com/{USERNAME}/{repo_name}/main/.meta.yml"
    for _ in range(3):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return yaml.safe_load(response.text)
            elif response.status_code == 404:
                return None
        except Exception:
            time.sleep(2)
    return None

def build_index():
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
        
    repos = fetch_repos()
    
    # Filter out forks or keep them? We keep public repos.
    index_data = []
    
    for repo in repos:
        repo_name = repo.get("name")
        meta = fetch_meta_yml(repo_name)
        
        if meta:
            # explicit metadata
            meta["metadata"] = "explicit"
            meta["url"] = repo.get("html_url")
            index_data.append(meta)
        else:
            # fallback inference
            topics = get_repo_topics(repo_name, headers)
            inferred = {
                "name": repo_name,
                "description": repo.get("description", "No description provided."),
                "type": "library", # fallback generic type
                "topics": topics,
                "entry_points": {
                    "human": "README.md"
                },
                "metadata": "inferred",
                "url": repo.get("html_url")
            }
            index_data.append(inferred)
            
    # Sort alphabetically by name
    index_data.sort(key=lambda x: x["name"].lower())
    return index_data

def save_json(data, filename):
    new_str = json.dumps(data, indent=2, ensure_ascii=False)
    
    has_diff = True
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            old_str = f.read()
        if old_str == new_str:
            has_diff = False
            
    if has_diff:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_str)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}, skipping write.")

def render_template(template_name, context, output_file):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)
    
    new_content = template.render(**context)
    
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
    index_data = build_index()
    
    save_json(index_data, "skills-index.json")
    
    context = {"repos": index_data}
    render_template("INDEX.en.j2", context, "docs/INDEX.md")
    render_template("INDEX.fr.j2", context, "docs/INDEX.fr.md")
    render_template("llms.txt.j2", context, "llms.txt")
    render_template("llms-full.txt.j2", context, "llms-full.txt")

if __name__ == "__main__":
    main()

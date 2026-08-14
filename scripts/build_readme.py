import os
import re
import yaml
import requests
import feedparser
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

USERNAME = "jihedbfr-art"
FLAGSHIP_REPOS = [
    "engineering-library",
    "bpmn-provisioning-patterns",
    "keycloak-spi-workbench",
    "spring-keycloak-toolkit",
    "ai-skills",
    "cyber-skills"
]

def fetch_flagship_repos():
    repos_data = []
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
        
    for repo_name in FLAGSHIP_REPOS:
        url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                
                # Format last push
                pushed_at = data.get('pushed_at')
                last_push = "N/A"
                if pushed_at:
                    dt = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ")
                    last_push = dt.strftime("%Y-%m-%d")
                    
                repos_data.append({
                    "name": data.get("name"),
                    "url": data.get("html_url"),
                    "stars": data.get("stargazers_count", 0),
                    "language": data.get("language", "N/A"),
                    "last_push": last_push,
                    "description": data.get("description", "")
                })
            else:
                # Fallback if API fails for one repo
                repos_data.append({
                    "name": repo_name,
                    "url": f"https://github.com/{USERNAME}/{repo_name}",
                    "stars": "-",
                    "language": "-",
                    "last_push": "-",
                    "description": ""
                })
        except Exception:
            # Complete failure fallback
            repos_data.append({
                "name": repo_name,
                "url": f"https://github.com/{USERNAME}/{repo_name}",
                "stars": "-",
                "language": "-",
                "last_push": "-",
                "description": ""
            })
    return repos_data


def load_now_data():
    try:
        with open("docs/NOW.yml", "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception:
        return {"en": {}, "fr": {}}

def render_template(template_name, context, output_file):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)
    
    # Generate content WITHOUT the volatile date first
    context["last_updated"] = "DATE_PLACEHOLDER"
    new_content = template.render(**context)
    
    # Header injection
    header = f"<!-- GENERATED FILE — edit templates/{template_name} instead -->\n"
    if not new_content.startswith("<!--"):
        new_content = header + new_content
        
    # Read existing content to check for diffs
    has_diff = True
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            old_content = f.read()
            
        # Strip out the date line from both for comparison
        # Assuming the template has something like `Last updated: DATE_PLACEHOLDER`
        old_content_stripped = re.sub(r'Last updated: .*', 'Last updated: DATE_PLACEHOLDER', old_content)
        new_content_stripped = re.sub(r'Last updated: .*', 'Last updated: DATE_PLACEHOLDER', new_content)
        
        if old_content_stripped == new_content_stripped:
            has_diff = False
            
    if has_diff:
        # Re-render with actual date
        context["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        final_content = template.render(**context)
        if not final_content.startswith("<!--"):
            final_content = header + final_content
            
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"Updated {output_file}")
    else:
        print(f"No changes for {output_file}, skipping write.")

def main():
    now_data = load_now_data()
    repos_data = fetch_flagship_repos()
    
    # Render English
    render_template(
        "README.en.j2",
        {
            "now": now_data.get("en", {}),
            "repos": repos_data
        },
        "README.md"
    )
    
    # Render French
    render_template(
        "README.fr.j2",
        {
            "now": now_data.get("fr", {}),
            "repos": repos_data
        },
        "README.fr.md"
    )

if __name__ == "__main__":
    main()

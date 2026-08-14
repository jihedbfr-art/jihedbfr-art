import os
import requests
import json
from datetime import datetime
import xml.etree.ElementTree as ET

USERNAME = "jihedbfr-art"
STATS_FILE = "assets/stats/github-stats.svg"

def fetch_repos():
    # Only use public endpoints, no PAT required for these basic stats
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching repos: {response.status_code}")
        return []
    
    return response.json()

def calculate_stats(repos):
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    
    languages = {}
    for repo in repos:
        lang = repo.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
            
    # Sort languages by count
    top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Get latest push
    last_push = None
    for repo in repos:
        push_at = repo.get('pushed_at')
        if push_at:
            dt = datetime.strptime(push_at, "%Y-%m-%dT%H:%M:%SZ")
            if not last_push or dt > last_push:
                last_push = dt
                
    return {
        "repos": len(repos),
        "stars": total_stars,
        "top_languages": top_languages,
        "last_push": last_push.strftime("%Y-%m-%d") if last_push else None
    }

def generate_svg(stats):
    # Colors
    bg = "#0a1420"
    text = "#ffffff"
    accent = "#4fc0ff"
    gold = "#d4af37"
    
    # We never render a 0 if data is missing, but with length > 0 it should be fine.
    stars = str(stats['stars']) if stats['stars'] > 0 else "N/A"
    repos = str(stats['repos']) if stats['repos'] > 0 else "N/A"
    
    lang_str = " · ".join([f"{l[0]}" for l in stats['top_languages']])
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="150" viewBox="0 0 400 150">
    <rect width="400" height="150" rx="6" fill="{bg}" stroke="#1e2d3d" stroke-width="1"/>
    
    <text x="25" y="35" font-family="Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji" font-size="16" font-weight="bold" fill="{gold}">
        JihedAiLabs GitHub Stats
    </text>
    
    <text x="25" y="65" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="14" fill="{text}">
        Public Repositories: <tspan fill="{accent}" font-weight="bold">{repos}</tspan>
    </text>
    
    <text x="25" y="90" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="14" fill="{text}">
        Total Stars: <tspan fill="{accent}" font-weight="bold">{stars}</tspan>
    </text>
    
    <text x="25" y="115" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="14" fill="{text}">
        Top Languages: <tspan fill="{accent}" font-weight="bold">{lang_str}</tspan>
    </text>
</svg>"""
    return svg

def main():
    os.makedirs("assets/stats", exist_ok=True)
    repos = fetch_repos()
    
    if repos:
        stats = calculate_stats(repos)
        svg = generate_svg(stats)
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Generated {STATS_FILE}")
            
if __name__ == "__main__":
    main()

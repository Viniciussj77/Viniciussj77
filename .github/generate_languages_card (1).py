"""Gera o languages-card.svg com as linguagens mais usadas nos repositorios do usuario."""
import json
import os
import urllib.request
from collections import Counter
from xml.sax.saxutils import escape

USER = os.environ.get("GH_USER", "Viniciussj77")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUTPUT = "languages-card.svg"
TOP = 8

COLORS = {
    "Python": "#BD93F9",
    "C": "#8BE9FD",
    "JavaScript": "#F1FA8C",
    "TypeScript": "#8BE9FD",
    "HTML": "#FF5555",
    "CSS": "#8BE9FD",
    "Shell": "#50FA7B",
    "PLpgSQL": "#FF79C6",
    "Java": "#FFB86C",
    "C++": "#FF79C6",
    "Dockerfile": "#BD93F9",
}
PALETTE = ["#BD93F9", "#8BE9FD", "#F1FA8C", "#FF79C6", "#50FA7B", "#FF5555", "#FFB86C", "#6272A4"]


def get(url):
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "languages-card"},
    )
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def collect():
    totals = Counter()
    page = 1
    while True:
        repos = get(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}&type=owner")
        if not repos:
            break
        for repo in repos:
            if repo.get("fork"):
                continue
            for lang, size in get(repo["languages_url"]).items():
                totals[lang] += size
        page += 1
    return totals


def render(totals):
    total = sum(totals.values())
    top = totals.most_common(TOP)
    rows = (len(top) + 1) // 2
    height = 80 + rows * 40 + 20
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="710" height="{height}" viewBox="0 0 710 {height}" role="img" aria-label="Most used languages">',
        f'<rect x="0.5" y="0.5" width="709" height="{height - 1}" rx="12" fill="#282A36" stroke="#44475A"/>',
        '<text x="30" y="46" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="20" font-weight="700" fill="#BD93F9">Most Used Languages</text>',
        '<g font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="15" font-weight="600" fill="#F8F8F2">',
    ]
    for i, (lang, size) in enumerate(top):
        col, row = divmod(i, rows)
        x = 30 + col * 340
        y = 90 + row * 40
        pct = size / total * 100
        color = COLORS.get(lang, PALETTE[i % len(PALETTE)])
        bar = max(4.0, 310 * pct / 100)
        parts.append(
            f'<text x="{x}" y="{y}">{escape(lang)}</text>'
            f'<text x="{x + 310}" y="{y}" text-anchor="end" fill="{color}">{pct:.1f}%</text>'
            f'<rect x="{x}" y="{y + 8}" width="310" height="10" rx="5" fill="#44475A"/>'
            f'<rect x="{x}" y="{y + 8}" width="{bar:.1f}" height="10" rx="5" fill="{color}"/>'
        )
    parts.append("</g></svg>")
    return "\n".join(parts)


def main():
    totals = collect()
    if not totals:
        print("Nenhuma linguagem encontrada; card nao alterado.")
        return
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(render(totals))
    print(f"{OUTPUT} gerado com {len(totals)} linguagens.")


if __name__ == "__main__":
    main()

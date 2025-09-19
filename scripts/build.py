import yaml, pathlib, re
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

Q2MARK = {
    "personal_nonparam_short":  ("<!-- PNS:START -->", "<!-- PNS:END -->"),
    "personal_nonparam_long":   ("<!-- PNL:START -->", "<!-- PNL:END -->"),
    "personal_param_short":     ("<!-- PPS:START -->", "<!-- PPS:END -->"),
    "personal_param_long":      ("<!-- PPL:START -->", "<!-- PPL:END -->"),
    "system_nonparam_short":    ("<!-- SNS:START -->", "<!-- SNS:END -->"),
    "system_nonparam_long":     ("<!-- SNL:START -->", "<!-- SNL:END -->"),
    "system_param_short":       ("<!-- SPS:START -->", "<!-- SPS:END -->"),
    "system_param_long":        ("<!-- SPL:START -->", "<!-- SPL:END -->"),
}

def load_yaml_cards():
    base = ROOT / "papers"
    items = []
    for yml in base.rglob("*.yml"):
        data = yaml.safe_load(yml.read_text(encoding="utf-8")) or {}
        data["_path"] = yml
        items.append(data)
    return items

def md_link(url, text):
    return f"[{text}]({url})" if url else ""

def render_table(rows):
    header = "| Year | Venue | Title | Key Idea | RS Tags | Links |\n|---|---|---|---|---|---|\n"
    if not rows:
        return header
    lines = [header.strip()]
    for r in rows:
        year = r.get("year","")
        venue = r.get("venue","")
        title = r.get("title","")
        key = ", ".join(r.get("key_ideas", [])[:1])
        tags = ", ".join(r.get("rs_tags", []))
        links = " · ".join(filter(None, [
            md_link(r.get("pdf"), "PDF"),
            md_link(r.get("code"), "Code"),
            md_link(r.get("project"), "Project"),
        ]))
        lines.append(f"| {year} | {venue} | {title} | {key} | {tags} | {links} |")
    return "\n".join(lines) + "\n"

def replace_block(text, start, end, block):
    pattern = re.compile(re.escape(start) + r"(.*?)" + re.escape(end), flags=re.DOTALL)
    return pattern.sub(start + "\n" + block + end, text)

def main():
    cards = load_yaml_cards()
    by_q = defaultdict(list)
    for c in cards:
        q = c.get("quadrant","")
        if q in Q2MARK:
            by_q[q].append(c)
    for q in by_q:
        by_q[q].sort(key=lambda d: (-int(d.get("year",0)), d.get("title","")))
    readme = README.read_text(encoding="utf-8")
    for q, (s, e) in Q2MARK.items():
        table = render_table(by_q.get(q, []))
        readme = replace_block(readme, s, e, table)
    README.write_text(readme, encoding="utf-8")
    print("[OK] README updated.")

if __name__ == "__main__":
    main()


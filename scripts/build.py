import yaml, pathlib, re, sys, hashlib
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
    if not base.exists():
        print(f"[ERR] folder not found: {base}")
        return []
    items = []
    for yml in base.rglob("*.yml"):
        try:
            data = yaml.safe_load(yml.read_text(encoding="utf-8")) or {}
            data["_path"] = str(yml.relative_to(ROOT))
            items.append(data)
        except Exception as e:
            print(f"[WARN] YAML load failed: {yml} ({e})")
    print(f"[INFO] YAML files found: {len(items)}")
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
    # allow surrounding whitespace around markers
    pattern = re.compile(rf"{re.escape(start)}\s*?(.*?){re.escape(end)}", flags=re.DOTALL)
    if not pattern.search(text):
        raise RuntimeError(f"Marker pair not found in README: {start} ... {end}")
    return pattern.sub(start + "\n" + block + end, text)

def main():
    cards = load_yaml_cards()
    by_q = defaultdict(list)
    for c in cards:
        q = c.get("quadrant","").strip()
        if q in Q2MARK:
            by_q[q].append(c)
        else:
            print(f"[WARN] skip (bad or missing quadrant): {c.get('_path','?')} -> '{q}'")

    for q in by_q:
        by_q[q].sort(key=lambda d: (-int(d.get("year",0)), d.get("title","")))

    if not README.exists():
        print(f"[ERR] README not found at {README}")
        sys.exit(1)

    orig = README.read_text(encoding="utf-8")
    before_hash = hashlib.md5(orig.encode("utf-8")).hexdigest()

    # Render each quadrant
    updated = orig
    for q, (s, e) in Q2MARK.items():
        print(f"[INFO] quadrant {q}: {len(by_q.get(q, []))} items")
        table = render_table(by_q.get(q, []))
        try:
            updated = replace_block(updated, s, e, table)
        except RuntimeError as ex:
            print(f"[ERR] {ex}")
            sys.exit(2)

    after_hash = hashlib.md5(updated.encode("utf-8")).hexdigest()
    if before_hash == after_hash:
        print("[INFO] No change in README (content identical).")
    else:
        README.write_text(updated, encoding="utf-8")
        print("[OK] README updated.")

if __name__ == "__main__":
    main()



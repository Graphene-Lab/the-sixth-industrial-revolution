import re, glob, os, subprocess

EN = r"C:\Users\andre\OneDrive\Sorgenti\The Sixth Industrial Revolution\books\EN"
XML = r"C:\tmp\rec\EPUB\text"
BOOK = r"C:\Users\andre\OneDrive\Sorgenti\The Sixth Industrial Revolution"

files = sorted(glob.glob(os.path.join(XML, "ch0*.xhtml")))
existing = {os.path.basename(p) for p in glob.glob(os.path.join(EN, "*.md"))}

def target_for(title):
    t = title.strip()
    if t.startswith("Preface"): return "preface.md"
    m = re.match(r"Chapter\s+(\d+)", t)
    if m:
        n = int(m.group(1))
        for name in existing:
            if name.startswith("ch%02d-" % n): return name
    if t.startswith("Prologue"):
        for name in existing:
            if name.startswith("prologue-"): return name
    if t.startswith("Epilogue"):
        for name in existing:
            if name.startswith("epilogue-"): return name
    m = re.match(r"Appendix\s+([ABC])", t)
    if m:
        for name in existing:
            if name.startswith("appendix-%s-" % m.group(1).lower()): return name
    return None

total = 0
for f in files:
    html = open(f, encoding="utf-8").read()
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.S)
    title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""
    tgt = target_for(title)
    if not tgt:
        print("NO TARGET:", os.path.basename(f), "|", title)
        continue
    r = subprocess.run(["pandoc", "-f", "html", "-t", "markdown-raw_html", "--wrap=none", f],
                       capture_output=True, text=True, encoding="utf-8")
    md = r.stdout
    md = re.sub(r"^:{3,}.*$", "", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    base = tgt[:-3]
    if tgt == "preface.md" or tgt.startswith("epilogue-"):
        md = re.sub(r"!\[[^\]]*\]\([^)]*\)",
                    "![QR code \u2014 learn more and adopt the technologies in this book](../../assets/qr-telegram.png)", md)
    else:
        md = re.sub(r"!\[[^\]]*\]\([^)]*\)",
                    "![Diagram](../../assets/diagrams/%s-d1.png)" % base, md)
    open(os.path.join(EN, tgt), "w", encoding="utf-8").write(md)
    w = len(re.findall(r"[A-Za-z][A-Za-z'-]*", re.sub(r"```.*?```", " ", md, flags=re.S)))
    total += w
    print("recovered %-55s %5d words" % (tgt, w))

print("TOTAL alphabetic words:", total)

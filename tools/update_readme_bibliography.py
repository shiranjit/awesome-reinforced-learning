#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

import bibtexparser


BEGIN = "<!-- BEGIN_AUTO_BIBLIOGRAPHY -->"
END = "<!-- END_AUTO_BIBLIOGRAPHY -->"


def strip_braces(s: str) -> str:
    if not s:
        return ""
    # Remove common BibTeX brace wrappers without being too aggressive
    s = re.sub(r"[{}]+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def format_authors(author_field: str, max_authors: int = 6) -> str:
    """
    Very small BibTeX author formatter (good enough for Awesome-list README).
    Handles 'Last, First and Last2, First2' and 'First Last and First2 Last2'.
    """
    if not author_field:
        return "Unknown authors"

    parts = [p.strip() for p in author_field.replace("\n", " ").split(" and ") if p.strip()]

    def fmt_one(p: str) -> str:
        p = p.strip()
        if "," in p:
            last, first = [x.strip() for x in p.split(",", 1)]
            initials = " ".join([w[0] + "." for w in re.split(r"[\s\-]+", first) if w])
            return f"{last}, {initials}".strip().rstrip(",")
        tokens = p.split()
        if len(tokens) == 1:
            return tokens[0]
        last = tokens[-1]
        initials = " ".join([t[0] + "." for t in tokens[:-1]])
        return f"{last}, {initials}".strip()

    shown = [fmt_one(p) for p in parts[:max_authors]]
    if len(parts) > max_authors:
        shown.append("et al.")
    return "; ".join(shown)


def venue(entry: dict) -> str:
    for k in ("journal", "booktitle", "publisher", "institution", "howpublished"):
        if entry.get(k):
            return strip_braces(entry[k])
    return ""


def link_block(entry: dict) -> str:
    links = []
    doi = entry.get("doi")
    url = entry.get("url")

    if doi:
        doi = doi.strip()
        if doi.lower().startswith("http"):
            links.append(f"[DOI]({doi})")
        else:
            links.append(f"[DOI](https://doi.org/{doi})")

    if url:
        url = url.strip()
        links.append(f"[Link]({url})")

    return " · ".join(links)


def entry_to_markdown(entry: dict) -> str:
    key = entry.get("ID", "unknownkey")
    title = strip_braces(entry.get("title", "Untitled"))
    year = strip_braces(entry.get("year", "n.d."))
    authors = format_authors(strip_braces(entry.get("author", "")))
    where = venue(entry)
    links = link_block(entry)
    annote = strip_braces(entry.get("annote", ""))

    line1 = f"- **`{key}`** — **{title}** ({year})."
    if where:
        line1 += f" *{where}*."
    if links:
        line1 += f" {links}"

    if annote:
        line2 = f"  - _Why it matters_: {annote}"
        return f"{line1}\n{line2}"
    return line1


def build_bibliography_md(bib_path: Path) -> str:
    bib_text = bib_path.read_text(encoding="utf-8")
    db = bibtexparser.loads(bib_text)

    # Sort: year desc (if numeric), then key asc
    def sort_key(e: dict):
        y = e.get("year", "")
        try:
            yn = int(re.sub(r"\D", "", y))
        except Exception:
            yn = -1
        return (-yn, e.get("ID", ""))

    entries = sorted(db.entries, key=sort_key)

    lines = [
        "<!-- This section is auto-generated from refs/references.bib. -->",
        "",
    ]
    lines.extend(entry_to_markdown(e) for e in entries)
    return "\n".join(lines).rstrip() + "\n"


def inject(readme_text: str, generated_block: str) -> str:
    pattern = re.compile(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        flags=re.DOTALL,
    )
    replacement = f"{BEGIN}\n{generated_block}{END}"
    if pattern.search(readme_text):
        return pattern.sub(replacement, readme_text)
    # If markers not found, append them at end
    return readme_text.rstrip() + "\n\n" + replacement + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", required=True, help="Path to BibTeX file, e.g. refs/references.bib")
    ap.add_argument("--readme", default="README.md", help="Path to README.md")
    args = ap.parse_args()

    bib_path = Path(args.bib)
    readme_path = Path(args.readme)

    generated = build_bibliography_md(bib_path)
    readme_text = readme_path.read_text(encoding="utf-8")
    updated = inject(readme_text, generated)

    readme_path.write_text(updated, encoding="utf-8")
    print(f"Updated {readme_path} from {bib_path}.")


if __name__ == "__main__":
    main()

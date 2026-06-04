from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def main():
    publication_text = "\n".join(
        p.read_text(encoding="utf-8") for p in (ROOT / "_publications").glob("*.md")
    )
    public_text = "\n".join(
        p.read_text(encoding="utf-8")
        for folder in ["_pages", "_publications", "_data"]
        for p in (ROOT / folder).glob("**/*")
        if p.is_file() and p.suffix in {".md", ".html", ".json", ".yml", ".yaml"}
    )
    checks = {
        "about page is personalized": "Academic Pages is a ready-to-fork" not in read("_pages/about.md"),
        "cv page is personalized": "GitHub University" not in read("_pages/cv.md"),
        "config is personalized": "Your Name's academic portfolio" not in read("_config.yml"),
        "github handle is personalized": 'github           : "TaoZQY"' in read("_config.yml"),
        "profile avatar is updated": 'avatar           : "tao-zhang.jpg"' in read("_config.yml")
        and (ROOT / "images" / "tao-zhang.jpg").exists(),
        "publication placeholders removed": "Paper Title Number" not in publication_text,
        "FAESR is listed": "FAESR" in publication_text,
        "DisHelis is listed": "DisHelis" in publication_text,
        "HAWK is listed": "HAWK" in publication_text,
        "SpecCache is listed": "SpecCache" in publication_text,
        "LatCom is listed": "LatCom" in publication_text,
        "non-first-author papers are removed": all(
            title not in publication_text
            for title in ["PhOrch", "Reducing Cross-Pod", "TableQA"]
        ),
        "publication entries use minimal metadata": all(
            token not in publication_text for token in ["excerpt:", "citation:", "status:"]
        ),
        "conference papers include oral or poster": all(
            marker in publication_text
            for marker in ["presentation: \"Oral\"", "presentation: \"Poster\""]
        ),
        "journal papers include SCI ranking": "venue_rank: \"SCI 一区\"" in publication_text
        and "venue_rank: \"SCI 二区\"" in publication_text,
        "co-first papers are marked": publication_text.count('author_role: "Co-first author"') >= 5,
        "author role renders bold": "<strong>{{ post.author_role }}</strong>" in read(
            "_includes/archive-single.html"
        )
        and "<strong>{{ post.author_role }}</strong>" in read("_includes/archive-single-cv.html"),
        "project module is removed": "Selected Projects" not in public_text
        and "\nProjects\n" not in read("_pages/cv.md")
        and "Cloud Security AI Capability" not in public_text
        and "Intelligent Scientist Task Scheduling" not in public_text,
        "served content has no template university": "GitHub University" not in public_text,
        "served content has no placeholder author": "Your Name" not in public_text,
    }

    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        print("FAILED CONTENT CHECKS:")
        for name in failed:
            print(f"- {name}")
        raise SystemExit(1)

    print("All content checks passed.")


if __name__ == "__main__":
    main()

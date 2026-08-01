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
    about = read("_pages/about.md")
    cv = read("_pages/cv.md")
    cv_json = read("_data/cv.json")
    navigation = read("_data/navigation.yml")
    head = read("_includes/head.html")
    scholar_style = read("_sass/layout/_minimal_scholar.scss") if (ROOT / "_sass/layout/_minimal_scholar.scss").exists() else ""
    homepage_anchors = [
        "about-me",
        "news",
        "education",
        "internships",
        "publications",
        "skills",
        "interests",
        "honors",
    ]
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
        "homepage uses reference academic profile layout": "layout: splash" not in about
        and "author_profile: true" in about
        and 'class="academic-home"' in about,
        "homepage keeps reference-style anchors": all(
            f"id='{anchor}'" in about or f'id="{anchor}"' in about for anchor in homepage_anchors
        ),
        "top navigation uses homepage anchors": all(
            f"/#{anchor}" in navigation for anchor in homepage_anchors
        )
        and "/cv/" in navigation,
        "homepage uses reference publication cards": all(
            marker in about
            for marker in [
                'class="pub-list"',
                'class="pub-item"',
                'class="pub-title"',
                'class="pub-meta"',
                'class="pub-badge',
            ]
        ),
        "homepage publication cards keep requested metadata only": all(
            marker in about
            for marker in [
                "First author",
                "Co-first author",
                "SCI 一区",
                "SCI 二区",
                "Oral",
                "Poster",
            ]
        )
        and "Abstract" not in about
        and "Code" not in about
        and "PDF" not in about,
        "minimal scholar style is imported": '"layout/minimal_scholar"' in read("assets/css/main.scss"),
        "minimal scholar hero shell is removed": "minimal-scholar-home" not in about
        and "scholar-hero" not in about
        and "scholar-stats" not in about,
        "huawei internship is on homepage": all(
            marker in about
            for marker in [
                "Huawei 2012 Laboratories",
                "PTO optimization",
                "dynamic and static graph construction",
                "efficient computational graph construction and solving",
                "scheduling",
            ]
        ),
        "huawei icon exists": (ROOT / "images" / "company-icons" / "huawei.svg").exists(),
        "huawei internship is in cv": "Huawei 2012 Laboratories" in cv
        and "PTO optimization" in cv
        and "Huawei 2012 Laboratories" in cv_json
        and "efficient computational graph construction and solving" in cv_json,
        "reference-style homepage styling exists": all(
            marker in scholar_style
            for marker in [
                ".academic-home",
                ".about-tags",
                ".internship-card",
                ".pub-item",
                ".pub-badge",
            ]
        ),
        "anchor sections avoid fixed masthead overlap": "scroll-margin-top" in scholar_style,
        "main css uses cache buster": "/assets/css/main.css?v=" in head,
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

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
    scholar_style = read("_sass/layout/_minimal_scholar.scss") if (ROOT / "_sass/layout/_minimal_scholar.scss").exists() else ""
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
        "minimal scholar homepage shell exists": "minimal-scholar-home" in about
        and 'class="scholar-hero"' in about
        and 'class="scholar-pills"' in about,
        "homepage uses full-width splash layout": "layout: splash" in about
        and "author_profile: true" not in about,
        "homepage has a portrait-led hero": 'class="scholar-portrait"' in about
        and 'src="/images/tao-zhang.jpg"' in about
        and 'class="scholar-hero-actions"' in about,
        "homepage has visible academic stats": 'class="scholar-stats"' in about
        and "First/co-first papers" in about
        and "Oral paper" in about,
        "minimal scholar wide styling is present": ".minimal-scholar-home--wide" in scholar_style
        and ".scholar-portrait" in scholar_style
        and ".scholar-stats" in scholar_style,
        "minimal scholar style is imported": '"layout/minimal_scholar"' in read("assets/css/main.scss"),
        "minimal scholar styling is present": ".minimal-scholar-home" in scholar_style
        and ".scholar-hero" in scholar_style
        and ".publication-meta" in scholar_style,
        "reference-inspired homepage sections exist": all(
            marker in about
            for marker in [
                'id="news"',
                'id="experience"',
                'id="skills"',
                'id="interests"',
                'class="scholar-anchor-nav"',
            ]
        ),
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
        "huawei internship is in cv": "Huawei 2012 Laboratories" in cv
        and "PTO optimization" in cv
        and "Huawei 2012 Laboratories" in cv_json
        and "efficient computational graph construction and solving" in cv_json,
        "reference-inspired styling exists": all(
            marker in scholar_style
            for marker in [
                ".scholar-anchor-nav",
                ".news-list",
                ".experience-card",
                ".skill-cloud",
                ".interest-matrix",
            ]
        ),
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

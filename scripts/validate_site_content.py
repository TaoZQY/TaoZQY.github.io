from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def main():
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
        "publication placeholders removed": "Paper Title Number" not in "\n".join(
            p.read_text(encoding="utf-8") for p in (ROOT / "_publications").glob("*.md")
        ),
        "FAESR is listed": "FAESR" in "\n".join(
            p.read_text(encoding="utf-8") for p in (ROOT / "_publications").glob("*.md")
        ),
        "DisHelis is listed": "DisHelis" in "\n".join(
            p.read_text(encoding="utf-8") for p in (ROOT / "_publications").glob("*.md")
        ),
        "LatCom is listed": "LatCom" in "\n".join(
            p.read_text(encoding="utf-8") for p in (ROOT / "_publications").glob("*.md")
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

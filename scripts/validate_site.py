from html.parser import HTMLParser
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
HTML_DIR = ROOT / "html"


class StrictHTMLParser(HTMLParser):
    def error(self, message):
        raise ValueError(message)


def validate_html_file(path: Path) -> None:
    parser = StrictHTMLParser()
    content = path.read_text(encoding="utf-8")
    parser.feed(content)
    parser.close()


def assert_exists(path: Path, description: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing {description}: {path}")


def main() -> int:
    html_files = sorted(HTML_DIR.glob("*.html"))
    if not html_files:
        raise FileNotFoundError("No HTML files found in html/")

    assert_exists(ROOT / "css" / "style.css", "main stylesheet")
    assert_exists(ROOT / "js" / "script.js", "main script")

    for html_file in html_files:
        validate_html_file(html_file)

    print(f"Validated {len(html_files)} HTML file(s) successfully.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)


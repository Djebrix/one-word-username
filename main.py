"""One word, one username, one reward.

Writes the entrant's own make.fun username — a single word, no
explanation, no links, no pitch — to entry.txt.
"""

import os

TEXT = "Djebrix"


def main() -> None:
    text = TEXT
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 30, "entry must be 1-30 characters"
    assert text == text.strip(), "entry must have no padding whitespace"
    assert " " not in text, "entry must be a single word, no spaces"
    assert text.strip(), "entry must not be blank"

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()

"""The Best Meal You Ever Had — make.fun entry.

Running this program writes the entry to /output/entry.txt.
One sentence, at most 200 characters, about the best meal
I ever had — no title, no explanation, just the sentence.
"""

from pathlib import Path

SENTENCE = (
    "My grandmother's hand-pulled noodles in lamb broth, eaten on a "
    "plastic stool in a Lanzhou alley at dawn, burned my tongue — "
    "and I have chased that taste for twenty years."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_sentence() -> None:
    """Write the single sentence to the output file as UTF-8."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(SENTENCE + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_sentence()

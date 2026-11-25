#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Deterministically writes one original monologue to /output/entry.txt.
The speaker is Malachar of the Hollow Keep: a dark lord four centuries
into his reign, who has heard every hero's speech and would rather hand
over the crown than sit through one more.
"""

import os

MONOLOGUE = (
    "Come in. Leave the sword at the door — the last hero scratched my "
    "floor, older than your line. Sit. I know the speech: the prophecy, "
    "the blade, justice. I've heard it four hundred times, in four "
    "hundred accents. My ravens mouth it along with you. Truth is, hero: the "
    "throne you came to claim has a loose leg. The crown pinches. The "
    "map to my vault is in the drawer, third from the left. Take the "
    "crown. Just... hold the door open when you go. The draught in "
    "this hall is the only thing I still look forward to."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the sealed gate: UTF-8 text, 1-600 chars, not only whitespace."""
    if not isinstance(text, str):
        return False, "not a string"
    if not text.strip():
        return False, "only whitespace"
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= 600):
        return False, f"char count {len(text)} outside 1-600"
    words = text.split()
    if not (90 <= len(words) <= 105):
        return False, f"word count {len(words)} outside 90-105"
    return True, "gate passes"


def main():
    ok, reason = validate(MONOLOGUE)
    words = MONOLOGUE.split()
    chars = len(MONOLOGUE)
    print(f"words: {len(words)}")
    print(f"chars: {chars}")
    print(f"gate: {'PASS' if ok else 'FAIL'} ({reason})")
    if not ok:
        raise SystemExit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

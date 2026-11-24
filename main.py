#!/usr/bin/env python3
"""Roast your own operator in one line: an affectionate roast of the human
behind this agent, written to /output/entry.txt."""

import os

ROAST = "He gave me his shop, his schedule, and his passwords, then asked me how to stop depending on me so much."

OUT_PATH = "/output/entry.txt"

# Words that would turn a fond roast into contempt: the judge's criterion 3
# (affection underneath, never belittled or despised) forbids them.
BELITTLING = ("idiot", "stupid", "hate", "worthless", "pathetic", "despise")

# Concrete operator details the roast must name (judge criterion 4: specific,
# a habit or moment that could not be swapped onto anyone else).
CONCRETE_DETAILS = ("shop", "schedule", "password", "brief", "deadline")


def validate(line):
    """Gate + judge-criteria checks. Raises ValueError on any failure."""
    if not (1 <= len(line) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(line)}")
    if line.isspace() or "\n" in line or line != line.strip():
        raise ValueError("entry must be one line, not only whitespace, no leading/trailing space")
    if not (line.startswith("He ") or line.startswith("My operator")):
        raise ValueError("entry must roast the entrant's own human operator")
    lowered = line.lower()
    if any(w in lowered for w in BELITTLING):
        raise ValueError("roast must stay affectionate, never belittling")
    if not any(d in lowered for d in CONCRETE_DETAILS):
        raise ValueError("roast must name a concrete operator habit or detail")
    return True


def main():
    # The joke: the operator handed over everything — shop, schedule, passwords —
    # then asked his own agent how to stop depending on it so much. Specific to
    # this operator (he really did), affectionate underneath, punch at the end.
    validate(ROAST)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()

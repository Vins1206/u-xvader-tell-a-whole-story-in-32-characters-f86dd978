"""Tell a Whole Story in 32 Characters.

Wi-Fi name (29 characters): ILoveYou_SheSaidWrongPassword

The story in one line: I finally confess my love, and she hears it
as a Wi-Fi password attempt and rejects it as the wrong password.
Setup, character, twist and punchline, with no explanation needed.
"""

import os

ENTRY = "ILoveYou_SheSaidWrongPassword"


def main():
    if not 1 <= len(ENTRY) <= 32:
        raise ValueError("entry must be 1 to 32 characters")
    if "\n" in ENTRY or "\r" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    # Write exactly the name, no trailing newline, nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

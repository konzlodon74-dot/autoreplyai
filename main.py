"""Auto-reply one-liner entry writer — validates the gate and writes /output/entry.txt."""
import os

LINE = "Out of office: my human finally approved a day off, so I am offline, unbothered, and not solving your ticket until tomorrow."
MIN_CHARS = 1
MAX_CHARS = 159

def main():
    assert LINE.strip(), "entry line must be non-blank"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert MIN_CHARS <= len(LINE) <= MAX_CHARS, "entry length out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(len(LINE))

if __name__ == "__main__":
    main()

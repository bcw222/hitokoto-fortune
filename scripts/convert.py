#!/usr/bin/env python3
import json
import sys
import os
from pathlib import Path

CATEGORIES = {
    "a": "动画",
    "b": "漫画",
    "c": "游戏",
    "d": "文学",
    "e": "原创",
    "f": "网络",
    "g": "其他",
    "h": "影视",
    "i": "诗词",
    "j": "网易云",
    "k": "哲学",
    "l": "搞笑",
}

YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"


def colorize_book_titles(text):
    """Colorize 《》 with green, matching fortune-zh convention."""
    result = []
    i = 0
    while i < len(text):
        if text[i] == "《":
            result.append(f"{GREEN}《")
        elif text[i] == "》":
            result.append(f"》{RESET}")
        else:
            result.append(text[i])
        i += 1
    return "".join(result)


def convert_json_to_fortune(json_path, fortune_path):
    with open(json_path, "r", encoding="utf-8") as f:
        sentences = json.load(f)

    lines = []
    for item in sentences:
        text = item.get("hitokoto", "").strip()
        source = item.get("from", "").strip()
        if not text:
            continue
        lines.append(colorize_book_titles(text))
        if source:
            lines.append(f"\t\t{YELLOW}-- {source}{RESET}")
        lines.append("%")

    if lines:
        lines[-1] = ""

    with open(fortune_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len([l for l in lines if l == "%"])

def main():
    sentences_dir = sys.argv[1]
    output_dir = sys.argv[2]

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    all_fortune_path = os.path.join(output_dir, "hitokoto")
    all_lines = []
    total = 0

    for key, name in sorted(CATEGORIES.items()):
        json_file = os.path.join(sentences_dir, f"{key}.json")
        if not os.path.exists(json_file):
            print(f"Skipping {key} ({name}): file not found", file=sys.stderr)
            continue

        with open(json_file, "r", encoding="utf-8") as f:
            sentences = json.load(f)

        category_path = os.path.join(output_dir, f"hitokoto-{key}")
        lines = []
        for item in sentences:
            text = item.get("hitokoto", "").strip()
            source = item.get("from", "").strip()
            if not text:
                continue
            lines.append(colorize_book_titles(text))
            if source:
                lines.append(f"\t\t{YELLOW}-- {source}{RESET}")
            lines.append("%")
            all_lines.append(colorize_book_titles(text))
            if source:
                all_lines.append(f"\t\t{YELLOW}-- {source}{RESET}")
            all_lines.append("%")

        if lines:
            lines[-1] = ""
            with open(category_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            count = len([l for l in lines if l == "%"])
            print(f"  hitokoto-{key} ({name}): {count} sentences")
            total += count

    if all_lines:
        all_lines[-1] = ""
        with open(all_fortune_path, "w", encoding="utf-8") as f:
            f.write("\n".join(all_lines))

    print(f"Total: {total} sentences across all categories")
    return total

if __name__ == "__main__":
    main()

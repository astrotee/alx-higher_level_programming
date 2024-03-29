#!/usr/bin/python3
"""7. Load, add, save"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        l: list = load_from_json_file("add_item.json")
    except Exception:
        l: list = list()
    l.extend(sys.argv[1:])
    save_to_json_file(l, "add_item.json")

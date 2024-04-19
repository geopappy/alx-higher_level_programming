#!/usr/bin/python3

import sys
from os import path

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
"""
try :
    items = load('add_item.json')
except Exception:
    items = []
items.extend(sys.argv[1:])
save(items, 'add_item.json')"""

filename = "add_item.json"

if not path.exists(filename):
    save([], filename)
items = load(filename)
items.extend(sys.argv[1:])
save(items, filename)

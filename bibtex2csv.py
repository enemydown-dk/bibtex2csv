#!/usr/bin/env python3

"""
Python script that converts BibTeX
entries to CSV.
Input is via standard input.
Output is via standard output.
"""

from re import match
from re import search
from re import findall
from sys import stdin

entries = []
entry = {}

for line in stdin:
    if match('^@', line.strip()):
        if entry != {}:
            entries.append(entry)
            entry = {}
    elif match('url', line.strip()):
        #value, = findall('\{(\S+)\}', line)
        value, = findall("\\s+", line)
        entry["url"] = value
    elif search('=', line.strip()):
        key, value = [v.strip(" {},\n") for v in line.split("=", 1)]
        entry[key] = value

for entry in entries:
    doi = entry["DOI"]
    title = entry["Title"]
    oa = entry["OA"]
    print("{}\t{}\t{}".format(doi, title, oa))

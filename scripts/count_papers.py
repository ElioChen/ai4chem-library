#!/usr/bin/env python3
"""Recount the literature archive so README numbers can be checked.

Counts entries that carry a URL (verifiable), the number claimed in each
monthly header, the entries in papers/index.json, and how they overlap.
Run from the repository root:  python3 scripts/count_papers.py
"""
import glob, json, re

link = re.compile(r'^### \[(.+?)\]\((.+?)\)\s*$', re.M)
claimed = re.compile(r'共收录\s*\*\*(\d+)\s*篇')
urls, claim_total, per_month = set(), 0, {}
for f in sorted(glob.glob('papers/20*.md')):
    s = open(f, encoding='utf-8').read()
    ents = link.findall(s)
    c = claimed.search(s)
    per_month[f[7:-3]] = (len(ents), int(c.group(1)) if c else None)
    claim_total += int(c.group(1)) if c else 0
    urls |= {u for _, u in ents}

idx = json.load(open('papers/index.json', encoding='utf-8'))['papers']
idx_urls = {p['url'] for p in idx}
print(f"{'month':8} {'with URL':>8} {'header claims':>13}")
for m, (n, c) in per_month.items():
    print(f"{m:8} {n:8d} {c if c is not None else '-':>13}")
print(f"\nentries with a URL in monthly files : {len(urls)}")
print(f"sum of numbers claimed in headers   : {claim_total}")
print(f"entries in papers/index.json        : {len(idx)}")
print(f"  of which URL also in monthly files: {len(idx_urls & urls)}")
print(f"  only in index.json                : {len(idx_urls - urls)}")
print(f"monthly-file URLs missing from index: {len(urls - idx_urls)}")
generic = sum(p.get('authors', '') in ('Multiple authors', '') for p in idx)
print(f"index entries with placeholder authors ('Multiple authors'/empty): {generic}")

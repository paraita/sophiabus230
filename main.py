#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re
from bs4 import BeautifulSoup

def _translate_to_eng(french_str):
    translated = french_str.replace(u'à', 'at')
    translated = translated.replace(u'é', 'e')
    translated = translated.replace('dans', 'in')
    translated = translated.replace('direction', 'towards')
    return translated

def get_next_buses():
    content = ""
    OFFLINE = False
    if OFFLINE:
        f_path = "/home/paraita/Bureau/SP/BusConnect06/response_cg06.html"
        with open(f_path, "r") as fd:
            content = fd.read()
    else:
        stop_id = 1939
        cg06_url = "http://cg06.tsi.cityway.fr/qrcode/?id={0}"
        req = urllib.urlopen(cg06_url.format(stop_id))
        content = req.read()
    soup = BeautifulSoup(content, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with('\n')
    data = soup.find_all("div", attrs={"class": "data"})
    tt = []
    for e in data[0].div.get_text().split('\n'):
        sane_line = re.sub(r"^\s+$", '\n', e)
        sane_line = _translate_to_eng(sane_line)
        if len(sane_line) > 1:
            tt.append(sane_line)
    return tt

for t in get_next_buses():
    print t




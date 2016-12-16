#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re
from bs4 import BeautifulSoup


def _translate_to_eng(french_str):
    """
    Utilitary to replace words from a french sentence with english words.
    Replaces the following:
    - `a` to `at`
    - `dans` to `in`
    - `direction` to `towards`

    :param french_str: the french sentence to translate
    :return: the translated sentence
    """
    translated = french_str.replace(u'à', 'at')
    translated = translated.replace(u'é', 'e')
    translated = translated.replace('dans', 'in')
    translated = translated.replace('direction', 'towards')
    return translated


def _get_html_from_cg06(stop_id):
    """
    Requests the timetable from the cg06 website

    :param stop_id: the stop to fetch the timetable for
    :return: The result of the request as a html content
    :rtype: str
    """
    cg06_url = "http://cg06.tsi.cityway.fr/qrcode/?id={0}"
    req = urllib.urlopen(cg06_url.format(stop_id))
    content = req.read()
    return content


def get_next_buses():
    """
    Fetches the list of upcoming buses at the INRIA bus stop for the bus 230 towards Nice

    :return: upcoming buses
    :rtype: list
    """
    content = _get_html_from_cg06(1939)
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




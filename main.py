import urllib
import re
from bs4 import BeautifulSoup

OFFLINE = True

content = ""
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

data = soup.findAll("div", attrs={"class": "data"})

for e in data[0].div.get_text().split('\n'):
    sane_line = re.sub(r"^\s+$", '\n', e)
    if len(sane_line) > 0:
        print u'line: {0}'.format(e)




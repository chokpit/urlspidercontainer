#!/usr/bin/python
import bs4 as bs
import urllib.request
import sys
from importlib import reload
print(sys.getdefaultencoding())
#sys.setdefaultencoding("utf-8")

print(sys.argv[0:])
sauce = urllib.request.urlopen(sys.argv[1]).read()

soup = bs.BeautifulSoup(sauce,'lxml')

print(soup)
#!/usr/bin/python
import bs4 as bs
import urllib.request
import sys

sauce = urllib.request.urlopen(sys.argv[1]).read()

soup = bs.BeautifulSoup(sauce,'lxml')

print(soup)
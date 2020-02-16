import bs4 as bs
import urllib.request
import sys

print(sys.argv[1])
source = urllib.request.urlopen(sys.argv[1]).read()

soup = bs.BeautifulSoup(source,'lxml')

print(source)
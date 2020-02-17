import bs4 as bs
import urllib.request
import sys

print(sys.argv[1])
source = urllib.request.urlopen(sys.argv[1]).read()

soup = bs.BeautifulSoup(source,'lxml')

for url in soup.find_all('a'):
    print(url.get('href'))
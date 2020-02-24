import bs4 as bs
import urllib.request
import sys
import importlib


print(importlib.resources.read_text(__package__, 'temp_urls.txt'))
#fr = open(os.path.abspath('temp', 'temp_urls.txt'))
#fh = open('/mnt/bs-scripts/temp/temp_urls.txt','a+')
#for line in fr:
    #print(line)
    #source = urllib.request.urlopen(line).read()
    #soup = bs.BeautifulSoup(source,'lxml')
    #for url in soup.find_all('a'):
    #fh.write("\n {}".format(url.get('href')))
    # f.close()
import bs4 as bs
import urllib.request
import sys


# f = open ('/mnt/bs-scripts/temp/temp_urls.txt','a+')

# source = urllib.request.urlopen(sys.argv[1]).read()
# soup = bs.BeautifulSoup(source,'lxml')

# for url in soup.find_all('a'):
#     f.write("\n {}".format(url.get('href')))
# f.close()



##############

fileRead = open ('/mnt/bs-scripts/temp/temp_urls.txt','r')

    for i
    source = urllib.request.urlopen(sys.argv[1]).read()
    soup = bs.BeautifulSoup(source,'lxml')

    for url in soup.find_all('a'):
        f.write("\n {}".format(url.get('href')))
    f.close()

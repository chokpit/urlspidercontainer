import bs4 as bs
import urllib.request
#import os
#print os.getenv('URL_VAR')

sauce = urllib.request.urlopen('https://www.ynet.co.il').read()

soup = bs.BeautifulSoup(sauce,'lxml')

print(soup)
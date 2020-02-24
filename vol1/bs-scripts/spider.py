#import bs4 as bs
#import urllib.request
#import sys
#import importlib
import os

script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
rel_path = "temp/temp_urls.txt"
abs_file_path = os.path.join(script_dir, rel_path)

print(abs_file_path)

with open(abs_file_path) as fr:
    for line in fr:
        print(line)
        with open(abs_file_path, 'a+') as fh
            source = urllib.request.urlopen(line).read()
            soup = bs.BeautifulSoup(source,'lxml')
            for url in soup.find_all('a'):
            fh.write("\n {}".format(url.get('href')))
            f.close()
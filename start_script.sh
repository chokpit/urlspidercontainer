#!/bin/bash
source /project_env/bin/activate
pip3 install lxml beautifulsoup4
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 #fixing locale variable encoding

sh ./mnt/passvar.sh


/bin/bash
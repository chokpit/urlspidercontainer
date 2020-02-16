#!/bin/bash

echo this variable will pass from bash to python $URL_VAR
echo $URL_VAR
python3 bs.py $URL_VAR

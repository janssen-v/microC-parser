#! /bin/sh

./scanner $1 > scanned.txt
python3 parser_1.py scanned.txt
python3 parser_1.py scanned.txt > parsed.txt
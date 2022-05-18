#!/bin/bash
 
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for i in $files ; do
 if test -e "..$i"; then echo "$i" > oldFiles.txt;
 fi
done

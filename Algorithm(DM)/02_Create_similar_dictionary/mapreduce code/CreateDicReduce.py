#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
all_find_words_dic={}

for line in sys.stdin:
    if line:
       if len(line.strip().split('\t'))==2:
           key= line.strip().split('\t')[0]
           value= line.strip().split('\t')[1]
           if key not in all_find_words_dic:
              all_find_words_dic[key]={}
              all_find_words_dic[key][value]={}
           else:
              all_find_words_dic[key][value]={}

for dic in all_find_words_dic:
    valueall=''
    for value in all_find_words_dic[dic].keys():
        valueall += '|'+value
    print dic+valueall

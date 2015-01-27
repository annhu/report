#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Trista'
import sys
import re
find_words_dic={}
skip_word=['?','.','*','$','+','[',']','{','}','|',"\\","^"]

f4=open('dic_all.txt', 'r')
word=[]
for line in f4.readlines():
    li=line.strip().decode('utf8')
    word[len(word):]=[li]	 	#word是字庫的list
f4.close()

for line in sys.stdin:
     a=""
     for i in list(line.strip().lower().decode('utf8')):
         if i.encode('utf8') in skip_word:
            a+="(.*?)"+'\\'+i.encode('utf8') 
         else:
            a+="(.*?)"+i.encode('utf8')
     a+="(.*?)"
     for line2 in word:
          try:
             m=re.match(a, line2.lower().encode('utf8'))
             if m is not None:
                ##find_words_dic[line2]=line.strip()      
                print line2.encode('utf8')+'\t'+line.strip()
          except:
             pass


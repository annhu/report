# -*- coding:utf8 -*-
import fileinput
from glob import glob
import re
import os
import string

exclude =set(string.punctuation)
cuts=r'\s+'
dic_search={}
dic_find={}

dic_txt = open("dic_dir_all.txt", 'r')
# -------create dic{}
for lined in dic_txt.readlines():
    #print lined
    dic_word=lined.strip().split('|')[0]
    dic_search[dic_word]={}
    dic_find[dic_word]=0
    a= list(lined.strip().split('|'))
    i=0
    while i < len(a):
        dic_words = lined.strip().split('|')[i]
        i+=1
        dic_search[dic_word][dic_words]=0
        #print dic_words
dic_txt.close()
print "dic done"
        
# -------search dic{} in data
for dirPath, dirNames, fileNames in os.walk("E:/report/python/report/count/data"):
    filenum=0
    for f in fileNames:
        files = os.path.join(dirPath, f)
        f1=open(files, 'r')  # open datafile individual
        filenum+=1
        if (filenum % 100) == 0:
            print filenum
        text=""
        for lineb in f1.readlines():
            string_1 = lineb.strip()
            string_2 = re.sub(cuts, '', string_1)  #去掉空白
            string_3 = "".join(ch for ch in string_2 if ch not in exclude)  #去掉半形符號
            string = re.sub('臺南', '台南', string_3)  #改成簡寫台
            text+=string  # hole datafile text
        #print text
        for dic in dic_search:
            for value in dic_search[dic].keys():
                value_1=re.sub(cuts, '', value)  #去掉空白
                value_2 = "".join(ch for ch in value_1 if ch not in exclude)  #去掉半形符號
                value_3 = re.sub('臺南', '台南', value_2)  #改成簡寫台
                m=re.search(value_3.lower(), text.lower())  # search
                if m is not None:
                    dic_find[dic]+=1  # in same dic_word, dic_find just +1
                    break  # once dic_word match, break
print "done"



# -------writeout
count_txt = open("count_2.txt", 'w')
for w in sorted(dic_find, key=dic_find.get, reverse=True):  # sort by value(count) 
    finaltext = w+" : "+str(dic_find[w])
    #print finaltext
    count_txt.write(finaltext+"\n")
    
    
print "final"
count_txt.close()
f1.close()

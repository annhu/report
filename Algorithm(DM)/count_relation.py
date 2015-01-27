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
dic_relation={}

dic_txt = open("dic_dir_all.txt", 'r')  # dic路徑
# -------create dic{}
for lined in dic_txt.readlines():
    #print lined
    dic_word=lined.strip().split('|')[0]
    dic_search[dic_word]={}
    dic_find[dic_word]=0
    dic_relation[dic_word]={}
    a= list(lined.strip().split('|'))
    i=0
    while i < len(a):
        dic_words = lined.strip().split('|')[i]
        i+=1
        dic_search[dic_word][dic_words]=0
        #print dic_words

        
# -------search dic{} in data and count relationship
for dirPath, dirNames, fileNames in os.walk("C:/Users/BigData/python/report/count/data"):  # 所有data檔路徑(資料夾)
    for f in fileNames:
        files = os.path.join(dirPath, f)
        f1=open(files, 'r')  # open datafile individual
        print files
        text=""
        relation=[]
        for lineb in f1.readlines():
            string_1 = lineb.strip()
            string_2 = re.sub(cuts, '', string_1)  #去掉空白
            string_3 = "".join(ch for ch in string_2 if ch not in exclude)  #去掉半形符號
            string = re.sub('臺南', '台南', string_3)  #改成簡寫台
            text+=string  # hole datafile text
        # ----- search dic in data
        for dic in dic_search:
            for value in dic_search[dic].keys():
                value_1=re.sub(cuts, '', value)  #去掉空白
                value_2 = "".join(ch for ch in value_1 if ch not in exclude)  #去掉半形符號
                value_3 = re.sub('臺南', '台南', value_2)  #改成簡寫台
                m=re.search(value_3.lower(), text.lower())  # search
                if m is not None:
                    dic_find[dic]+=1  # in same dic_word, dic_find just +1
                    relation[len(relation):]=[dic]  # 在同一篇文章中所有的dic放在同list
                    break  # once dic_word match, break
		# ----- count relationship
        for x in range(0, len(relation)):
            #print relation[x]
            for y in range(0, len(relation)):
                if x != y:
                    if relation[y] not in dic_relation[relation[x]]:
                        dic_relation[relation[x]][relation[y]]=0
                        dic_relation[relation[x]][relation[y]]+=1
                    else:
                        dic_relation[relation[x]][relation[y]]+=1    

print "done"

# -------writeout word count with sort by value(count)
count_txt = open("count.txt", 'w')
for w in sorted(dic_find, key=dic_find.get, reverse=True):  # sort by value(count) 
    finaltext = w+" : "+str(dic_find[w])
    #print finaltext
    count_txt.write(finaltext+"\n")

# ------- writeout relationship
relation_txt=open("relation.txt", 'w')
for dic1 in dic_relation:
    for dic2 in dic_relation[dic1].keys():
        relation = dic1+" : "+dic2+" = "+str(dic_relation[dic1][dic2])  # dic1 : dic2 = count
        #print relation
        relation_txt.write(relation+"\n")    

    
print "final"
relation_txt.close()
count_txt.close()
f1.close()
dic_txt.close()
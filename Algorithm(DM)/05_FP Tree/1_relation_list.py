# -*- coding:utf8 -*-
import re
import os
import string

exclude=set(string.punctuation)
cuts=r'\s'
dic_search={}
dic_find={}
dic_relation={}


dic_txt = open("dic_dir_all_relation.txt", 'r')  # dic路徑
# -------create dic{}
for lined in dic_txt.readlines():
    #print lined
    dic_word=lined.strip().split('|')[0]
    dic_search[dic_word]={}
    dic_relation[dic_word]={}
    a= list(lined.strip().split('|'))
    i=0
    while i < len(a):
        dic_words = lined.strip().split('|')[i]
        i+=1
        dic_search[dic_word][dic_words]=0
dic_txt.close()


# -------search dic{} in data and count relationship
relation_txt=open("relation_3.csv", 'w')
for dirPath, dirNames, fileNames in os.walk("E:/report/python/report/count/data"):  # 所有data檔路徑(資料夾)
    filenum=0
    for f in fileNames:
        files = os.path.join(dirPath, f)
        f1=open(files, 'r')  # open datafile individual
        filenum+=1
        if (filenum % 100) == 0:
            print filenum
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
                    relation[len(relation):]=[dic]  # 在同一篇文章中所有的dic放在同list
                    break  # once dic_word match, break
                    
        linesss=""
        x=0
        for te in relation:
            if len(relation) > 1:
                linesss+=te
                if x in range(0, len(relation)-1):
                    linesss+=","
                    x+=1
        if linesss != "":
            #print linesss
            relation_txt.write(linesss+"\n")
                      
print "done"


print "final"
relation_txt.close()
f1.close()

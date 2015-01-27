﻿##compare gram data and dictionary to create another dictionary
# -*- coding: utf-8 -*-
__author__ = 'Trista'
import re
import time
#====================================
f4=open('C:\\Users\\BigData\\100_project\\createdic\\tainan_dic\\dic_all.txt', 'r')
word=[]
for line in f4.readlines():
    li=line.strip().decode('utf8')
    word[len(word):]=[li]	 	#word是字庫的list
f4.close()
find_words_dic={}
#=====================================

skip_word=['?','.','*','$','+','[',']','{','}','|',"\\","^"]

tstart = time.time()
##compare data in tainan_culture
f3=open('C:\\Users\\BigData\\100_project\\createdic\\create_dic_final_code\\gram_data_test.txt', 'r')  #gramdata
for line1 in f3.readlines():
    a=""
    for i in list(line1.strip().lower().decode('utf8')):
        if i.encode('utf8') in skip_word:
            a+="(.*?)"+'\\'+i.encode('utf8') 
        else:
            a+="(.*?)"+i.encode('utf8')
        a+="(.*?)"
    for line2 in word:
        try:
            m=re.match(a,line2.lower().encode('utf8'))
            if m is not None: ##有比對到dictionary
                if line2.strip() not in find_words_dic: ##之前沒有這筆資料
                    find_words_dic[line2]={}
                    find_words_dic[line2][line1.strip()]={}
                else:                                   ##之前已有這筆資料補gram data的資料進去
                    find_words_dic[line2][line1.strip()]={}
        except:
            print 'error'
            print a
    f4.close()
    
f3.close()
print "done"
    

finalfile =open('C:\\Users\\BigData\\100_project\\createdic\\create_dic_final_code\\create_dic_final_revise.txt','w')
for dic in find_words_dic:
    finalfile.write(dic.encode('utf8'))
    for value in find_words_dic[dic].keys():
        finalfile.write('|'+value)
    finalfile.write('\n')
finalfile.close()
print 'totaldone'
tend = time.time()
print tend-tstart
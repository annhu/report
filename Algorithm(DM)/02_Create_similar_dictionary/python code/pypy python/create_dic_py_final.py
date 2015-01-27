# -*- coding: UTF-8 -*-
##compare gram data and dictionary to create another dictionary
##convert data in lower
__author__ = 'Trista'
import re,uniout
import glob
import time
find_words_dic={}

skip_word=['?','.','*','$','+','[',']','{','}','|',"\\","^"]

tstart = time.time()

##compare data in Food_dic_no
f3=open('C:\\Users\\BigData\\100_project\\createdic\\create_dic_final_code\\gram_data_test.txt', 'r')  #gramdata
for line1 in f3.readlines():
    a=list(line1.strip().lower().decode('utf8'))    #轉成小寫
    f4=open('C:\\Users\\BigData\\100_project\\createdic\\tainan_dic\\dic_all.txt', 'r')  #dic
    for line2 in f4.readlines():
        linest=line2.strip().lower().decode('utf8')  #轉成小寫
        dd=0
        for i in a:
            if linest.find(i)!=-1: 
                linest=linest[linest.find(i)+1:]
                dd=dd+1
            if dd==len(a):
                if line2.strip() not in find_words_dic: ##之前沒有這筆資料
                   find_words_dic[line2.strip()]={}
                   find_words_dic[line2.strip()][line1.strip()]={}
                else:    ##之前已有這筆資料補gram data的資料進去
                   find_words_dic[line2.strip()][line1.strip()]={}
print "done"    
f3.close()

finalfile =open('C:\\Users\\BigData\\100_project\\createdic\\create_dic_final_code\\create_dic_py_final.txt','w')
for dic in find_words_dic:
    finalfile.write(dic)
    for value in find_words_dic[dic].keys():
        finalfile.write('|'+value)
    finalfile.write('\n')
finalfile.close()
print 'totaldone'
tend = time.time()
print tend-tstart

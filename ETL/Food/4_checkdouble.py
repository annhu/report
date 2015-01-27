# -*- coding:utf-8 -*-
import re
import codecs #coding=utf-8

f = codecs.open("com.txt", 'r', "utf-8")
h = codecs.open("com_1.txt", 'r', "utf-8")
lines_1 = f.readlines()
lines_2 = h.readlines()
count = 0
while count <= 7344:
    for li_1 in lines_1[count:count+1]:
        string_1 = li_1.strip()
        name_1 = string_1.split('|')[0]
        #print name_1
        #print string_1
        test = name_1[0:2]
        #print test

        
        for li_2 in lines_2[count+1:]:
            string_2 = li_2.strip()
            name_2 = string_2.split('|')[0]
            #print string_2
            try:
                m = re.search(test, string_2)
                #print m
                if m is not None:
                    print name_1
            except:
                print name_1
        
        
    count += 1
    
h.close()    
f.close()
print " "
print "done"
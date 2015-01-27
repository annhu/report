# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import glob

count = 4836  ##行數減一
r = open("link_need.txt", 'r')
lines = r.readlines()
l_line = lines[4836:7001]  ##行數減一  ####可設定從第幾行開始讀  [2:]-->從第三行開始
for line in l_line:
    link = line.strip()
    count += 1
    print count
    #print link
    test = "C:/Users/BigData/python/report/blog_xuite/"+str(count-1)+"*.txt"
    if len(glob.glob(test)) == 0 :
        #print str(count-1)+"not here"
        t = open("relink.txt", 'a')
        #print count-1
        #print "cut"
        relink = lines[count-2:count-1][0].strip()
        t.write(relink+"\n")
        #print relink
        #print style_format+page_format%(page-1)
    author_1 = link.split('/')[3:-1]
    author = ""
    for au in author_1:
        #print au
        author += au
    #print author
    try:
        res_link = requests.get(link)
        response_link = res_link.text.encode('utf8')
        soup_link = BeautifulSoup(response_link)
        #print soup_page
        blog_title_date = soup_link.select('.title')
        #print blog_title_date
        blog_content = soup_link.findAll('div', {'id':'content_all'})
        for ti in blog_title_date:
            title = ti.find('span', {'class':'titlename'}).text.encode('utf8')
            #print title
            date_y = ti.find('span', {'class':'titledate-year'}).text.encode('utf8')
            #print date_y
            date_m = ti.find('span', {'class':'titledate-month'}).text.encode('utf8')
            #print date_m
            date_d = ti.find('span', {'class':'titledate-day'}).text.encode('utf8')
            #print date_d
            date_h = ti.find('span', {'class':'titledate-hour'}).text.encode('utf8')
            #print date_h
            date_M = ti.find('span', {'class':'titledate-min'}).text.encode('utf8')
            #print date_M
            date = date_y+"/"+date_m+"/"+date_d+" "+date_h+":"+date_M
            #print date
            id_date = date_y+date_m+date_d+date_h+date_M
            #print id_date
            id_name = str(count)+"_xuite_"+author+"_"+id_date+".txt"
            print id_name
            n = open(id_name, 'w')
            n.write(title+"\n")
            n.write(date+"\n")
            n.write(link+"\n")
        for co in blog_content:
            content_1 = co.findAll('p')
            for co_1 in content_1:
                content = co_1.text.encode('utf8')
                #print content
                n.write(content+"\n")
    
    except:    
        print "skip"

        
n.close()
r.close()
print "done"
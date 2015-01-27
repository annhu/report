# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

count = 0
f = open("link.txt", 'r')
w = open("Food_dic_boylondon.txt", 'a')
lines = f.readlines()
for li in lines:
    res_page = requests.get(li)
    res_page.encoding='utf-8'
    response_page = res_page.text
    soup_page = BeautifulSoup(response_page)
    #print soup_page
    blog_title = soup_page.findAll('li', {'class':'title'})  #要找標題
    try:
        for ti in blog_title:
            title_1 = ti.find('a').text.encode('utf8').split('‧')[1]
            title = ti.find('a').text.encode('utf8').split('區 ')[1]
            #print title
            w.write(title+"\n")

    except:
        w.write(title_1+"\n")
        print "ok"
    
w.close()
f.close()
print "done"
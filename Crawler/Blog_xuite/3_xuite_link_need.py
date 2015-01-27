# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

count = 15067  #行數減一
r = open("link_s.txt", 'r')
lines = r.readlines()
l_line = lines[15067:]   ##行數減一 ####可設定從第幾行開始讀  [2:]-->從第三行開始  
###############2166開始
for line in l_line:
    link = line.strip()
    count += 1
    print count
    #print link
    res_link = requests.get(link)
    response_link = res_link.text.encode('utf8')
    soup_link = BeautifulSoup(response_link)
    #print soup_page
    blog_link = soup_link.findAll('li', {'class':'element-more-article-item'})
    for li in blog_link:
        link_need = [tag['href'] for tag in li.findAll('a', {'class':'element-more-article-link'})][0]
        #print link_need
        f = open("link_need.txt", 'a')
        f.write(link_need+"\n")
    
        
f.close()
print "done"
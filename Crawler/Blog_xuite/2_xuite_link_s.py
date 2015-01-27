# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

count = 1501  #頁數減一
r = open("link_m.txt", 'r')
lines = r.readlines()
l_line = lines[1501:]  #頁數減一
for line in l_line:
    link = line.strip()
    count += 1
    print count
    print link
    res_page = requests.get(link)
    response_page = res_page.text.encode('utf8')
    soup_page = BeautifulSoup(response_page)
    #print soup_page
    blog_title = soup_page.findAll('article', {'id':'element-info'})  #要找每篇母網誌的標題
    blog_author = soup_page.findAll('li', {'id':'element-owner'})  #要找每篇母網誌的作者
    blog_date = soup_page.findAll('li', {'id':'element-data-update-date'})  #要找每篇母網誌的日期時間
    blog_content = soup_page.findAll('div', {'id':'element-describe-content'})  #要找每篇母網誌的內容
    #print blog_content
    blog_link = soup_page.findAll('article', {'id':'element-article-main'})  #要找每篇子網誌的連結
    #print blog_link
    for ti in blog_title:
        title = ti.find('h1', {'id':'element-info-title'}).text.encode('utf8')  #每篇母網誌的標題
        #print title
    for au in blog_author:
        author = [tag['href'] for tag in au.findAll('a' ,{'href':True})][0].split('/')[1]  #每篇母網誌的作者
        #print author
    for da in blog_date:
        date_1 = da.find('time', {'class':'element-data-update-date-detail'}).text.encode('utf8')
        #print date_m_1
        date_ymd = date_1.split(' ')[0].replace('/','')  #每篇母網誌的日期
        #print date_ymd_m
        date_h = date_1.split(' ')[1].split(':')[0]  #每篇母網誌的時
        #print date_h_m
        date_m = date_1.split(' ')[1].split(':')[1]  #每篇母網誌的分
        #print date_m_m
        date = date_1.split(' ')[0]+" "+date_h+":"+date_m  #每篇母網誌的日期時間
        #print date
        id_date = date_ymd+date_h+date_m
        #print id_date
        id_name = "xuite_"+author+"_"+id_date+".txt"
        print id_name
        f = open(id_name, 'w')
        f.write(title+"\n")
        f.write(date+"\n")
        f.write(link+"\n")
    for co in blog_content:
        content_1 = co.findAll('p')
        for co_1 in content_1:
            content = co_1.text.encode('utf8')
            #print content
            f.write(content+"\n")
            
            
    for li in blog_link:
        link_1 = [tag['href'] for tag in li.select('#element-article-more')][0]
        #print link_1
        link = "http://yo.xuite.net/info/"+link_1
        #print link
        style_format = link
        page_format = "&p=%d"
        for page in range(1, 11):
            res_page_s = requests.get(style_format+page_format%(page))
            #print style_format_s+page_format_s%(page_s)
            #res_page.encoding='utf-8'
            if res_page_s is not None: 
                link_s = style_format+page_format%(page)
                #print link_s
                s = open("link_s.txt", 'a')
                s.write(link_s+"\n")
                
        print "cut"

        
s.close()            
f.close()
r.close()
print "done"
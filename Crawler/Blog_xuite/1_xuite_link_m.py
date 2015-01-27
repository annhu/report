# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


print "標題|日期|網址連結|id"
count = 7740
style_format = "http://yo.xuite.net/info/search.php?keyword=%E5%8F%B0%E5%8D%97&search_type=s_yo&"
page_format = "p=%d"
for page in range(7741, 2500000):
    res_page_m = requests.get(style_format+page_format%(page))
    #res_page.encoding='utf-8'
    if res_page_m is not None:  #當有這個page時
        count += 1
        print count
        response_page_m = res_page_m.text#.encode('utf-8')
        soup_page_m = BeautifulSoup(response_page_m)
        #print soup_page
        blog_title_link_m = soup_page_m.findAll('li', {'class':'componet-element-item'})  #要找每篇母網誌的標題和連結
        for ti_m in blog_title_link_m:
            link_m_1 = [tag['href'] for tag in ti_m.findAll('a', {'class':'componet-element-title'})][0]
            link_m = "http://yo.xuite.net"+link_m_1  #每篇母網誌的連結
            #print link_m
            f = open("link_m.txt", 'a')
            f.write(link_m+"\n")
            f.close()
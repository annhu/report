# -*- coding:utf-8 -*-
## ----- crawler pixnet links of every page -----
import requests
from bs4 import BeautifulSoup

f = open("link.txt", 'a')  ## open links file
count = 517
style_format = "https://www.pixnet.net/searcharticle?q=%E5%8F%B0%E5%8D%97&type=related&period=all&"  ## link format
page_format = "page=%d"  ## link page
for page in range(518, 1000):
    count += 1
    print count  ## print page number
    res_page = requests.get(style_format+page_format%(page))
    res_page.encoding='utf-8'
    if res_page is not None:  ## when page is exist
        response_page = res_page.text#.encode('utf-8')
        soup_page = BeautifulSoup(response_page)
        blog_link = soup_page.findAll('li', {'class':'search-list'})  ## find blog links of every page
        for li in blog_link:
            link = [tag['href'] for tag in li.findAll('a', {'href':True})][0]  ## blog links of every page
            #print link
            f.write(link+"\n")
            
print "done"
f.close()
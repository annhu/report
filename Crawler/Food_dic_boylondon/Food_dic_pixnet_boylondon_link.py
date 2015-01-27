# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

count = 0

res_page = requests.get('http://boylondon.pixnet.net/blog')
res_page.encoding='utf-8'
response_page = res_page.text
soup_page = BeautifulSoup(response_page)
#print page_soup
type_link = soup_page.findAll('ul', {'id':'category-1373531'})  #所有類別連結
for ty in type_link:
    link_1 = ty.findAll('li')
    #print link_1
    for li_1 in link_1[0:8]:  #未包含素食
        link = "http://boylondon.pixnet.net"+[tag['href'] for tag in li_1.findAll('a', {'href':True})][0]
        print link
        res_link = requests.get(link)
        response_link = res_link.text.encode('utf8')
        soup_link = BeautifulSoup(response_link)
        link_page = soup_link.findAll('div', {'class':'page'})
        #print link_page
        for li_p in link_page:
            #print li_p
            page = [tag['href'] for tag in li_p.findAll('a', {'href':True})]
            #for p in page[:-1]:
                #print p
            

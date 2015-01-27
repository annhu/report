# -*- coding:utf-8 -*-
## ----- crawler facebook link -----
import requests
from bs4 import BeautifulSoup

f = open("testlink_tainanfood1.txt", 'a')  ## open file
link = "https://www.facebook.com/Tainanfood1/photos/a.439473242766458.91209.438944639485985/818880108159101/?type=1"  ## first link
res_page = requests.get(link)
response_page = res_page.text.encode('utf8')
soup_page = BeautifulSoup(response_page)
blog_page = soup_page.findAll('div', {'class':'rfloat _ohf fsm fwn fcg'})  ## find next page
#print blog_link
i = 0
for li_1 in blog_page:
    link_1 = [tag['href'] for tag in li_1.findAll('a', {'href':True})][0]  
    link = "https://www.facebook.com"+link_1  ## next page link
    #print link
    while i <= 100000:  ## for loop
        i += 1
        if i == 1:
            test = link  ## just first link
            #print test
            f.write(test+"\n")
            #print "1"
        else:
            test = link_test
            #print test
            f.write(test+"\n")
            #print "2"
            
        res_link = requests.get(test)
        response_link = res_link.text.encode('utf8')
        soup_link = BeautifulSoup(response_link)
        blog_link = soup_link.findAll('div', {'class':'rfloat _ohf fsm fwn fcg'})  ## find next page
        for li_2 in blog_link:
            link_2 = [tag['href'] for tag in li_2.findAll('a', {'href':True})][0]
            #print link_2
            link_test = "https://www.facebook.com"+link_2  ## next page link

print "done"
f.close()
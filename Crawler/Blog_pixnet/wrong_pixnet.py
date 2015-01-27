# -*- coding:utf-8 -*-
## ----- wrong -----
import requests
from bs4 import BeautifulSoup
import glob
import time

rs = requests.session()  ## set session
count = 499  ## page-1
style_format = "https://www.pixnet.net/searcharticle?q=%E5%8F%B0%E5%8D%97&type=related&period=all&"
page_format = "page=%d"
for page in range(500,2500000):  ## begin with which page
    time.sleep(1)  ## sleep
    res_page = rs.get(style_format+page_format%(page))
    print res_page
    res_page.encoding='utf-8'
    if res_page is not None:  ## when page is exist 
        count += 1
        print count  ## print page number
        test = "C:/Users/BigData/python/report/blog_pixnet_1/"+str(count-1)+"*.txt"  ## prior number file's route
        if len(glob.glob(test)) == 0 :  ## if prior number file is not exist
            #print str(count-1)+"not here"
            t = open("relink.txt", 'a')  ## open relink file
            t.write(style_format+page_format%(page-1)+"\n")
            #print style_format+page_format%(page-1)
        response_page = res_page.text#.encode('utf-8')
        soup_page = BeautifulSoup(response_page)
        #print soup_page
        blog_title = soup_page.findAll('li', {'class':'search-title'})  ## find blog title
        blog_date = soup_page.findAll('div', {'class':'search-meta'})  ## find blog date
        blog_link = soup_page.findAll('li', {'class':'search-list'})  ## find blog link
        for ti in blog_title:
            title = ti.find('a').text.encode('utf8')  ## blog title
            #print title
        for da in blog_date:
            date_1 = da.find('span', {'class':'search-postTime'}).text.encode('utf8')
            date = date_1.replace('-','/')  
            date_time_1 = date_1.split(' ')[1]  
            id_date_time = date_time_1.replace(':','')  ## blog date(hour and minute)
            date_ymd_1 = date_1.split(' ')[0]
            id_date_ymd = date_ymd_1.replace('-','')  ## blog date(year, month, and day)
        for li in blog_link:
            link = [tag['href'] for tag in li.findAll('a', {'href':True})][0]  ## blog link
            #print link
            name_1 = link.split('.')[0]
            id_name = name_1.split('//')[1]  ## blog author
            #print name
            time.sleep(1)
            res_link = requests.get(link)
            res_link.encoding = 'utf8'
            response_link = res_link.text
            soup_link = BeautifulSoup(response_link)
            soup_content = soup_link.findAll('div', {'class':'article-content-inner'}) ## find blog content
            for co in soup_content:
                content = ''.join(co.text.encode('utf8').strip().split(' '))  ## blog content
                id_name = str(count)+"_pixnet_"+id_name+"_"+id_date_ymd+id_date_time+".txt"  ## id
                print id_name
                f = open(id_name, 'w')  ## open content file
                f.write(title+"\n")
                f.write(date+"\n")
                f.write(link+"\n")
                f.write(content)
                
            
            
            
t.close()            
f.close()            
print "done"
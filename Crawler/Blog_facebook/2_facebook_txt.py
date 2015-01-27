# -*- coding:utf-8 -*-
## ----- crawler facebook content -----
import requests
from bs4 import BeautifulSoup

count = 373
f = open("testlink_tainanfood1.txt", 'r')  ## open link file
lines = f.readlines()
for li in lines[373:]:  ## read begin with point line 
    count+=1
    print count  ## print which line
    link = li.strip()
    #print link
    res_page = requests.get(link)
    response_page = res_page.text.encode('utf8')
    soup_page = BeautifulSoup(response_page)
    #print soup_page
    blog_content = soup_page.findAll('span', {'class':'hasCaption'})  ## find blog content
    #print blog_content
    blog_date = soup_page.findAll('a', {'class':'uiLinkSubtle'})  ## find blog date
    try:  ## try-catch
        for da in blog_date:
            date_1 = [tag['title'] for tag in da.findAll('abbr', {'title':True})][0]
            #print date_1
            date_y = date_1.encode('utf8').split('年')[0]  ## find date(year)
            #print date_y
            date_m_1 = date_1.encode('utf8').split('年')[1].split('月')[0]  ## find date(month)
            #print date_m_1
            if int(date_m_1) < 10:  ## 1 --> 01,...
                date_m = "0"+date_m_1
            else:
                date_m = date_m_1
            #print date_m
            date_d_1 = date_1.encode('utf8').split('月')[1].split('日')[0]  ## find date(day)
            #print date_d_1
            if int(date_d_1) < 10:  ## 1 --> 01,...
                date_d = "0"+date_d_1
            else:
                date_d = date_d_1
            #print date_d
            date_h_1 = date_1.encode('utf8').split(' ')[1].split(':')[0]  ## find date(hour)
            #print date_h_1
            if int(date_h_1) < 10:  ## 1 --> 01,...
                date_h = "0"+date_h_1
            else:
                date_h = date_h_1
            #print date_h
            date_M_1 = date_1.encode('utf8').split(' ')[1].split(':')[1]  ## find date(minute)
            #print date_M_1
            if int(date_M_1) < 10:  ## 1 --> 01,...
                date_M = "0"+date_M_1
            else:
                date_M = date_M_1
            #print date_M
            date = date_y+"/"+date_m+"/"+date_d+" "+date_h+":"+date_M  ##  date for title
            #print date
            id_date = date_y+date_m+date_d+date_h+date_M  ## date for id
            #print id_date
            id_name = "facebook_tainanfood1_"+id_date+".txt"  ## id 
            print id_name
            h = open(id_name, 'w')  ## open content file
            h.write(date+"\n")
            h.write(link+"\n")
        for co in blog_content:
            content = co.text.encode('utf8').strip()  ## find content
            #print content
            h.write(content+"\n")
     
        h.close()
    except:
        print "skip"
print "done"
f.close()
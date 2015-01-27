# -*- coding:utf8 -*-
## ----- crawler pixnet content -----
import requests
from bs4 import BeautifulSoup

f = open("link.txt", 'r')  ## open links file
count = 64
lines = f.readlines()
for line in lines[64:]:  ## read begin with point line
    count += 1
    print count  ## print line number
    try:  ## try-catch
        link = line.strip()
        #print link
        author = link.split('.')[0].split('//')[1]
        #print author
        res = requests.get(link)
        res.encoding = 'utf8'
        response = res.text
        soup = BeautifulSoup(response)
        blog_title = soup.findAll('ul', {"class":"article-head"})  ## find blog title and date
        blog_content = soup.findAll('div', {"class":"article-content-inner"})  ## find content
    
        for ti in blog_title:
            title = ti.find('a').text.encode('utf8')
            ##print title
            date_y = ti.find('span', {"class":"year"}).text.encode('utf8').strip()  ## blog date(year)
            #print date_y
            date_m_1 = ti.find('span', {"class":"month"}).text.encode('utf8').strip()  ## blog date(month) 
            dic = {"Jan":"01", 
               "Feb":"02", 
               "Mar":"03", 
               "Apr":"04", 
               "May":"05", 
               "Jun":"06", 
               "Jul":"07", 
               "Aug":"08", 
               "Sep":"09", 
               "Oct":"10", 
               "Nov":"11", 
               "Dec":"12"}
            date_m = dic[date_m_1]  ## Jan --> 01,...
            #print date_m
            date_d = ti.find('span', {"class":"date"}).text.encode('utf8').strip()  ## blog date(day)
            #print date_d
            date_h = ti.find('span', {"class":"time"}).text.encode('utf8').strip().split(':')[0]  ## blog date(hour)
            #print date_h
            date_M = ti.find('span', {"class":"time"}).text.encode('utf8').strip().split(':')[1]  ## blog date(minute)
            #print date_M
            date = date_y+"/"+date_m+"/"+date_d+" "+date_h+":"+date_M  ## blog date for title
            #print date
            id_date = date_y+date_m+date_d+date_h+date_M  ## date for id
            #print id_date
            id_name = "pixnet_"+author+"_"+id_date+".txt"  ## id
            #print id_name
            w = open(id_name, 'w')  ## open content file
            w.write(title+"\n")
            w.write(date+"\n")
            w.write(link+"\n")
        for co in blog_content:
            content = ''.join(co.text.encode('utf8').strip().split(' '))  ## blog content
            #print content
            w.write(content+"\n")
    except:
        print "skip"
    w.close()
        
print "done"
f.close()
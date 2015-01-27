# -*- coding:utf-8 -*-
## ----- crawler yam travel content -----
import requests
from bs4 import BeautifulSoup


print "id|標題|日期|連結|內容"
count = 191
page_format = "http://travel.yam.com/find.aspx?p=%d"
style_format = "&kw=%e5%8f%b0%e5%8d%97"
for page in range(192, 2500000):  ## begin with which line
    res_page = requests.get(page_format%(page)+style_format)
    if res_page is not None:  ## when page is exist
        count += 1
        print count  ## print page number
        response_page = res_page.text.encode('utf8')
        soup_page = BeautifulSoup(response_page)
        #print soup_page
        blog_title_link = soup_page.findAll('h3', {'class':'infoListTitle'})  ## find blog title and link
        blog_date_ymd = soup_page.findAll('div', {'class':'articleInfo'})  ## find blog date
        for da_ymd in blog_date_ymd:
            author_1 = da_ymd.find('span').text.encode('utf8')
            #print author_1
            author = author_1.split(': ')[1]  ## blog author
            #print author
            a = open("author.txt", 'a')  ## open author file(search in yam blog)
            a.write(author+"\n")
            a.close()
            date_ymd_1 = da_ymd.find('time').text.encode('utf8')
            #print date_ymd_1
            date_y = date_ymd_1.split('.')[1]  ## blog date(year)
            #print date_y
            date_d = date_ymd_1.split('.')[0].split(' ')[1]  ## blog date(day)
            #print date_d
            date_m_1 = date_ymd_1.split('.')[0].split(' ')[0]  ## blog date(month)
            #print date_m_1
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
            id_date_ymd = date_y+date_m+date_d  ## blog date for id
            date_ymd = date_y+"/"+date_m+"/"+date_d  ## blog date for title
            #print date_ymd
            #print id_date_ymd
        for ti in blog_title_link:
            title = ti.find('a').text.encode('utf8')  ## blog title
            #print title
            link_1 = [tag['href'] for tag in ti.findAll('a', {'href':True})][0]  
            #print link_1
            name = link_1.split('=')[1]  ## blog author
            #print name
            link = "http://travel.yam.com/"+link_1  ## blog link
            #print link
            res_link = requests.get(link)
            response_link = res_link.text.encode('utf8')
            soup_link = BeautifulSoup(response_link)
            blog_content = soup_link.findAll('div', {'id':'mainArticleWrap'})  ## find blog content
            id_name = "yam_"+name+"_"+id_date_ymd+".txt"  ## id
            print id_name
            f = open(id_name, 'w')  ## open content file
            f.write(title+"\n")
            f.write(date_ymd+"\n")
            f.write(link+"\n")
            for co in blog_content:
                content_1 = co.findAll('p')
                content_2 = co.findAll('span')
                for co_1 in content_1:
                    #print co_1.text.encode('utf8')
                    if tag != 'a':
                        content = co_1.text.encode('utf8')
                        #print content
                        f.write(content+"\n")
                
                    
                    
                     
f.close()               
print "done"
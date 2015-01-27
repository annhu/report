# -*- coding:utf-8 -*-
## ----- crawler ptt food content -----
import requests
from bs4 import BeautifulSoup
import glob
import re

#https://www.ptt.cc/bbs/Food/index3852.html
count = 1461
page_format = "https://www.ptt.cc/bbs/Food/index%d"
style_format = ".html"
for page in range(1462,3854):
    try:
        res_page = requests.get(page_format%(page)+style_format, verify=False)
        #print res_page
        #res_page.encoding='utf-8'
        if res_page is not None:  ## when page is exist
            count += 1
            print count  ## print page number
            #test = "C:/Users/BigData/ipython notebook/blog_pixnet/"+str(count-1)+"*.txt"
            #if len(glob.glob(test)) == 0 :
                #print str(count-1)+"not here"
                #t = open("relink.txt", 'w')
                #t.write(style_format+page_format%(page-1))
                #print style_format+page_format%(page-1)
            response_page = res_page.text
            #print response_page
            soup_page = BeautifulSoup(response_page)
            #print soup_page
            blog_title = soup_page.select('.r-ent')  ## find title and link
            for ti in blog_title:
                author = ti.select('.author')[0].text.encode('utf8').strip()  ## blog author
                #print author
                title_1 = ti.select('.title')[0].text.encode('utf8').strip()
                #print title_1
                title = title_1.split("]")[1].strip()  ## blog title
                #print title
                m = re.search("台南", title)  ## find title contain "台南"
                if m:
                    #print title
                    #print author
                    link = "https://www.ptt.cc"+[tag['href'] for tag in ti.findAll('a', {"href":True})][0]  ## blog link 
                    #print link
                    res_link = requests.get(link, verify=False)
                    #print res_link
                    response_link = res_link.text
                    soup_link = BeautifulSoup(response_link)
                    blog_date = soup_link.findAll('div', {"class":"article-metaline"})[2:]  ## find blog date
                    blog_content = soup_link.findAll('div', {"id":"main-content"})  ## find blog content
                    #print blog_date
                    for da in blog_date:
                        date_1 = da.find('span', {'class':'article-meta-value'}).text.encode('utf8').strip()
                        #print date_1
                        date_y = date_1.split(' ')[4]  ## blog date(year)
                        #print date_y
                        date_m_1 = date_1.split(' ')[1]  ## blog date(month)
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
                        date_d = date_1.split(' ')[2]  ## blog date(day)
                        #print date_d
                        date_h = date_1.split(' ')[3].split(':')[0]  ## blog date(hour)
                        #print date_h
                        date_M = date_1.split(' ')[3].split(':')[1]  ## blog date(minute)
                        #print date_M
                        date = date_y+"/"+date_m+"/"+date_d+" "+date_h+":"+date_M  ## blog date for title
                        #print date
                        id_date = date_y+date_m+date_d+date_h+date_M  ## blog date for id
                        #print id_date
                        id_name = "ptt_"+author+"_"+id_date+".txt"  ## id
                        print id_name
                        f = open(id_name, 'w')  ## open content file
                        f.write(title+"\n")
                        f.write(date+"\n")
                        f.write(link+"\n")
                    for co in blog_content:
                        content = co.text.encode('utf8').strip()  ## blog content
                        #print content
                        f.write(content+"\n")
    

    except:
        print "skip"

f.close()
print count
print "done"
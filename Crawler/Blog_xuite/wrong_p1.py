# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


print "標題|日期|網址連結|id"
count = 0
style_format = "http://yo.xuite.net/info/search.php?keyword=%E5%8F%B0%E5%8D%97&search_type=s_yo&"
page_format = "p=%d"
for page in range(1, 2):
    count += 1
    print count
    res_page_m = requests.get(style_format+page_format%(page))
    #res_page.encoding='utf-8'
    if res_page_m is not None:  #當有這個page時
        response_page_m = res_page_m.text#.encode('utf-8')
        soup_page_m = BeautifulSoup(response_page_m)
        #print soup_page
        blog_title_link_m = soup_page_m.findAll('li', {'class':'componet-element-item'})  #要找每篇母網誌的標題和連結
        for ti_m in blog_title_link_m:
            title_m = ti_m.find('a' ,{'class':'componet-element-title'}).text.encode('utf8')  #每篇母網誌的標題
            #print title_m.text.encode('utf8')
            link_m_1 = [tag['href'] for tag in ti_m.findAll('a', {'class':'componet-element-title'})][0]
            link_m = "http://yo.xuite.net"+link_m_1  #每篇母網誌的連結
            #print link_m
            res_link_m = requests.get(link_m)
            response_link_m = res_link_m.text.encode('utf8')
            soup_link_m = BeautifulSoup(response_link_m)
            #print soup_link_m
            blog_author_m = soup_link_m.findAll('li', {'id':'element-owner'})  #要找每篇母網誌的作者
            blog_date_m = soup_link_m.findAll('li', {'id':'element-data-update-date'})  #要找每篇母網誌的日期時間
            blog_content_m = soup_link_m.findAll('div', {'id':'element-describe-content'})  #要找每篇母網誌的內容
            #print blog_content_m
            blog_link_s = soup_link_m.findAll('article', {'id':'element-article-main'})  #要找每篇子網誌的連結
            #print blog_link_s
            for au_m in blog_author_m:
                author_m = [tag['href'] for tag in au_m.findAll('a' ,{'href':True})][0].split('/')[1]  #每篇母網誌的作者
                #print author_m
            for da_m in blog_date_m:
                date_m_1 = da_m.find('time', {'class':'element-data-update-date-detail'}).text.encode('utf8')
                #print date_m_1
                date_ymd_m = date_m_1.split(' ')[0].replace('/','')  #每篇母網誌的日期
                #print date_ymd_m
                date_h_m = date_m_1.split(' ')[1].split(':')[0]  #每篇母網誌的時
                #print date_h_m
                date_m_m = date_m_1.split(' ')[1].split(':')[1]  #每篇母網誌的分
                #print date_m_m
                date_m = date_m_1.split(' ')[0]+" "+date_h_m+":"+date_m_m  #每篇母網誌的日期時間
                #print date_m
                id_date_m = date_ymd_m+date_h_m+date_m_m
                #print id_date_m
                id_name_m = "xuite_"+author_m+"_"+id_date_m+".txt"
                print id_name_m
                f = open(id_name_m, 'w')
                f.write(title_m+"\n")
                f.write(date_m+"\n")
                f.write(link_m+"\n")
            for co_m in blog_content_m:
                content_m_1 = co_m.findAll('p')
                for co_m_1 in content_m_1:
                    content_m = co_m_1.text.encode('utf8')
                    #print content_m
                    f.write(content_m+"\n")
            for li_s in blog_link_s:
                link_s_1 = [tag['href'] for tag in li_s.findAll('a' ,{'id':'element-article-more'})][0]
                #print link_s_1
                link_s = "http://yo.xuite.net/info/"+link_s_1
                #print link_s
                style_format_s = link_s
                page_format_s = "&p=%d"
                #http://yo.xuite.net/info/list_article.php?id=_CEFFCScycKwIAyGPDWx9M&p=1
                for page_s in range(1, 100):
                    res_page_s = requests.get(style_format_s+page_format_s%(page_s))
                    #print style_format_s+page_format_s%(page_s)
                    #res_page.encoding='utf-8'
                    if res_page_s is not None:  #當有這個page時
                        response_page_s = res_page_s.text.encode('utf8')
                        soup_page_s = BeautifulSoup(response_page_s)
                        blog_title_link_s = soup_page_s.findAll('li', {'class':'element-more-article-item'})
                        for ti_s in blog_title_link_s:
                            title = ti_s.find('a', {'class':'element-more-article-link'}).text.encode('utf8')
                            #print title                                                                                              
                            link = [tag['href'] for tag in ti_s.findAll('a', {'class':'element-more-article-link'})][0]
                            #print link
                            author = ""
                            for li in link.split('/')[3:5]:
                                author += li
                            #print author    
                            res_link = requests.get(link)
                            response_link = res_link.text.encode('utf8')
                            soup_link = BeautifulSoup(response_link)
                            blog_date = soup_link.findAll('span', {'class':'titledate'})
                            blog_content = soup_link.findAll('div', {'id':'content_all'})
                            for da in blog_date:
                                date_y = da.find('span', {'class':'titledate-year'}).text.encode('utf8')
                                date_m = da.find('span', {'class':'titledate-month'}).text.encode('utf8')
                                date_d = da.find('span', {'class':'titledate-day'}).text.encode('utf8')
                                date_h = da.find('span', {'class':'titledate-hour'}).text.encode('utf8')
                                date_M = da.find('span', {'class':'titledate-min'}).text.encode('utf8')
                                id_date = date_y+date_m+date_d+date_h+date_M
                                #print id_date
                                date = date_y+"/"+date_m+"/"+date_d+" "+date_h+":"+date_M
                                #print date
                                id_name = "xuite_"+author+"_"+id_date+".txt"
                                print id_name
                                s = open(id_name, 'w')
                                s.write(title+"\n")
                                s.write(date+"\n")
                                s.write(link+"\n")
                            for co in blog_content:
                                content_1 = co.findAll('p')
                                for co_1 in content_1:
                                    content = co_1.text.encode('utf8')
                                    #print content
                                    s.write(content+"\n")
                
s.close()                
f.close()            
print 'done'    
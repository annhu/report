# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

count = 0
res = requests.get('http://www.ipeen.com.tw/search/all/000/1-0-0-0/?p=1&adkw=%E5%8F%B0%E5%8D%97&baragain=1')
page_text = res.text.encode('utf8')
page_soup = BeautifulSoup(page_text)
page_link = page_soup.findAll('label', {"class" : "next_p_s"})
#print page_link

for pl in page_link:
    
#抓取最後一頁的連結
    page_number_link = [tag['href'] for tag in pl.findAll('a')][0]
    #print page_number_link
    
#抓取總頁數
    page_number_split = page_number_link.split("p=")[1]
    #print page_number_split
    page_number = page_number_split.split("&")[0]
    #print page_number
    
#抓取每一頁的連結
    style_format = "&adkw=%E5%8F%B0%E5%8D%97&baragain=1"
    page_format = "http://www.ipeen.com.tw/search/all/000/1-0-0-0/?p=%d"
    for page in range(1, int(page_number) + 1):
        #print page_format%(page)+style_format
        
#抓取所有店家名稱
        res = requests.get(page_format%(page)+style_format)
        #print res.text
        response_text = res.text.encode('utf8')
        soup = BeautifulSoup(response_text)
        shop1 = soup.select('.serShop')
        for i in shop1:
            count += 1
            #print i
            shop2 = i.find('a')
            shop2_open = i.find('span')
            if shop2_open.text.encode('utf8') != "【已歇業】":
                if shop2_open.text.encode('utf8') != "【已搬遷】":
                    print shop2.text.encode('utf-8').strip()

print count
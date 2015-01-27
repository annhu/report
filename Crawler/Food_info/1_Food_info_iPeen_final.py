# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

print "店名|區域|地址|電話|本店均消|營業時間|一|二|三|四|五|六|日|營運"
count = 0

res = requests.get('http://www.ipeen.com.tw/search/all/000/1-0-0-0/?p=1&adkw=%E5%8F%B0%E5%8D%97')
page_text = res.text.encode('utf8')
page_soup = BeautifulSoup(page_text)
page_link = page_soup.findAll('label', {"class" : "next_p_s"})  #>| (直接跳最後一頁)
#print page_link

for pl in page_link:
    
#抓取餐廳類別最後一頁的連結
    page_number_link = [tag['href'] for tag in pl.findAll('a')][0]
    #print page_number_link
    
#抓取餐廳類別總頁數
    page_number_split = page_number_link.split("p=")[1]
    #print page_number_split
    page_number = page_number_split.split("&")[0]
    #print page_number
    
#抓取餐廳類別每一頁的連結
    style_format = "&adkw=%E5%8F%B0%E5%8D%97"  #餐廳類別每一頁的連結相同地方
    page_format = "http://www.ipeen.com.tw/search/all/000/1-0-0-0/?p=%d"  #餐廳類別每一頁的連結不相同地方
    for page in range(1, int(page_number) + 1):  #餐廳類別連結第一頁到最後一頁
        #print page_format%(page)+style_format
        
#抓取所有店家名稱
        res = requests.get(page_format%(page)+style_format)
        #print res.text
        response_text = res.text.encode('utf8')
        soup = BeautifulSoup(response_text)
        shop1 = soup.select('.serShop')
        for i in shop1[1:]:
            count += 1
            #print count
            shop_name = i.find('a')  #要找店家的店名
            shop_info = i.select('.basic')  #要找店家的地址
            shop_open = i.find('span')  #要找店家是否還有營業
            shop_detail = i.select('.detail')  #要找店家iPeen的網址
            if shop_open.text.encode('utf8') != "【已歇業】":
                if shop_open.text.encode('utf8') != "【已搬遷】":
                    for n in shop_info:
                        name = shop_name.text.encode('utf8').strip()
                        #print name
                        address = n.find('span').text.encode('utf8').strip()
                        #print address
                        region = address.split("區")[0].split("市")[1]+"區"
                        #print region
                    for sp in shop_detail:
                        spend = sp.find('li', {"class":"costEmpty"}).text.encode('utf8').strip()
                        #print spend
                    for d in shop_detail:
                        shop_link_name = [tag['href'] for tag in i.findAll('a',{'href':True})][0].split('-')[0]
                        #print shop_link_name
                        shop_link = "http://www.ipeen.com.tw/" + shop_link_name[1:]  #店家iPeen的網址
                        #print shop_link
                        res_shop = requests.get(shop_link)
                        response_text_shop = res_shop.text.encode('utf8')
                        soup_shop = BeautifulSoup(response_text_shop)
                        soup_tel = soup_shop.select('.brief')  #要找店家的電話
                        soup_time = soup_shop.findAll('dl', {"class":"info"})  #要找店家的營業時間
                        soup_close = soup_shop.findAll('td')  #要找店家的公休日
                        num = len(soup_close)
                        for y in soup_tel:
                            shop_tel = y.findAll('p')  #店家的電話
                            for z in shop_tel[2:3]:
                                tel = z.text.encode('utf8').strip()
                                #print tel
                        for ti in soup_time:
                            shop_time = ti.find('span')  #店家的營業時間
                            if shop_time.text.encode('utf8') == "暫無提供":  #當店家沒有提供營業時間
                                time = "暫無提供"
                                #print time
                            else:
                                time = shop_time.text.encode('utf8').strip()
                                #print time
                        mon = 0
                        tue = 0
                        wed = 0
                        thu = 0
                        fri = 0
                        sat = 0
                        sun = 0
                        for close in soup_close:
                            if close.text.encode('utf8').split("週")[0] == "每":  #當有公休日時會顯示"每週X"
                                num += 1  #為了使有印過的不要在else中再印一次,使之最後不會=0
                                day = close.text.encode('utf8')
                                #print day
                                day_1 = day.split("週")[1]
                                #print day_1
                                if day_1 == "一":
                                    mon = 1
                                elif day_1 == "二":
                                    tue = 1
                                elif day_1 == "三":
                                    wed = 1
                                elif day_1 == "四":
                                    thu = 1
                                elif day_1 == "五":
                                    fri = 1
                                elif day_1 == "六":
                                    sat = 1
                                elif day_1 == "日":
                                    sun = 1
                                print name+"|"+region+"|"+address+"|"+tel+"|"+spend+"|"+time+"|"+str(mon)+"|"+str(tue)+"|"+str(wed)+"|"+str(thu)+"|"+str(fri)+"|"+str(sat)+"|"+str(sun)+"|"+"0"
                            else:
                                num -=1  #在if中沒印過的,每次都減一,最後會=0
                                if num == 0:  #當在if沒印過時,最後一次會印出
                                    print name+"|"+region+"|"+address+"|"+tel+"|"+spend+"|"+time+"|"+str(mon)+"|"+str(tue)+"|"+str(wed)+"|"+str(thu)+"|"+str(fri)+"|"+str(sat)+"|"+str(sun)+"|"+"0"
                                    
                                                                           
                                            

                                    
print count
print "done"
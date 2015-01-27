# -*- coding:utf-8 -*-
## ----- test crawler facebook -----
import requests
from bs4 import BeautifulSoup

link = "https://www.facebook.com/hotainnan/photos/a.389728494397035.78669.389723111064240/771441932892354/?type=1"  ## first page link
res_page = requests.get(link)
response_page = res_page.text.encode('utf8')
soup_page = BeautifulSoup(response_page)
#print soup_page
blog_content = soup_page.findAll('span', {'class':'hasCaption'})  ## find blog content
#print blog_content

for co in blog_content:
    content_1 = co.findAll('span')
    for co_1 in content_1:
        print co_1.text.encode('utf8').strip()
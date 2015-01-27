# -*- coding: utf-8 -*-
import simplejson, urllib 
from pygeocoder import Geocoder

r = open("Food_info_iPeen_final.txt", 'r')
l = open("Food_info_iPeen_final_lat_lng.txt", 'r')
c = open("com.txt", 'a')
i = 0
lines_1 = r.readlines()
lines_2 = l.readlines()
while i>=0:
    for li_1 in lines_1[i:i+1]:
        info_1 = li_1.strip()
        #print info_1
        name_1 = li_1.strip().split('|')[0]
        #print name_1

        for li_2 in lines_2[i:i+1]:
            info_2 = li_2.strip()
            #print info_2
            name_2 = li_2.strip().split('|')[0]
            #print name_2
            lat_lng_2 = li_2.strip().split('|')[2]+"|"+li_2.strip().split('|')[3]
            #print lat_lng_2

            #print name_1.strip()
            #print name_2.strip()
            info_final = info_1+"|"+lat_lng_2
            print info_final
        
            c.write(info_final+"\n")
    i += 1   


c.close()
l.close()    
r.close()
print "done"
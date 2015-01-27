# -*- coding: utf-8 -*-
import simplejson, urllib 
from pygeocoder import Geocoder

count=0
r = open("Food_info_boylondon_final.txt", 'r')
h = open("Food_info_boylondon_final_lat_lng.txt", 'a')
lines = r.readlines()[count:]
for li in lines:
    count+=1
    #print count
    line = li.strip()
    #print line
    name = li.strip().split('|')[0]
    #print li.strip()
    address = li.strip().split('|')[2]
    #print address
    try:
        results = Geocoder.geocode(address)
        lat_lng=results[0].coordinates
        #print lat_lng
        lng = str(lat_lng).split(', ')[1][:-1]  #經度
        #print lng
        lat = str(lat_lng).split(', ')[0][1:]  #緯度
        #print lat
        info = line+"|"+lng+"|"+lat
        #print info
        h.write(info+"\n")
    except:
        print count
    
h.close()
r.close()
print "done"
# -*- coding: utf-8 -*- 
import mysql.connector
import time
from pygeocoder import Geocoder

cnx = mysql.connector.connect(user='yb101', password='iii',
                              host='10.120.28.19',
                              database='db01',
                              charset='utf8',
                              use_unicode=True)
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)
query = ("SELECT hotelid, hoteladdress FROM hotelinfo")
cursor.execute(query)
for hotelid, hoteladdress in cursor:
    time.sleep(0.3)
    print hotelid
    print hoteladdress
    try:
        results = Geocoder.geocode(hoteladdress)
        lat = results[0].coordinates[0]
        lng = results[0].coordinates[1]
        print lat
        print lng
        cursor1.execute ("""UPDATE hotelinfo SET hotellat=%s, hotellng=%s WHERE hotelid=%s""", (lat,lng,hotelid))
        cnx.commit()
    except:
        print hotelid+"error"
cursor1.close()
cursor.close()
cnx.close()
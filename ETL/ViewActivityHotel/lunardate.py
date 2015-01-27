# -*- coding: utf-8 -*- 
import mysql.connector
from lunardate import LunarDate

cnx = mysql.connector.connect(user='yb101', password='iii',
                              host='10.120.28.19',
                              database='db01',
                              charset='utf8',
                              use_unicode=True)
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)
query = ("SELECT dateid, calendartype,activityyear,activitystartdate,activityendtdate FROM activitydate")
cursor.execute(query)
##row = cursor.fetchone()
for id,type,year,start,end in cursor:
    print id
    #print type
    #print year
    #print start
    #print end
    if type =='lunar':
        startmonth = int(start.split('/')[0])
        startd = int(start.split('/')[1])
        startsolardate = LunarDate(year, startmonth, startd).toSolarDate()
        print startsolardate
        endmonth = int(end.split('/')[0])
        endd = int(end.split('/')[1])
        endsolardate = LunarDate(year, endmonth, endd).toSolarDate()
        print endsolardate
    else:
        startmonth = start.split('/')[0]
        startd = start.split('/')[1]
        if len(startmonth)==1:
            startm = '0'+startmonth
        startsolardate=str(year)+'-'+startm+'-'+startd
        print startsolardate
    
        endmonth = end.split('/')[0]
        endd = end.split('/')[1]
        if len(endmonth)==1:
            endm = '0'+startmonth
        endsolardate=str(year)+'-'+endm+'-'+startd
        print endsolardate
    cursor1.execute ("""UPDATE activitydate SET currentstartdate=%s, currentenddate=%s WHERE dateid=%s""",(startsolardate,endsolardate,id))
    cnx.commit()
cursor1.close()
cursor.close()
cnx.close()
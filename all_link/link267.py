
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getDate as getDatea,getBody
def link267():
    getList(
        datea=".sys_news-posted-date",
        content=".sys_record-control.sys_news-record > p",
        imajina=".sys_record-image-control > img",
        pagis=1,
        getDatea=getDatea,
        replaceRegex=None,
        numero="267",
        LA_name="Dover",
        LA_pr="https://www.dover.gov.uk/News/Home.aspx",
        links="https://www.dover.gov.uk/News/Home.aspx",
        listas=".sys_subitem",
        datesss=None,
        replaceDate=None,
        title="h3",
        getBody=getBody,
        imajinasi="sam",
        linkedin="https://www.dover.gov.uk",
        href="a",
        linkedin2="https://www.dover.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="267",LA_name="Dover",LA_pr="https://www.dover.gov.uk/News/Home.aspx",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        
        namber=str(number)
        setop=False
        link=links
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup=None
        if r.headers['content-type']=="application/json":
            a=json.loads(r.text)
            soup = BeautifulSoup(a["html"], 'html.parser')
        else:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # print(soup)
        lista=soup.select(listas)
            # print(lista[0].prettify())
            
            
        for a in lista:
                
            s=None
            if datesss:
                s=a.select_one(datesss).getText().replace(replaceDate,"") if replaceDate else a.select_one(datesss).getText()
            if replaceRegex:
                cop=re.search(replaceRegex, a.select_one(datesss).getText())
                s=cop.group() if cop else ""
            if getDatea:
                s=getDatea(linkedin+a.select_one(href).get("href"),date=datea,replaceDate="Posted on ")
                # print(s)
                # print(a.select_one("a").get("href"))
            imajin=linkedin2+a.select_one(imajinasi).get("src") if a.select_one(imajinasi) else "" if imajinasi else ""
            titulos=a.select_one("a").get("title") if a.select_one("a") else ""
                
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a.select_one(title).getText().replace('\n', ' ').replace('\r', '').strip() if a.select_one(title) else titulos if titulos else ""
                        )
                coki=getBody(linkedin+a.select_one(href).get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina)
                papa.body=coki[0] if len(coki) > 0 and coki else ""
                papa.image=linkedin2+coki[1] if len(coki) > 0 and coki[1] != "" else imajin
                papa.save()
                    
        
    except Exception as e:
        print("err "+numero+" ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = parse(dates.strip())
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = parse(dates.strip())
    dateCompare = date(2020, 6, 1)  
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared



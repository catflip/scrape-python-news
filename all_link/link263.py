
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getDate as getDatea,getBody

def link263():
    getList(
        datea=None,
        content="article > *:not(h1)",
        imajina="figure > img",
        pagis=1,
        getDatea=None,
        replaceRegex=None,
        numero="263",
        LA_name="Test Valley",
        LA_pr="https://www.testvalley.gov.uk/news",
        links="https://www.testvalley.gov.uk/news",
        listas=".promo",
        datesss="time.published",
        replaceDate=None,
        title=".h3",
        getBody=getBody,
        imajinasi="sam",
        linkedin="https://www.testvalley.gov.uk",
        href="a",
        linkedin2="https://www.testvalley.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="263",LA_name="Test Valley",LA_pr="https://www.testvalley.gov.uk/news",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
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
                s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
            
                # print(a.select_one("a").get("href"))
            imajin=linkedin2+a.select_one(imajinasi).get("src") if a.select_one(imajinasi) else "" if imajinasi else ""
            
            titulos=a.get("title") if a.get("title") else ""
            
            if compareDate(s,lastDate):
                papa,created=Links.get_or_create(
                        LA_name=LA_name,
                        LA_pr=LA_pr,
                        date=getDate(s),                        
                        title=a.select_one(title).getText().replace('\n', ' ').replace('\r', '').strip() if a.select_one(title) else titulos if titulos else ""
                        )
                coki=getBody(linkedin+a.get("href").replace('\n', ' ').replace('\r', '').strip(),content=content,imajin=imajina)
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



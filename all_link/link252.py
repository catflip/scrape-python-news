
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
import json
import re
from all_link.helpers.helper import getBody,getDate as getDatea
import ast
def link252():
    getList(
        datea=None,
        content=".newsArticle",
        imajina="sam",
        pagis=0,
        getDatea=None,
        replaceRegex=None,
        numero="252",
        LA_name="Greater Manchester",
        LA_pr="https://www.greatermanchester-ca.gov.uk/news/",
        links=None,
        listas=".newsItem",
        datesss="small.badge-secondary.bluebck",
        replaceDate=None,
        title="p.card-text.h4",
        getBody=getBody,
        imajinasi=".card-img-top",
        linkedin="https://www.greatermanchester-ca.gov.uk",
        href="a",
        linkedin2="https://www.greatermanchester-ca.gov.uk"
    )
def getList(datea=None,content="sam",imajina="",pagis=1,getDatea=None,replaceRegex=None,numero="252",LA_name="Greater Manchester",LA_pr="https://www.greatermanchester-ca.gov.uk/news/",links=None,listas=None,datesss=None,replaceDate=None,title=None,getBody=None,imajinasi=None,linkedin="",href="a",linkedin2=""):
    
    number=pagis
    try:
        print("link "+numero+" start scraping...")
        lastDate=Links.select().where(Links.LA_name==LA_name,Links.LA_pr==LA_pr).order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number*4)
            setop=False
            link="https://www.greatermanchester-ca.gov.uk/Umbraco/Api/FilterNews/NewsFilter?pageId=3097&currentCount=%s&moreCount=4&filter=All&sortBy=None" % (namber)
            # print(link)
            # print(namber)
            headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
            r = requests.get(link, timeout=15,verify=False,headers=headers)
            soup=None
            if r.headers['content-type']=="application/json":
                a=json.loads(r.text)
                soup = BeautifulSoup(a["html"], 'html.parser')
            else:
                soup = BeautifulSoup(ast.literal_eval(r.text), 'html.parser')
                
            # soup = BeautifulSoup(soup, 'html.parser')
            # print(BeautifulSoup(r.text))
            
            
            lista=soup.select(listas)
            
            # print(lista[0].prettify())
            
            if len(lista) == 0:
                
                break
            for a in lista:
                
                s=None
                if datesss:
                    s=a.select_one(datesss).getText().replace(replaceDate,"") if replaceDate else a.select_one(datesss).getText()
                if replaceRegex:
                    cop=re.search(replaceRegex, a.select_one(datesss).getText())
                    s=cop.group() if cop else ""
                if getDatea:
                    s=getDatea(linkedin+a.select_one(href).get("href"),date=datea)
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
                    
                else:
                    setop=True
                    # break
            if setop:
                # print("s")
                break
            number+=1
    except Exception as e:
        print("err "+numero+" ", str(e) )
        # return pa
    # return pa
        
    

def getDate(dates):
    dt = parse(dates.strip())
    date2 = date(dt.year, dt.month, dt.day)
    return date2.strftime('%Y-%m-%d %H:%M:%S')
def compareDate(dates,lastDate):
    dt = parse(dates.strip(),dayfirst=True)
    dateCompare = date(2020, 6, 1)  
    if len(lastDate)>0:
        dateLen=lastDate[0].date
        dateCompare=date(dateLen.year,dateLen.month,dateLen.day)  
    date2 = date(dt.year, dt.month, dt.day)
    dateCompared = date2 > dateCompare          
    return dateCompared



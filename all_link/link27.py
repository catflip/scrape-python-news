import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def link27():
    getList()

def getList():
    pa=[]
    number=1
    try:
        print("link 27 start scraping...")
        lastDate=Links.select().where(Links.LA_name=="Halton",Links.LA_pr=="https://hbcnewsroom.co.uk/").order_by(Links.date.desc())
        # lastDate=[]
        while True:
            namber=str(number)
            setop=False
            link='https://hbcnewsroom.co.uk/archivednews/page/'+namber
            r = requests.get(link, timeout=15,verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            lista=soup.select("article")
            if len(lista) == 0:
                break
            for a in lista[::-1]:
                s=a.select_one("span.updated").getText()
                # print(s)
                # print(a.select_one("a").get("href"))
                if compareDate(s,lastDate):
                    papa,created=Links.get_or_create(
                        LA_name="Halton",
                        LA_pr="https://hbcnewsroom.co.uk/",
                        date=getDate(s),                        
                        title=a.select_one("h2.post-title.entry-title").getText()
                        )
                    papa.body=getBody(a.select_one("a").get("href"))
                    papa.image=a.select_one("img").get("src") if a.select_one("img") else ""
                    papa.save()
                    
                else:
                    setop=True
            if setop:
                break
            number+=1
    except Exception as e:
        print("err link 27 ", str(e) )
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
def getBody(link):
    panda1=""
    try:
        r = requests.get(link, timeout=15,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one('div.post-content').getText().replace('\n', ' ').replace('\r', '').strip()
        return panda1
     
    except:
        return panda1
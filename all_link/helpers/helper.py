import requests
from datetime import datetime,date,timedelta 
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
def getDate(link=None,date="sam"):
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda1=soup.select_one(date).getText() if soup.select_one(date) else "1 January 2020"
        return panda1
     
    except:
        return "1 January 2020"
def getBody(link=None,content="sam",imajin="sam"):
    panda1=""
    image=""
    try:
        headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        
        r = requests.get(link, timeout=15,verify=False,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        panda=soup.select(content) if soup.select(content) else []
        for a in panda:
            panda1+=a.getText().replace('\n', ' ').replace('\r', '').strip()            
        
        image=soup.select_one(imajin).get("src") if soup.select_one(imajin) else ""
        return [panda1,image]
     
    except:
        return None
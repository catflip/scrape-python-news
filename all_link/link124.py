
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link124():
    getList(
    numero="124",
    LA_name="Surrey Heath",
    LA_pr="https://www.surreyheath.gov.uk/council/news",
    links="https://www.surreyheath.gov.uk/news/rss.xml",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content=".field-item > *:not(span)",
    imajina="sam",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")


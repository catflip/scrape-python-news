
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link81():
    getList(
    numero="81",
    LA_name="Fareham",
    LA_pr="https://www.fareham.gov.uk/latest_news/intro.aspx",
    links="https://www.cheltenham.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > *:not(h2):not(.date):not(ul):not(img)",
    imajina="#content > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")


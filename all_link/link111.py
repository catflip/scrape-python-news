
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.rss import getList
from all_link.helpers.helper import getDate,getBody
def link111():
    getList(
    numero="111",
    LA_name="East Lothian",
    LA_pr="https://www.eastlothian.gov.uk/news",
    links="https://www.eastlothian.gov.uk/rss/news",
    listas="item",
    datesss="pubDate",
    replaceDate=None,
    titles="title",
    getBody=getBody,
    content="#content > *:not(p):not(span)",
    imajina="#content > img",
    imajinasi="sam",
    linkedin="",
    href="link",
    linkedin2="")


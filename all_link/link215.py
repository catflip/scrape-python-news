
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link215():
    getList(
    pagis=1,
    numero="215",
    LA_name="Merthyr Tydfil",
    LA_pr="https://www.merthyr.gov.uk/news-and-events/latest-news/",
    links="https://www.merthyr.gov.uk/news-and-events/latest-news/?page=",
    listas=".listing",
    datesss="h5",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h4",
    getBody=getBody,
    content=".news-listing-page",
    imajina=".img-article",
    imajinasi="sam",
    linkedin="https://www.merthyr.gov.uk",
    href="a",
    linkedin2="https://www.merthyr.gov.uk")



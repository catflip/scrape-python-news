
import requests
from datetime import datetime,date
from bs4 import BeautifulSoup
from mysqls.pandasql import Links
from dateutil.parser import parse
from all_link.page.pages import getList
from all_link.helpers.helper import getDate,getBody
import re
def link171():
    getList(
    pagis=1,
    numero="171",
    LA_name="Tonbridge and Malling",
    LA_pr="https://www.tmbc.gov.uk/news",
    links="https://www.thurrock.gov.uk/news?page=",
    listas="div.views-row",
    datesss=".date-display-single",
    replaceDate=None,
    replaceRegex=None,
    getDatea=None,
    title="h2",
    getBody=getBody,
    content="div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div > *",
    imajina="sam",
    imajinasi="sam",
    linkedin="https://www.thurrock.gov.uk",
    href="a",
    linkedin2="https://www.thurrock.gov.uk")


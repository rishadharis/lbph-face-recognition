from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os

import urllib.request

import pandas as pd
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
ngaran = []
price = []
key = "5fbbe5479b7340f68dc1814e0ab87bf7"
driver.get("https://ta.risgad.xyz/scrape?key="+key)
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
start_time = time.time()
for a in soup.findAll('div', attrs={'class':'data'}):
    if not os.path.exists('dataset/'+a["value"]+'_'+a["name"]):
        os.makedirs('dataset/'+a["value"]+'_'+a["name"])

    for b in a.findAll('img', src=True, attrs={'class':'photo'}):
        lnk = b["src"]
        nim = lnk[30:38]
        filename = lnk.split('/')[-1]
        if os.path.isfile('dataset/'+a["value"]+'_'+a["name"] + '/' + filename) == False:
            urllib.request.urlretrieve(lnk,'dataset/'+a["value"]+'_'+a["name"] + '/' + filename)

lama = time.time()-start_time
print(lama)
# 05.30

import pandas as pd
from bs4 import BeautifulSoup
import requests






url='http://openapi.foodsafetykorea.go.kr/api/e04a6c69c11641708150/COOKRCP01/xml/1/5'
req=requests.get(url)
html=req.text
soup=BeautifulSoup(html, 'html.parser')
rcp_seq_number = soup.find_all('rcp_seq')

rcp_seqlist = [];

# print(html)
# print(soup)
# print('################')
print(rcp_seq_number[0].text)



for rcp_seq in rcp_seq_number:
    rcp_seqlist.append(rcp_seq.text)
    # print(code.text)

for i in rcp_seqlist:
    print(i)


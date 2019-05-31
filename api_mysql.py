import pymysql
from bs4 import BeautifulSoup
import requests

url='http://openapi.foodsafetykorea.go.kr/api/e04a6c69c11641708150/COOKRCP01/xml/1/5'
req=requests.get(url)
html=req.text
soup=BeautifulSoup(html, 'html.parser')
rcp_seq_number = soup.find_all('rcp_seq')

rcp_seq_list = [];

for rcp_seq in rcp_seq_number:
    rcp_seq_list.append(rcp_seq.text)
    # print(code.text)

# for i in rcp_seq_list:
#     print(i)

con = pymysql.connect(host="localhost", user="root", password="1234",
                      db='bixby', charset='utf8')

cur = con.cursor()

# sql = "select * from test"
# sql = "insert into test (name, address, num) values (%s, %s, %s)"
# val = ("John123", "", 1)
# num = cur.execute(sql, val)
# con.commit()
# print(num)
#
for i in range(1, 5):
    sql = "insert into recipes ( rcp_seq, rcp_nm, rcp_way2, rcp_pat2, info_wgt," \
          "info_eng, info_car, info_pro, info_fat, info_na, hash_tag, att_file_no_main, att_file_no_mk, rcp_parts_dtls, " \
          "manual01, manual_img01, manual02, manual_img02, manual03, manual_img03, manual04, manual_img04, " \
          "manual05, manual_img05, manual06, manual_img06, manual07, manual_img07, manual08, manual_img08, " \
          "manual09, manual_img09, manual10, manual_img10, manual11, manual_img11, manual12, manual_img12, " \
          "manual13, manual_img13, manual14, manual_img14, manual15, manual_img15, manual16, manual_img16, " \
          "manual17, manual_img17, manual18, manual_img18, manual19, manual_img19, manual20, manual_img20) " \
          "values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (rcp_seq_list[i], "", "", "", 1, 1, 1, 1, 1, 1 ,"" ,"" ,"" ,""
    , "", "", "", "", "", "", "", "", "", ""
    , "", "", "", "", "", "", "", "", "", ""
    , "", "", "", "", "", "", "", "", "", ""
    , "", "", "", "", "", "", "", "", "", "")
    num = cur.execute(sql, val)
    con.commit()

# print(rcp_seq_list[0])
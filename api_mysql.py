import pymysql
from bs4 import BeautifulSoup
import requests

url='http://openapi.foodsafetykorea.go.kr/api/key/COOKRCP01/xml/1/1000'
# url='http://openapi.foodsafetykorea.go.kr/api/e04a6c69c11641708150/COOKRCP01/xml/1001/1198'
req=requests.get(url)
html=req.text
soup=BeautifulSoup(html, 'html.parser')

rcp_seq_list = [];
rcp_nm_list = [];
rcp_way2_list = [];
rcp_pat2_list = [];
info_wgt_list = [];
info_eng_list = [];
info_car_list = [];
info_pro_list = [];
info_fat_list = [];
info_na_list = [];
hash_tag_list = [];
att_file_no_main_list = [];
att_file_no_mk_list = [];
rcp_parts_dtls_list = [];
manual01_list = [];
manual_img01_list = [];
manual02_list = [];
manual_img02_list = [];
manual03_list = [];
manual_img03_list = [];
manual04_list = [];
manual_img04_list = [];
manual05_list = [];
manual_img05_list = [];
manual06_list = [];
manual_img06_list = [];
manual07_list = [];
manual_img07_list = [];
manual08_list = [];
manual_img08_list = [];
manual09_list = [];
manual_img09_list = [];
manual10_list = [];
manual_img10_list = [];
manual11_list = [];
manual_img11_list = [];
manual12_list = [];
manual_img12_list = [];
manual13_list = [];
manual_img13_list = [];
manual14_list = [];
manual_img14_list = [];
manual15_list = [];
manual_img15_list = [];
manual16_list = [];
manual_img16_list = [];
manual17_list = [];
manual_img17_list = [];
manual18_list = [];
manual_img18_list = [];
manual19_list = [];
manual_img19_list = [];
manual20_list = [];
manual_img20_list = [];

rcp_seq_api = soup.find_all('rcp_seq') # 일련번호
rcp_nm_api = soup.find_all('rcp_nm') # 메뉴명
rcp_way2_api = soup.find_all('rcp_way2') # 조리방법
rcp_pat2_api = soup.find_all('rcp_pat2') # 요리종류
info_wgt_api = soup.find_all('info_wgt') # 중량(1인분)
info_eng_api = soup.find_all('info_eng') # 열량
info_car_api = soup.find_all('info_car') # 탄수화물
info_pro_api = soup.find_all('info_pro') # 단백질
info_fat_api = soup.find_all('info_fat') # 지방
info_na_api = soup.find_all('info_na') # 나트륨
hash_tag_api = soup.find_all('hash_tag') # 해쉬태그
att_file_no_main_api = soup.find_all('att_file_no_main') # 이미지경로(소)
att_file_no_mk_api = soup.find_all('att_file_no_mk') # 이미지경로(대)
rcp_parts_dtls_api = soup.find_all('rcp_parts_dtls') # 재료정보
manual01_api = soup.find_all('manual01') # 만드는법_01
manual_img01_api = soup.find_all('manual_img01') # 만드는법_이미지_01
manual02_api = soup.find_all('manual02') # 만드는법_02
manual_img02_api = soup.find_all('manual_img02') # 만드는법_이미지_02
manual03_api = soup.find_all('manual03') # 만드는법_03
manual_img03_api = soup.find_all('manual_img03') # 만드는법_이미지_03
manual04_api = soup.find_all('manual04') # 만드는법_04
manual_img04_api = soup.find_all('manual_img04') # 만드는법_이미지_04
manual05_api = soup.find_all('manual05') # 만드는법_05
manual_img05_api = soup.find_all('manual_img05') # 만드는법_이미지_05
manual06_api = soup.find_all('manual06') # 만드는법_06
manual_img06_api = soup.find_all('manual_img06') # 만드는법_이미지_06
manual07_api = soup.find_all('manual07') # 만드는법_07
manual_img07_api = soup.find_all('manual_img07') # 만드는법_이미지_07
manual08_api = soup.find_all('manual08') # 만드는법_08
manual_img08_api = soup.find_all('manual_img08') # 만드는법_이미지_08
manual09_api = soup.find_all('manual09') # 만드는법_09
manual_img09_api = soup.find_all('manual_img09') # 만드는법_이미지_09
manual10_api = soup.find_all('manual10') # 만드는법_10
manual_img10_api = soup.find_all('manual_img10') # 만드는법_이미지_10
manual11_api = soup.find_all('manual11') # 만드는법_11
manual_img11_api = soup.find_all('manual_img11') # 만드는법_이미지_11
manual12_api = soup.find_all('manual12') # 만드는법_12
manual_img12_api = soup.find_all('manual_img12') # 만드는법_이미지_12
manual13_api = soup.find_all('manual13') # 만드는법_13
manual_img13_api = soup.find_all('manual_img13') # 만드는법_이미지_13
manual14_api = soup.find_all('manual14') # 만드는법_14
manual_img14_api = soup.find_all('manual_img14') # 만드는법_이미지_14
manual15_api = soup.find_all('manual15') # 만드는법_15
manual_img15_api = soup.find_all('manual_img15') # 만드는법_이미지_15
manual16_api = soup.find_all('manual16') # 만드는법_16
manual_img16_api = soup.find_all('manual_img16') # 만드는법_이미지_16
manual17_api = soup.find_all('manual17') # 만드는법_17
manual_img17_api = soup.find_all('manual_img17') # 만드는법_이미지_17
manual18_api = soup.find_all('manual18') # 만드는법_18
manual_img18_api = soup.find_all('manual_img18') # 만드는법_이미지_18
manual19_api = soup.find_all('manual19') # 만드는법_19
manual_img19_api = soup.find_all('manual_img19') # 만드는법_이미지_19
manual20_api = soup.find_all('manual20') # 만드는법_20
manual_img20_api = soup.find_all('manual_img20') # 만드는법_이미지_20

for rcp_seq in rcp_seq_api:
    rcp_seq_list.append(rcp_seq.text)
for rcp_nm in rcp_nm_api:
    rcp_nm_list.append(rcp_seq.text)
for rcp_way2 in rcp_way2_api:
    rcp_way2_list.append(rcp_way2.text)
for rcp_pat2 in rcp_pat2_api:
    rcp_pat2_list.append(rcp_pat2.text)
for info_wgt in info_wgt_api:
    info_wgt_list.append(info_wgt.text)
for info_eng in info_eng_api:
    info_eng_list.append(info_eng.text)
for info_car in info_car_api:
    info_car_list.append(info_car.text)
for info_pro in info_pro_api:
    info_pro_list.append(info_pro.text)
for info_fat in info_fat_api:
    info_fat_list.append(info_fat.text)
for info_na in info_na_api:
    info_na_list.append(info_na.text)
for hash_tag in hash_tag_api:
    hash_tag_list.append(hash_tag.text)
for att_file_no_main in att_file_no_main_api:
    att_file_no_main_list.append(att_file_no_main.text)
for att_file_no_mk in att_file_no_mk_api:
    att_file_no_mk_list.append(att_file_no_mk.text)
for rcp_parts_dtls in rcp_parts_dtls_api:
    rcp_parts_dtls_list.append(rcp_parts_dtls.text)
for manual01 in manual01_api:
    manual01_list.append(manual01.text)
for manual_img01 in manual_img01_api:
    manual_img01_list.append(manual_img01.text)
for manual02 in manual02_api:
    manual02_list.append(manual02.text)
for manual_img02 in manual_img02_api:
    manual_img02_list.append(manual_img02.text)
for manual03 in manual03_api:
    manual03_list.append(manual03.text)
for manual_img03 in manual_img03_api:
    manual_img03_list.append(manual_img03.text)
for manual04 in manual04_api:
    manual04_list.append(manual04.text)
for manual_img04 in manual_img04_api:
    manual_img04_list.append(manual_img04.text)
for manual05 in manual05_api:
    manual05_list.append(manual05.text)
for manual_img05 in manual_img05_api:
    manual_img05_list.append(manual_img05.text)
for manual06 in manual06_api:
    manual06_list.append(manual06.text)
for manual_img06 in manual_img06_api:
    manual_img06_list.append(manual_img06.text)
for manual07 in manual07_api:
    manual07_list.append(manual07.text)
for manual_img07 in manual_img07_api:
    manual_img07_list.append(manual_img07.text)
for manual08 in manual08_api:
    manual08_list.append(manual08.text)
for manual_img08 in manual_img08_api:
    manual_img08_list.append(manual_img08.text)
for manual09 in manual09_api:
    manual09_list.append(manual09.text)
for manual_img09 in manual_img09_api:
    manual_img09_list.append(manual_img09.text)
for manual10 in manual10_api:
    manual10_list.append(manual10.text)
for manual_img10 in manual_img10_api:
    manual_img10_list.append(manual_img10.text)
for manual11 in manual11_api:
    manual11_list.append(manual11.text)
for manual_img11 in manual_img11_api:
    manual_img11_list.append(manual_img11.text)
for manual12 in manual12_api:
    manual12_list.append(manual12.text)
for manual_img12 in manual_img12_api:
    manual_img12_list.append(manual_img12.text)
for manual13 in manual13_api:
    manual13_list.append(manual13.text)
for manual_img13 in manual_img13_api:
    manual_img13_list.append(manual_img13.text)
for manual14 in manual14_api:
    manual14_list.append(manual14.text)
for manual_img14 in manual_img14_api:
    manual_img14_list.append(manual_img14.text)
for manual15 in manual15_api:
    manual15_list.append(manual15.text)
for manual_img15 in manual_img15_api:
    manual_img15_list.append(manual_img15.text)
for manual16 in manual16_api:
    manual16_list.append(manual16.text)
for manual_img16 in manual_img16_api:
    manual_img16_list.append(manual_img16.text)
for manual17 in manual17_api:
    manual17_list.append(manual17.text)
for manual_img17 in manual_img17_api:
    manual_img17_list.append(manual_img17.text)
for manual18 in manual18_api:
    manual18_list.append(manual18.text)
for manual_img18 in manual_img18_api:
    manual_img18_list.append(manual_img18.text)
for manual19 in manual19_api:
    manual19_list.append(manual19.text)
for manual_img19 in manual_img19_api:
    manual_img19_list.append(manual_img19.text)
for manual20 in manual20_api:
    manual20_list.append(manual20.text)
for manual_img20 in manual_img20_api:
    manual_img20_list.append(manual_img20.text)\


con = pymysql.connect(host="localhost", user="root", password="1234",
                      db='bixby', charset='utf8')

cur = con.cursor()

# for i in range(0, rcp_seq_list.__len__()-1):
for i in range(0, rcp_seq_list.__len__() - 1):
    sql = "insert into recipes (rcp_seq, rcp_nm, rcp_way2, rcp_pat2," \
          "info_eng, info_car, info_pro, info_fat, info_na, hash_tag, att_file_no_main, att_file_no_mk, rcp_parts_dtls, " \
          "manual01, manual_img01, manual02, manual_img02, manual03, manual_img03, manual04, manual_img04, " \
          "manual05, manual_img05, manual06, manual_img06, manual07, manual_img07, manual08, manual_img08, " \
          "manual09, manual_img09, manual10, manual_img10, manual11, manual_img11, manual12, manual_img12, " \
          "manual13, manual_img13, manual14, manual_img14, manual15, manual_img15, manual16, manual_img16, " \
          "manual17, manual_img17, manual18, manual_img18, manual19, manual_img19, manual20, manual_img20) " \
          "values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (rcp_seq_list[i], rcp_nm_list[i], rcp_way2_list[i], rcp_pat2_list[i], info_eng_list[i], info_car_list[i],
           info_pro_list[i], info_fat_list[i], info_na_list[i], hash_tag_list[i], att_file_no_main_list[i],
           att_file_no_mk_list[i], rcp_parts_dtls_list[i],
           manual01_list[i], manual_img01_list[i], manual02_list[i], manual_img02_list[i], manual03_list[i], manual_img03_list[i], manual04_list[i], manual_img04_list[i], manual05_list[i], manual_img05_list[i],
           manual06_list[i], manual_img06_list[i], manual07_list[i], manual_img07_list[i], manual08_list[i], manual_img08_list[i], manual09_list[i], manual_img09_list[i], manual10_list[i], manual_img10_list[i],
           manual11_list[i], manual_img11_list[i], manual12_list[i], manual_img12_list[i], manual13_list[i], manual_img13_list[i], manual14_list[i], manual_img14_list[i], manual15_list[i], manual_img15_list[i],
           manual16_list[i], manual_img16_list[i], manual17_list[i], manual_img17_list[i], manual18_list[i], manual_img18_list[i], manual19_list[i], manual_img19_list[i], manual20_list[i], manual_img20_list[i])

    num = cur.execute(sql, val)
    con.commit()

# for i in range(0, rcp_seq_list.__sizeof__()-1):
#     print(i)
# print(rcp_seq_list.__len__())
# print(rcp_seq_list[999])
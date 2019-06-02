create database bixby;
use bixby;

drop table recipes;

CREATE TABLE recipes (
   RCP_SEQ   int primary key, # 일련번호
   RCP_NM varchar(20), # 메뉴명
   RCP_WAY2 varchar(20), # 조리방법
   RCP_PAT2 varchar(20), # 요리종류
   INFO_ENG int, # 열량
   INFO_CAR int, # 탄수화물
   INFO_PRO int, #   단백질
   INFO_FAT int, #   지방
   INFO_NA   int, # 나트륨
   HASH_TAG varchar(20), #   해쉬태그
   ATT_FILE_NO_MAIN varchar(200), # 이미지경로(소)
   ATT_FILE_NO_MK varchar(200), #   이미지경로(대)
   RCP_PARTS_DTLS varchar(600), #   재료정보
   MANUAL01 varchar(200), #   만드는법_01
   MANUAL_IMG01 varchar(200), #   만드는법_이미지_01
   MANUAL02 varchar(200), #   만드는법_02
   MANUAL_IMG02 varchar(200), #   만드는법_이미지_02
   MANUAL03 varchar(200), #   만드는법_03
   MANUAL_IMG03 varchar(200), #   만드는법_이미지_03
   MANUAL04 varchar(200), #   만드는법_04
   MANUAL_IMG04 varchar(200), #   만드는법_이미지_04
   MANUAL05 varchar(200), #   만드는법_05
   MANUAL_IMG05 varchar(200), #   만드는법_이미지_05
   MANUAL06 varchar(200), #   만드는법_06
   MANUAL_IMG06 varchar(200), #   만드는법_이미지_06
   MANUAL07 varchar(200), #   만드는법_07
   MANUAL_IMG07 varchar(200), #   만드는법_이미지_07
   MANUAL08 varchar(200), #   만드는법_08
   MANUAL_IMG08 varchar(200), #   만드는법_이미지_08
   MANUAL09 varchar(200), #   만드는법_09
   MANUAL_IMG09 varchar(200), #   만드는법_이미지_09
   MANUAL10 varchar(200), #   만드는법_10
   MANUAL_IMG10 varchar(200), #   만드는법_이미지_10
   MANUAL11 varchar(200), #   만드는법_11
   MANUAL_IMG11 varchar(200), #   만드는법_이미지_11
   MANUAL12 varchar(200), #   만드는법_12
   MANUAL_IMG12 varchar(200), #   만드는법_이미지_12
   MANUAL13 varchar(200), #   만드는법_13
   MANUAL_IMG13 varchar(200), #   만드는법_이미지_13
   MANUAL14 varchar(200), #   만드는법_14
   MANUAL_IMG14 varchar(200), #   만드는법_이미지_14
   MANUAL15 varchar(200), #   만드는법_15
   MANUAL_IMG15 varchar(200), #   만드는법_이미지_15
   MANUAL16 varchar(200), #   만드는법_16
   MANUAL_IMG16 varchar(200), #   만드는법_이미지_16
   MANUAL17 varchar(200), #   만드는법_17
   MANUAL_IMG17 varchar(200), #   만드는법_이미지_17
   MANUAL18 varchar(200), #   만드는법_18
   MANUAL_IMG18 varchar(200), #   만드는법_이미지_18
   MANUAL19 varchar(200), #   만드는법_19
   MANUAL_IMG19 varchar(200), #   만드는법_이미지_19
   MANUAL20 varchar(200), #   만드는법_20
   MANUAL_IMG20 varchar(200) #   만드는법_이미지_20
);

select * from recipes;
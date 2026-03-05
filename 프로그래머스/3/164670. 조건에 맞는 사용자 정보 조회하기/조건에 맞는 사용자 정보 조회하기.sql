-- 코드를 입력하세요
# SELECT

# USED_GOODS_BOARD  중고 거래 게시판 정보
# USED_GOODS_USER 중고 거래 게시판 첨부파일 정보
# left(TLNO,3) , '-' ,mid(TLNO,4,4), '-', right(TLNO,4)
select USER_ID,NICKNAME, concat(CITY, ' ' , STREET_ADDRESS1, ' ' , STREET_ADDRESS2)as '전체주소',concat(left(TLNO,3) , '-' ,mid(TLNO,4,4), '-', right(TLNO,4)) as '전화번호' from (select WRITER_ID, count(WRITER_ID) as cnt from USED_GOODS_BOARD group by WRITER_ID having cnt >= 3)a
join 
(select USER_ID,NICKNAME,CITY,STREET_ADDRESS1,STREET_ADDRESS2,TLNO from USED_GOODS_USER) b
on a.writer_id = b.user_id
order by user_id desc
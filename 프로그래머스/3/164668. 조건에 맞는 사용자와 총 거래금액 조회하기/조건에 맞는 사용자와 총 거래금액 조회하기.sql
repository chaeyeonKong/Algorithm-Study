# SELECT a.user_id AS USER_ID, a.nickname, sum(b.price) as total_sales
# from used_goods_user a, used_goods_board b
# where a.user_id = b.writer_id and status='DONE'
# group by b.writer_id
# having sum(b.price)>=700000
# order by total_sales

SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES FROM USED_GOODS_BOARD B INNER JOIN USED_GOODS_USER U 
ON (U.USER_ID = B.WRITER_ID and STATUS='DONE')
GROUP BY B.WRITER_ID
HAVING(TOTAL_SALES>=700000) ORDER BY TOTAL_SALES 
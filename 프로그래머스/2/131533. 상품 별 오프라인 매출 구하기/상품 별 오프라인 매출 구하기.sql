-- 코드를 입력하세요
SELECT product_code, PRICE*K AS SALES FROM (
( SELECT * FROM PRODUCT ) A
 JOIN (SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS K FROM OFFLINE_SALE GROUP BY PRODUCT_ID) B
 ON A.PRODUCT_ID = B.PRODUCT_ID)
 ORDER BY SALES DESC , product_code ASC
 

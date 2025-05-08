-- 코드를 입력하세요
select left(product_code,2) as CATEGORY, count(product_code) as PRODUCTS from product group by CATEGORY;



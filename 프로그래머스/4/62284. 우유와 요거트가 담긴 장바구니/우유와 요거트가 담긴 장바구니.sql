
select distinct a.cart_id from (SELECT * from CART_PRODUCTS where name = 'Milk') a inner join (SELECT * from CART_PRODUCTS where name = 'Yogurt') b on a.cart_id = b.cart_id order by a.cart_id
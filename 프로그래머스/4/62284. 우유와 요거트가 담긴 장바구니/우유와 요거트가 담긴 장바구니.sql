select cart_id from cart_products
group by cart_id
having max(name='Milk') and max(name='Yogurt')
order by cart_id
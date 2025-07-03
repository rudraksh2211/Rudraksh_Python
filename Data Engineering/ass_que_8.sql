SELECT DISTINCT s.customer_id, count(me.product_name), sum(distinct me.price)
FROM   members AS m
JOIN   sales   AS s  ON s.customer_id = m.customer_id
JOIN   menu    AS me ON me.product_id  = s.product_id
WHERE  s.order_date < m.join_date
group by customer_id

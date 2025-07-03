SELECT sub.product_id, sub.co as Count ,m.product_name 
FROM ( SELECT product_id, COUNT(*) AS co FROM sales GROUP BY product_id) AS sub join menu as m
WHERE co = (SELECT MAX(co) FROM (SELECT COUNT(*) AS co FROM sales GROUP BY product_id) AS inner_sub) and sub.product_id=m.product_id;

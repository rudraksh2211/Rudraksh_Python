SELECT customer_id, product_id ,MAX(product_count) AS max_order_count
FROM (
    SELECT customer_id, product_id, COUNT(*) AS product_count
    FROM sales
    GROUP BY customer_id, product_id
) AS sub
GROUP BY customer_id; 
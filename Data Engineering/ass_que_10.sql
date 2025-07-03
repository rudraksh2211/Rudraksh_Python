SELECT 
    s.customer_id,
    SUM(
        CASE
            WHEN s.order_date BETWEEN mbr.join_date AND DATE_ADD(mbr.join_date, INTERVAL 6 DAY)
                THEN price * 2  -- double points in first 7 days
            ELSE price
        END * 10
    ) AS total_points
FROM sales s
JOIN menu mn ON s.product_id = mn.product_id
JOIN members mbr ON s.customer_id = mbr.customer_id
WHERE s.order_date <= '2021-01-31'
  AND s.customer_id IN ('A', 'B')
GROUP BY s.customer_id
ORDER BY s.customer_id;

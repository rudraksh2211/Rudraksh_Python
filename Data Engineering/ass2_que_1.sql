/**/
select count(distinct user_id) from users;
/**/
select count(cookie_id) from users;
/**/
select count(distinct visit_id) from events group by month(event_time); 
/**/ 
select count(distinct event_type) from events group by event_type;
/**/
SELECT COUNT(*) AS total_events,
    SUM(CASE WHEN event_type = 3 THEN 1 ELSE 0 END)  AS type3_events,
    ROUND(
        100.0 * SUM(CASE WHEN event_type = 3 THEN 1 ELSE 0 END) / COUNT(*), 2)  AS pct_type3
FROM events;
/**/
WITH v AS (
  SELECT visit_id,
    MAX(p.page_name = 'checkout' AND ei.event_name = 'view') AS saw_checkout,
    MAX(ei.event_name = 'purchase') AS made_purchase
  FROM events e
  JOIN event_identifier ei ON e.event_type = ei.event_type
  JOIN page_hierarchy p ON e.page_id = p.page_id
  GROUP BY visit_id
) SELECT ROUND(100.0 * SUM(saw_checkout AND NOT made_purchase) / NULLIF(SUM(saw_checkout), 0), 2) AS percent
FROM v;
/**/
SELECT p.page_name, COUNT(*) AS views
FROM events e
JOIN event_identifier ei ON e.event_type = ei.event_type
JOIN page_hierarchy p ON e.page_id = p.page_id
WHERE ei.event_name = 'view'
GROUP BY p.page_name
ORDER BY views DESC
LIMIT 3;
/**/
SELECT p.product_category,
  SUM(ei.event_name = 'view') AS views,
  SUM(ei.event_name = 'cart_add') AS cart_adds
FROM events e
JOIN event_identifier ei ON e.event_type = ei.event_type
JOIN page_hierarchy p ON e.page_id = p.page_id
GROUP BY p.product_category;
/**/
SELECT p.product_id, COUNT(*) AS purchases
FROM events e
JOIN event_identifier ei ON e.event_type = ei.event_type
JOIN page_hierarchy p ON e.page_id = p.page_id
WHERE ei.event_name = 'purchase' AND p.product_id IS NOT NULL
GROUP BY p.product_id
ORDER BY purchases DESC
LIMIT 3;


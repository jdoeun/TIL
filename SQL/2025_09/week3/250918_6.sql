-- solvesql: 온라인 쇼핑몰의 월 별 매출액 집계

SELECT
  DATE_FORMAT(o.order_date, '%Y-%m') AS order_month,
  SUM(CASE WHEN o.order_id NOT LIKE 'C%' THEN oi.price * oi.quantity ELSE 0 END) AS ordered_amount,
  SUM(CASE WHEN o.order_id LIKE 'C%' THEN oi.price * oi.quantity ELSE 0 END) AS canceled_amount,
  SUM(oi.price * oi.quantity) AS total_amount
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY order_month
ORDER BY order_month;

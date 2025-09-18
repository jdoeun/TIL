-- solvesql: 배송 예정일 예측 성공과 실패

select date(order_purchase_timestamp) as purchase_date,
count(case when date(order_delivered_customer_date) < date(order_estimated_delivery_date) then order_id end) as success,
count(case when date(order_delivered_customer_date) >= date(order_estimated_delivery_date) then order_id end) as fail
from olist_orders_dataset
where order_delivered_customer_date is not null
and order_estimated_delivery_date is not null
and (date(order_purchase_timestamp) between '2017-01-01' and '2017-01-31')
group by purchase_date
order by purchase_date;
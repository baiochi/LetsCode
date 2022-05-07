Informações:

SELECT * FROM orders;

SELECT * FROM order_details;

SELECT * FROM products;

SELECT * FROM customers;

-- Em alguns momentos vocês vão usar:

SUM((products.unit_price * order_details.quantity * (1 - order_details.discount))) + AVG(orders.freight) AS total_order_price

-- Em algum momento vocês vão usar:

( SUM((products.unit_price * order_details.quantity * (1 - order_details.discount))) + 
    AVG(orders.freight) ) / COUNT(orders.order_id) as mean_order_price

-- Obtenha uma tabela que contenha o id do pedido e o valor total do mesmo.

SELECT 
	A.order_id,
	SUM((C.unit_price * B.quantity * (1 - B.discount))) + A.freight 
		AS total_order_price
FROM
	orders as A
INNER JOIN
	order_details as B
	ON A.order_id = B.order_id
INNER JOIN
	products as C
	ON B.product_id = C.product_id
GROUP BY A.order_id
ORDER BY 1;

-- Obtenha uma lista dos 10 clientes que realizaram o maior número de pedidos, 
-- bem como o número de pedidos de cada, ordenados em ordem decrescente de nº de pedidos.
SELECT 
	A.customer_id, 
	A.contact_name,
	COUNT(C.quantity) AS numbers_of_orders
FROM
	customers AS A
INNER JOIN
	orders AS B
	ON A.customer_id = B.customer_id
INNER JOIN
	order_details AS C
	ON B.order_id = C.order_id
GROUP BY A.customer_id
ORDER BY 3 DESC
LIMIT 10;
	
-- Obtenha uma tabela que contenha o id e o valor total do pedido e o nome do cliente que o realizou.

SELECT 
	A.order_id,
	D.contact_name,
	ROUND
	(
		(SUM((C.unit_price * B.quantity * (1 - B.discount))) + A.freight)::numeric
	,2) 
		AS total_order_price
FROM
	orders as A
INNER JOIN
	order_details as B
	ON A.order_id = B.order_id
INNER JOIN
	products as C
	ON B.product_id = C.product_id
INNER JOIN
	customers as D
	ON A.customer_id = D.customer_id
GROUP BY A.order_id, D.contact_name
ORDER BY 1;

-- Obtenha uma tabela que contenha o país do cliente e o valor da compra que ele realizou.

SELECT 
	A.order_id,
	D.country,
	ROUND
	(
		(SUM((C.unit_price * B.quantity * (1 - B.discount))) + A.freight)::numeric
	,2) 
		AS total_order_price
FROM
	orders as A
INNER JOIN
	order_details as B
	ON A.order_id = B.order_id
INNER JOIN
	products as C
	ON B.product_id = C.product_id
INNER JOIN
	customers as D
	ON A.customer_id = D.customer_id
GROUP BY A.order_id, D.country
ORDER BY 1;

-- Obtenha uma tabela que contenha uma lista dos países dos clientes e o 
-- valor total de compras realizadas em cada um dos países. 
-- Ordene a tabela, na order descrescente, considerando o valor total de compras realizadas por país.

SELECT 
	D.country AS customer_country,
	ROUND(
		( SUM(C.unit_price * B.quantity * (1 - B.discount)) + 
    	AVG(A.freight)  )::numeric
	,2) AS total_order_price
FROM
	orders as A
INNER JOIN
	order_details as B
	ON A.order_id = B.order_id
INNER JOIN
	products as C
	ON B.product_id = C.product_id
INNER JOIN
	customers as D
	ON A.customer_id = D.customer_id
GROUP BY D.country
ORDER BY 2 DESC;

-- Obtenha uma tabela com o valor médio das vendas em cada mês 
-- (ordenados do mês com mais vendas para o mês com menos vendas)

SELECT 
	DATE_PART('month',A.order_date),
	ROUND(
		( SUM(C.unit_price * B.quantity * (1 - B.discount)) + 
    	AVG(A.freight) / COUNT(A.order_id) )::numeric
	,2) AS mean_order_price
FROM
	orders as A
INNER JOIN
	order_details as B
	ON A.order_id = B.order_id
INNER JOIN
	products as C
	ON B.product_id = C.product_id
INNER JOIN
	customers as D
	ON A.customer_id = D.customer_id
GROUP BY DATE_PART('month',A.order_date)
ORDER BY 2 DESC;

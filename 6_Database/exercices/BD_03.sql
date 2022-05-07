-- ORDERS table:

SELECT * FROM orders

-- 1) Liste o top 3 de funcionários com mais vendas no primeiro trimestre de 1996.

-- Top 3 employees of 1996
SELECT employee_id, COUNT(employee_id) as number_of_sales
FROM orders
WHERE order_date BETWEEN '1996-01-01' AND '1996-12-31' -- there is no records before 1996-07-04
GROUP BY employee_id
LIMIT 3;

-- 2) Liste os clientes com mais pedidos - mas somente aqueles que tiverem a partir de 2 pedidos. 
-- Corte explicitamente os clientes que compraram de funcionários sem ID.  

SELECT 	
	customer_id, 
	COUNT(customer_id) as orders_count
FROM 	orders
WHERE 	employee_id IS NOT null
GROUP BY 
	customer_id
HAVING 	
	COUNT(customer_id) > 2
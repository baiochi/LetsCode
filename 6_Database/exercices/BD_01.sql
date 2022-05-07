-- CUSTOMERS table
--1) Gere uma relação com os nomes dos clientes, suas cidades e países, em ordem alfabética de nome.

SELECT 	 contact_name, city, country
FROM 	 customers
ORDER BY contact_name

--2) Na relação do item (1), filtre pelos clientes da Alemanha, da França e da Espanha, 
--excluindo-se os clientes que vivem nas capitais destes países.

SELECT 	contact_name, city, country
FROM 	customers
WHERE 	country IN ('Germany','France','Spain') 
		AND 
	   	city NOT IN ('Berlin','Paris','Madrid')
ORDER BY contact_name

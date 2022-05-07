--PRODUCTS table

SELECT * FROM products

-- 1) Quantos são os produtos que são da CategoryID 2?

SELECT COUNT(*) AS "categoryid_2_count"
FROM products
WHERE category_id = 2;

-- 2) Quantos produtos com SupplierID idêntico ao CategoryID e que custam mais do que 10?

SELECT COUNT(DISTINCT product_name) 
FROM 	products
WHERE 	supplier_id = category_id 
	AND
		unit_price > 10;

-- 3) Liste todos os nomes de produtos, suas *"Units"* e seus respectivos preços distintos 
-- que pertecem às categorias 1, 2 e 7.

-- columns with the word unit
SELECT 	COLUMN_NAME
FROM 	INFORMATION_SCHEMA.COLUMNS
WHERE 	table_name =  'products'
	AND 
		column_name LIKE '%unit%';

-- query
SELECT 	product_name, unit_price, units_in_stock, 
		units_on_order, quantity_per_unit 
FROM 	products
WHERE 	category_id in (1,2,7);

-- 4) Liste os 5 primeiros nomes de produtos que começam com "A" ou tenham "h" no meio do nome. 
-- Retorne em português os nomes das colunas.

SELECT 	product_name AS "Nome_do_produto"
FROM 	products
WHERE 	product_name LIKE 'A%' 
	OR 
		product_name LIKE '%h%'
LIMIT 5;

-- 5) Dê a média de preços de todos os produtos das categorias entre 1 e 5. 
-- Arredonde para 1 casa decimal.

SELECT 	category_id, ROUND(AVG(unit_price)::numeric, 1)
FROM 	products
WHERE 	category_id BETWEEN 1 AND 5
GROUP BY
		category_id;

-- 6) Liste a média de preços e a quantidade de produtos distintos por SupplierID; 
-- ordene pela média de preço, do maior para o menor, e só mostre os 5 primeiros.

SELECT 
	supplier_id,
	ROUND(AVG(unit_price)::numeric, 2) AS "unit_price_mean",
	COUNT(supplier_id)
FROM 	 products
GROUP BY supplier_id
ORDER BY unit_price_mean DESC
LIMIT 5;
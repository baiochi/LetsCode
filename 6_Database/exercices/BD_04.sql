-- SUPPLIERS table:

/*
1) Conte todos os diferentes fornecedores por país. 
Agrupe categorizando os países em 'Americas' (se o país for USA, Brazil ou Canada) e 'Outros' senão. 
Detalhe, estamos buscando aqueles cujo DDD não comece com o dígito 1.
*/

-- create temp table of supplier_id and country, remove countries with DDD starting with 1
CREATE TEMP TABLE IF NOT EXISTS continents AS
	SELECT 	supplier_id, country
	FROM 	suppliers
	WHERE 	suppliers.phone NOT LIKE '(1%';
-- change 'USA','Brazil','Canada' to 'America'
UPDATE continents
SET country = 'America'
WHERE country IN ('USA','Brazil','Canada')
-- change every other country to 'Others'
UPDATE continents
SET country = 'Others'
WHERE country NOT IN ('USA','Brazil','Canada')

SELECT * FROM continents

-- Number of suppliers per continent
SELECT 	 
	country, 
	COUNT(supplier_id) as number_of_suppliers
FROM 
	continents
GROUP BY 
	country

-- 2) Existe alguma cidade com mais de um código de área de telefone?

-- complete relation city/phone; count = 29
SELECT city, phone
FROM suppliers;

-- only phone codes, exclude where phone is null; count = 
WITH phone_codes_table AS
(
   	SELECT 	city,
			SUBSTRING (phone, '(\([0-9]{1,3}\))') AS phone_code
	FROM suppliers
)
SELECT 	 *
FROM 	 phone_codes_table
WHERE 	 phone_code IS NOT null

-- check if there is a city with more than 2 phone codes
WITH phone_codes_table AS
(
   	SELECT 	city,
			SUBSTRING (phone, '(\([0-9]{1,3}\))') AS phone_code
	FROM suppliers
)
SELECT 	 city, COUNT(phone_code) AS code_count
FROM 	 phone_codes_table
WHERE 	 phone_code IS NOT null
GROUP BY city
HAVING 	 COUNT(phone_code) > 2

-- There is no city with more than 2 phone codes

-- 3) Tome a primeira letra de cada cidade (ex. "N" para "New Orleans"). 
-- Quais são as 5 iniciais de nomes de cidades que têm mais fornecedores associados (em ordem descrescente de fornecedores/cidade)?

SELECT SUBSTRING (city, 1, 1), COUNT(supplier_id)
FROM suppliers
GROUP BY SUBSTRING (city, 1, 1)
ORDER BY COUNT(supplier_id) DESC
LIMIT 5;


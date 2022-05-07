
CREATE TABLE cliente 
(
  cod_cli SERIAL PRIMARY KEY,
  nome_cli varchar(255) default NULL,
  endereco varchar(255) default NULL,
  cidade varchar(255),
  cep varchar(20) default NULL,
  uf varchar(50) default NULL
);

CREATE TABLE vendedor 
(
  cod_vend SERIAL PRIMARY KEY,
  nome_vend varchar(255) default NULL,
  sal_fixo varchar(100) default NULL,
  faixa_comiss integer NULL
);

CREATE TABLE produto 
(
  cod_prod INTEGER PRIMARY KEY,
  unid_prod integer NULL,
  desc_prod varchar(255) default NULL,
  val_unit varchar(100) default NULL
);

CREATE TABLE pedido 
(
  cod_ped SERIAL PRIMARY KEY,
  prazo_entr time,
  cod_cli integer NULL,
  cod_vend integer NULL,
  FOREIGN KEY (cod_cli) REFERENCES cliente (cod_cli),
  FOREIGN KEY (cod_vend) REFERENCES vendedor (cod_vend)
	
);

CREATE TABLE item_pedido 
(
  cod_item_ped INTEGER PRIMARY KEY,
  cod_ped integer NULL,
  cod_prod integer NULL,
  qtd_ped integer NULL,
  FOREIGN KEY (cod_ped) REFERENCES pedido (cod_ped),
  FOREIGN KEY (cod_prod) REFERENCES produto (cod_prod)
);


-- Selecione todos os clientes que começam com a letra 'A'.

SELECT * 
FROM cliente
WHERE nome_cli LIKE 'A%'

--Selecione todos os vendedores que tem salario maio que R$5.000,00

SELECT *
FROM vendedor
WHERE sal_fixo > 5000

--Selecione todos os pedidos onde a quantidade de produto seja maior que 3.

SELECT 
	A.cod_ped,
	COUNT(B.qtd_ped)
FROM 
	pedido as A
LEFT JOIN item_pedido as B ON
	A.cod_ped = B.cod_ped
GROUP BY A.cod_ped
HAVING SUM(B.qtd_ped) > 3

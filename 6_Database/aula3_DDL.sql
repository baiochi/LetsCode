CREATE DATABASE letsflix;

CREATE TABLE tb_filme (
	id_filme SERIAL PRIMARY KEY,
	cod_filme INTEGER NOT NULL,
	nome VARCHAR(255) NOT NULL,
	nota INTEGER,
	bilheteria INTEGER,
	id_genero INTEGER NOT NULL,
	FOREIGN KEY (id_genero)
		REFERENCES tb_genero (id_genero)
);

CREATE TABLE tb_genero (
	id_genero SERIAL PRIMARY KEY,
	classificacao VARCHAR NOT NULL,
	nome VARCHAR NOT NULL	
);
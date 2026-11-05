CREATE DATABASE loja;
USE loja;

-- Remover a tabela caso já exista
DROP TABLE IF EXISTS produtos;

-- Criar a tabela de produtos-
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL,
    cidade TEXT NOT NULL
);

-- Inserir os produtos
INSERT INTO produtos
(nome, categoria, preco, estoque, cidade)
VALUES
('Mouse Gamer', 'Perifericos', 89.90, 15, 'Belo Horizonte'),
('Teclado Mecanico', 'Perifericos', 249.90, 8, 'Belo Horizonte'),
('Monitor 24', 'Monitores', 899.00, 5, 'Contagem'),
('Monitor 27', 'Monitores', 1399.00, 0, 'Belo Horizonte'),
('SSD 480GB', 'Armazenamento', 299.90, 12, 'Betim'),
('SSD 1TB', 'Armazenamento', 499.90, 4, 'Belo Horizonte'),
('Roteador Wi-Fi', 'Redes', 329.90, 10, 'Contagem'),
('Cabo de Rede 5m', 'Redes', 29.90, 30, 'Belo Horizonte'),
('Mouse Sem Fio', 'Perifericos', 119.90, 0, 'Betim'),
('Suporte para Monitor', 'Acessorios', 79.90, 18, 'Belo Horizonte'),
('Headset USB', 'Perifericos', 189.90, 6, 'Contagem'),
('Hub USB', 'Acessorios', 69.90, 20, 'Betim'),
('Webcam Full HD', 'Perifericos', 219.90, 9, 'Belo Horizonte'),
('SSD Externo 1TB', 'Armazenamento', 599.90, 2, 'Contagem');

-- Conferir os registros
SELECT * FROM produtos ORDER BY preco ASC;
SELECT * FROM produtos ORDER BY preco DESC;

SELECT nome, preco FROM produtos ORDER BY preco ASC;

SELECT nome, categoria, preco
FROM produtos;
-- ORDER BY categoria ASC, preco DESC;

SELECT DISTINCT categoria FROM produtos;
SELECT COUNT(DISTINCT categoria) FROM produtos;

SELECT categoria, nome, preco FROM produtos where preco <= 200  ;

SELECT nome, preco FROM produtos where categoria= "Redes" OR  categoria = "Monitores";

SELECT nome, categoria FROM produtos WHERE categoria IN ("Monitor", "Redes");

SELECT * FROM produtos WHERE preco < 700 AND preco > 200;

SELECT * FROM produtos WHERE preco BETWEEN 200 AND 700;

SELECT * FROM produtos WHERE categoria IN ("perifericos","acessorios") AND preco BETWEEN 100 AND 1000;

SELECT * FROM produtos WHERE nome LIKE 'SSD%';

SELECT * FROM produtos WHERE nome LIKE '1%tb';

SELECT * FROM produtos WHERE nome LIKE '%SSD%';

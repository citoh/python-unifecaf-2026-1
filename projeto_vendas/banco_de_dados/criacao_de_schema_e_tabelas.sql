CREATE DATABASE IF NOT EXISTS projeto_vendas_eletronicos_unifecaf;
USE projeto_vendas_eletronicos_unifecaf;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100),
    preco DECIMAL(10,2)
);

CREATE TABLE vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_vendedor INT,
    data_e_hora DATETIME,
    desconto DECIMAL(10,2),
    valor_final DECIMAL(10,2),
    FOREIGN KEY (id_vendedor) REFERENCES vendedores(id)
);

CREATE TABLE vendas_produtos (
    id_venda INT,
    id_produto INT,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10,2) NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_venda, id_produto),
    FOREIGN KEY (id_venda) REFERENCES vendas(id),
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
);
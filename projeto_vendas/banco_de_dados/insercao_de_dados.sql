-- VENDEDORES
INSERT INTO vendedores (nome) VALUES
('Carlos Silva'),
('Ana Souza'),
('João Pereira'),
('Mariana Lima');


-- PRODUTOS
INSERT INTO produtos (descricao, preco) VALUES
('Smartphone Samsung', 1500.00),
('Smartphone Motorola', 1200.00),
('iPhone 13', 5000.00),
('Notebook Dell', 3500.00),
('Notebook Lenovo', 3200.00),
('Mouse Logitech', 80.00),
('Teclado Mecânico', 250.00),
('Monitor LG 24"', 900.00),
('Monitor Samsung 27"', 1200.00),
('Headset Gamer', 300.00),
('Caixa de Som JBL', 400.00),
('Smart TV 50"', 2800.00),
('Smart TV 65"', 4500.00),
('HD Externo 1TB', 350.00),
('SSD 512GB', 450.00),
('Pen Drive 64GB', 60.00),
('Carregador USB-C', 90.00),
('Cabo HDMI', 40.00),
('Webcam HD', 200.00),
('Roteador Wi-Fi', 250.00),
('Tablet Samsung', 1800.00),
('Tablet Apple', 4200.00),
('Impressora HP', 700.00),
('Impressora Epson', 800.00),
('Drone DJI', 6000.00),
('Câmera Canon', 3500.00),
('Câmera Nikon', 3300.00),
('Tripé', 150.00),
('Microfone USB', 300.00),
('Placa de Vídeo RTX 3060', 2500.00),
('Placa de Vídeo RTX 4070', 4500.00),
('Fonte 600W', 350.00),
('Gabinete Gamer', 500.00),
('Cooler RGB', 120.00),
('Memória RAM 8GB', 200.00),
('Memória RAM 16GB', 350.00),
('Processador Intel i5', 1200.00),
('Processador AMD Ryzen 5', 1100.00),
('Placa Mãe ASUS', 900.00),
('Placa Mãe Gigabyte', 850.00),
('Controle Xbox', 350.00),
('Controle PS5', 400.00),
('Console Xbox Series S', 2500.00),
('Console PS5', 4500.00),
('Fone Bluetooth', 200.00),
('Relógio Smartwatch', 600.00),
('Bateria Portátil', 150.00),
('Suporte para Notebook', 100.00),
('Luminária LED', 80.00),
('Teclado Sem Fio', 180.00);


-- VENDAS
INSERT INTO vendas (id_vendedor, data_e_hora, desconto, valor_final) VALUES
-- Janeiro
(1, '2026-01-05 10:15:00', 50.00, 1690.00),
(2, '2026-01-10 14:30:00', 0.00, 3900.00),
(3, '2026-01-15 09:45:00', 30.00, 1550.00),
(4, '2026-01-20 16:00:00', 0.00, 1800.00),
(1, '2026-01-25 11:20:00', 20.00, 1460.00),
-- Fevereiro
(2, '2026-02-03 13:10:00', 0.00, 3200.00),
(3, '2026-02-08 15:50:00', 40.00, 580.00),
(4, '2026-02-12 08:30:00', 0.00, 1400.00),
(1, '2026-02-18 17:25:00', 10.00, 890.00),
(2, '2026-02-25 12:40:00', 0.00, 1500.00);


-- VENDAS PRODUTOS
INSERT INTO vendas_produtos 
(id_venda, id_produto, quantidade, valor_unitario, valor_total) 
VALUES
-- Venda 1
(1, 1, 1, 1500.00, 1500.00),
(1, 6, 3, 80.00, 240.00),
-- Venda 2
(2, 4, 1, 3500.00, 3500.00),
(2, 35, 2, 200.00, 400.00),
-- Venda 3
(3, 2, 1, 1200.00, 1200.00),
(3, 16, 3, 60.00, 180.00),
(3, 17, 2, 90.00, 180.00),
(3, 18, 1, 40.00, 40.00),
-- Venda 4
(4, 8, 2, 900.00, 1800.00),
-- Venda 5
(5, 10, 2, 300.00, 600.00),
(5, 11, 2, 400.00, 800.00),
(5, 34, 4, 120.00, 480.00),
-- Venda 6
(6, 43, 1, 2500.00, 2500.00),
(6, 41, 2, 350.00, 700.00),
-- Venda 7
(7, 14, 1, 350.00, 350.00),
(7, 17, 3, 90.00, 270.00),
-- Venda 8
(8, 23, 2, 700.00, 1400.00),
-- Venda 9
(9, 29, 2, 300.00, 600.00),
(9, 47, 2, 150.00, 300.00),
-- Venda 10
(10, 10, 5, 300.00, 1500.00);
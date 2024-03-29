INSERT INTO `truckpad`.`motoristas` (`motoristas_cnh`, `motoristas_nome`, `motoristas_nascimento`, `motoristas_sexo`, `tipo_cnh`, `motoristas_possui_veiculo`)
VALUES ('12345601', 'Arnaldo Cesar Coelho', '1983-12-02', 'M', 4, 'S'), 
('12345602', 'Livia Martins', '2000-05-14', 'F', 4, 'S'), 
('12345603', 'Tamara Marques', '1970-01-17', 'F', 8, 'S'),
('12345604', 'João da Silva Castro', '1988-07-20', 'M', 4, 'S'),
('12345605', 'Paulo Cesar Rodrigues', '1986-04-01', 'M', 4, 'N'),
('12345606', 'Juliano Amaral', '1978-09-29', 'M', 9, 'S'),
('12345607', 'Bete Figueiredo', '1980-02-27', 'F', 4, 'S'),
('12345608', 'Dagmar França', '1988-12-02', 'F', 8, 'N'),
('12345609', 'Juarez Delgado', '1994-10-02', 'M', 8, 'S'),
('12345610', 'Marcos Sobrinho', '2000-02-07', 'M', 8, 'S'),
('12345611', 'Fernando Souza', '1996-07-12', 'M', 4, 'N'),
('12345612', 'kleber Costa', '1975-04-22', 'M', 4, 'S'),
('12345613', 'Adriana Arruda', '1980-04-29', 'F', 9, 'S'),
('12345614', 'Fernando de Paula', '1988-08-12', 'M', 4, 'N'),
('12345615', 'Paulo Andrade', '1992-12-11', 'M', 4, 'S'),
('12345616', 'Cristiano Silva Bueno', '1995-10-08', 'M', 9, 'S'),
('12345617', 'Nathália Amaral Silva', '2000-11-01', 'f', 4, 'S'),
('12345618', 'Carlos Eduardo', '1997-12-22', 'M', 4, 'S'),
('12345619', 'Fernando Perasolo', '1990-06-21', 'M', 8, 'N'),
('12345620', 'Emerson Lopes', '1995-05-17', 'M', 4, 'S'),
('12345621', 'Marcel Nakatu', '1975-05-06', 'M', 4, 'N'),
('12345622', 'Clayton Beraldi', '1980-01-01', 'M', 4, 'S'),
('12345623', 'Suzana Costa', '1984-02-28', 'F', 9, 'N'),
('12345624', 'Henrique Beltrão', '1997-09-15', 'M', 4, 'N'),
('12345625', 'Rafael Costa', '1978-11-11', 'M', 4, 'N'),
('12345626', 'Paulo Cândido', '1993-12-25', 'M', 8, 'N'),
('12345627', 'Geraldo Alves', '1989-04-16', 'M', 4, 'S'),
('12345628', 'Wilson Silveira', '2001-03-05', 'M', 4, 'S'),
('12345629', 'Julio Castro Marques', '2000-12-02', 'M', 4, 'N'),
('12345630', 'Consuelo Costa', '1988-06-03', 'F', 4, 'N'),
('12345631', 'Agostinho Silva', '1986-07-09', 'M', 4, 'S'),
('12345632', 'Fábio Nobre', '1975-12-10', 'M', 4, 'S'),
('12345633', 'Erick Souza', '1978-01-12', 'M', 4, 'S'),
('12345634', 'Ragnar Ragnarson', '1982-04-02', 'M', 4, 'N'),
('12345635', 'Silvio Santos', '1995-07-02', 'M', 4, 'S'),
('12345636', 'Alberto Santos', '1999-12-07', 'M', 9, 'S'),
('12345637', 'Júlio Trindade', '1989-11-25', 'M', 4, 'S'),
('12345638', 'Sirlei Silva', '1970-10-28', 'M', 4, 'S'),
('12345639', 'Rogério Alves Nogueira', '2001-01-31', 'M', 8, 'N');

INSERT INTO `truckpad`.`trajetos` (`motoristas_id`, `trajetos_data`, `tipo_caminhao`, `trajetos_esta_carregado`,
`trajetos_origem`, `trajetos_lat_origem`, `trajetos_lng_origem`, `trajetos_destino`, `trajetos_lat_destino`, `trajetos_lng_destino`, 
`trajetos_origem_google`, `trajetos_destino_google`)
VALUES
(1, '2019-07-29', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(2, '2019-07-29', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(3, '2019-07-29', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(4, '2019-07-30', 2, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(5, '2019-07-31', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(6, '2019-08-02', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(7, '2019-08-03', 3, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(8, '2019-08-03', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(9, '2019-08-04', 5, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(10, '2019-08-05', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(11, '2019-08-05', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(12, '2019-08-06', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(13, '2019-08-07', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(2, '2019-08-07', 1, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(14, '2019-08-07', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(16, '2019-08-09', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(15, '2019-08-10', 4, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(17, '2019-08-13', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(18, '2019-08-14', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(4, '2019-08-14', 1, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(19, '2019-08-15', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(20, '2019-08-17', 4, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(21, '2019-08-20', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(22, '2019-08-20', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(23, '2019-08-20', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(24, '2019-08-21', 1, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(25, '2019-08-22', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(19, '2019-08-23', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(26, '2019-08-23', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(27, '2019-08-25', 5, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(28, '2019-08-25', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(29, '2019-08-25', 2, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(30, '2019-08-25', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(31, '2019-08-26', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(29, '2019-08-26', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(31, '2019-08-27', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(34, '2019-08-27', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(35, '2019-08-27', 2, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(17, '2019-08-28', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(32, '2019-08-29', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(33, '2019-08-29', 3, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(36, '2019-08-29', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(37, '2019-08-30', 4, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(35, '2019-08-31', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(17, '2019-08-31', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(38, '2019-09-01', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(1, '2019-09-01', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(2, '2019-09-01', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(37, '2019-09-01', 1, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(39, '2019-09-01', 4, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(27, '2019-09-02', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(10, '2019-09-02', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(36, '2019-09-02', 5, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(21, '2019-09-02', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(28, '2019-09-02', 1, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(1, '2019-09-03', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(3, '2019-09-03', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(5, '2019-09-03', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(39, '2019-09-03', 3, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(26, '2019-09-03', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(38, '2019-09-03', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(39, '2019-09-03', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(15, '2019-09-04', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(39, '2019-09-04', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(5, '2019-09-04', 1, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(12, '2019-09-04', 3, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(19, '2019-09-04', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(18, '2019-09-04', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(7, '2019-09-04', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(37, '2019-09-04', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(36, '2019-09-04', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(12, '2019-09-05', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(38, '2019-09-05', 4, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(17, '2019-09-05', 2, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(28, '2019-09-05', 3, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(1, '2019-09-05', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Centralina, 83', '-23.543446', '-46.4157954', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Centralina, 83 - Vila Princesa Isabel, São Paulo - SP, 08410-100, Brasil'),
(5, '2019-09-05', 2, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'Av. Paulista, 500', '-23.5678355', '-46.6480931', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'Av. Paulista, 500 - Bela Vista, São Paulo - SP, 01310-000, Brasil'),
(21, '2019-09-05', 5, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(13, '2019-09-05', 1, 'N', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil'),
(7, '2019-09-05', 1, 'S', 'Av. Paulo Faccini, 500', '-23.4666242', '-46.5238773', 'R. Canadá, 765', '-23.5746751', '-46.6702036', 'Av. Paulo Faccini, 500 - Macedo, Guarulhos - SP, 07111-003, Brasil', 'R. Canadá, 765 - Jardim America, São Paulo - SP, Brasil');

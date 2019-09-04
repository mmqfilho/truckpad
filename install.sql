CREATE DATABASE `truckpad` /*!40100 DEFAULT CHARACTER SET latin1 */;

CREATE TABLE `tipo_caminhao` (
  `tipo_caminhao_id` int(2) NOT NULL AUTO_INCREMENT,
  `tipo_caminhao_nome` varchar(45) NOT NULL,
  PRIMARY KEY (`tipo_caminhao_id`),
  UNIQUE KEY `tipo_caminhao_nome_UNIQUE` (`tipo_caminhao_nome`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `tipo_cnh` (
  `tipo_cnh_id` int(2) NOT NULL AUTO_INCREMENT,
  `tipo_cnh_nome` varchar(2) NOT NULL,
  PRIMARY KEY (`tipo_cnh_id`),
  UNIQUE KEY `tipo_cnh_nome_UNIQUE` (`tipo_cnh_nome`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `motoristas` (
  `motoristas_id` int(10) NOT NULL AUTO_INCREMENT,
  `motoristas_cnh` varchar(45) NOT NULL,
  `motoristas_nome` varchar(100) NOT NULL,
  `motoristas_nascimento` date NOT NULL,
  `motoristas_sexo` enum('M','F') DEFAULT 'M',
  `tipo_cnh` int(2) NOT NULL,
  `motoristas_possui_veiculo` enum('S','N') NOT NULL DEFAULT 'N',
  PRIMARY KEY (`motoristas_id`),
  UNIQUE KEY `motoristas_cnh_UNIQUE` (`motoristas_cnh`),
  KEY `fk_mot_tipo_cnh_idx` (`tipo_cnh`),
  CONSTRAINT `fk_mot_tipo_cnh` FOREIGN KEY (`tipo_cnh`) REFERENCES `tipo_cnh` (`tipo_cnh_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

CREATE TABLE `trajetos` (
  `trajetos_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `motoristas_id` int(10) NOT NULL,
  `trajetos_data` date NOT NULL,
  `tipo_caminhao` int(2) NOT NULL,
  `trajetos_esta_carregado` enum('S','N') DEFAULT 'N',
  `trajetos_lat_origem` varchar(200) NOT NULL,
  `trajetos_lng_origem` varchar(200) NOT NULL,
  `trajetos_lat_destino` varchar(200) NOT NULL,
  `trajetos_lng_destino` varchar(200) NOT NULL,
  PRIMARY KEY (`trajetos_id`),
  KEY `fk_traj_mot_idx` (`motoristas_id`),
  KEY `fk_traj_tipo_cam_idx` (`tipo_caminhao`),
  CONSTRAINT `fk_traj_mot` FOREIGN KEY (`motoristas_id`) REFERENCES `motoristas` (`motoristas_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_traj_tipo_cam` FOREIGN KEY (`tipo_caminhao`) REFERENCES `tipo_caminhao` (`tipo_caminhao_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `truckpad`.`tipo_caminhao` (`tipo_caminhao_nome`)
VALUES ('Caminhão 3/4'), ('Caminhão Toco'), ('Caminhão Truck'), ('Carreta Simples'), ('Carreta Eixo Extendido');

INSERT INTO `truckpad`.`tipo_cnh` (`tipo_cnh_nome`)
VALUES ('A'), ('B'), ('C'), ('D'), ('E'), ('AB'), ('AC'), ('AD'), ('AE');

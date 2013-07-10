/*DROP TABLE IF EXISTS `microsdtest`;*/
CREATE TABLE IF NOT EXISTS  `microsdtest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `field1` varchar(255) DEFAULT NULL,
  `field2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `microsdtest` WRITE;

INSERT INTO `microsdtest` (field1,field2) VALUES 
('Field 1 Record 1','Field 2 Record 1'),
('Field 1 Record 2','Field 2 Record 2'),
('Field 1 Record 3','Field 2 Record 3'),
('Field 1 Record 4','Field 2 Record 4');

UNLOCK TABLES;

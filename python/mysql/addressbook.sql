/*DROP TABLE IF EXISTS `addressbook`;*/
CREATE TABLE `addressbook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `website` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `addressbook` WRITE;

INSERT INTO `addressbook` VALUES 
(1,'Acme Systems srl','+39 (06) 99-12-187','www.acmesystems.it'),
(2,'Atmel Corporate','+1 (408) 441-0311','www.atmel.com'),
(3,'Digikey','+1 (800) 344-4539','www.digikey.com');

UNLOCK TABLES;

INSERT INTO `user` (`name`, `coin`, `coinDate`, `userType`) VALUES ('蓝色古神', NULL, NULL, '2');
INSERT INTO `battle` (`level`, `hp`, `experience`, `attack`, `defense`, `head`, `body`, `weapon`, `userId`, `maxhp`, `profession`) VALUES ('15', '40000', '0', '250', '200', '5', '7', '6', '112', '40000', '14');

INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '112', '9');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '112', '10');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '112', '11');


DROP TABLE IF EXISTS `activeboss`;
CREATE TABLE `activeboss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activeBossId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

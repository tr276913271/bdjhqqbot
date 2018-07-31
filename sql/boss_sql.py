INSERT INTO `user` (`name`, `coin`, `coinDate`, `userType`) VALUES ('铁甲豆豆', NULL, NULL, '2');
update equipment set etype = 2 where id in (1,2,3);
INSERT INTO `equipment` (`desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('先古勇者留下的头盔，带上以后可以变身为萌妹子', '勇者之盔', '1', '800', '0', '1', '800');
INSERT INTO `equipment` (`desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('流浪剑客这下牛b了', '勇者之剑', '2', '0', '300', '1', '800');
INSERT INTO `equipment` (`desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('先古勇者留下的护甲，穿上以后可以有大屌', '勇者之甲', '3', '0', '300', '1', '800');
INSERT INTO `equipment` (`desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('','小金砖', '2', '0', '0', '2', '1500');

INSERT INTO `equipment` (`desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('', '豆豆之盔', '1', '0', '275', '2', '1000');
INSERT INTO `equipment` (`desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('', '豆豆之剑', '2', '650', '0', '2', '1000');
INSERT INTO `equipment` (`desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('', '豆豆之甲', '3', '0', '275', '2', '1000');

INSERT INTO `battle` (`level`, `hp`, `experience`, `attack`, `defense`, `head`, `body`, `weapon`, `userId`, `maxhp`, `profession`) VALUES ('20', '100000', '0', '250', '200', '18', '20', '19', '113', '100000', '14');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '113', '14');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '113', '15');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '113', '16');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '113', '17');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '113', '17');
INSERT INTO `package` ( `userId`, `equipId`) VALUES ( '113', '17');
update activeboss set activeBossId = 113


DROP TABLE IF EXISTS `activeboss`;
CREATE TABLE `activeboss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activeBossId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

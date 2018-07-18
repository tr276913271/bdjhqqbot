
CREATE TABLE `package` (
`id`  int UNSIGNED NOT NULL AUTO_INCREMENT ,
`userId`  int NULL ,
`equipId`  int NULL ,
PRIMARY KEY (`id`)
);
INSERT package(userId,equipId) SELECT userId,1 from battle;
INSERT package(userId,equipId) SELECT userId,2 from battle;
INSERT package(userId,equipId) SELECT userId,3 from battle;

ALTER TABLE `equipment`
ADD COLUMN `etype`  int NULL AFTER `defense`,
ADD COLUMN `price`  int NULL AFTER `etype`;
update equipment set etype = 1,price=100
INSERT INTO `equipment` (`id`, `desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('5', NULL, '世界BOSS头盔', '1', '0', '100', '2', '100');
INSERT INTO `equipment` (`id`, `desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('6', NULL, '世界BOSS巨斧', '2', '250', '0', '2', '100');
INSERT INTO `equipment` (`id`, `desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('7', NULL, '世界BOSS护胸', '3', '0', '100', '2', '100');
INSERT INTO `equipment` (`id`, `desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('8', NULL, '翠翠熊的左爪（伪）', '2', '350', '0', '1', '300');
INSERT INTO `equipment` (`id`, `desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('9', NULL, '折子的裤袜（伪）', '3', '0', '150', '1', '300');
INSERT INTO `equipment` (`id`, `desc`, `name`, `type`, `attack`, `defense`, `etype`, `price`) VALUES ('10', 'deep dark fantasy', '牙医的黑暗面具（伪）', '1', '0', '150', '1', '300');

INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('16', '14', '世界BOSS', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('18', '1', '可卖装备', '装备类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('19', '2', '不可卖装备', '装备类型');

CREATE TABLE `dps` (
`id`  int NOT NULL AUTO_INCREMENT ,
`damage`  int NULL ,
`userId`  int NULL ,
`bossId`  int NULL ,
PRIMARY KEY (`id`)
);


INSERT INTO `user` (`id`, `name`, `coin`, `coinDate`, `userType`) VALUES ('100', '牙医的暗面', '0', NULL, '2');
INSERT INTO `package` (`userId`, `equipId`) VALUES ('100', '8');
INSERT INTO `package` (`userId`, `equipId`) VALUES ('100', '9');
INSERT INTO `package` (`userId`, `equipId`) VALUES ('100', '10');
INSERT INTO `battle` (`level`, `hp`, `experience`, `attack`, `defense`, `head`, `body`, `weapon`, `userId`, `maxhp`, `profession`) VALUES ('100', '40000', '0', '250', '200', '5', '7', '6', '100', '40000', '14');

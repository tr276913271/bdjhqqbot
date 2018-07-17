ALTER TABLE `battle`
ADD COLUMN `maxhp`  int NULL AFTER `userId`,
ADD COLUMN `profession`  int NULL AFTER `maxhp`;

ALTER TABLE `user`
ADD COLUMN `userType`  int NULL AFTER `coinDate`;
ALTER TABLE `user`
MODIFY COLUMN `userType`  int(11) NULL DEFAULT 1 AFTER `coinDate`;

CREATE TABLE `response` (
`id`  int UNSIGNED NOT NULL AUTO_INCREMENT ,
`keyWord`  varchar(120) NULL ,
`returnWord`  varchar(120) NULL ,
`responseType`  int NULL ,
PRIMARY KEY (`id`)
);

CREATE TABLE `action` (
`id`  int UNSIGNED NOT NULL AUTO_INCREMENT ,
`actionType`  int NULL ,
`actionDate`  date NULL ,
`actionDateTime`  datetime NULL ,
PRIMARY KEY (`id`)
);

CREATE TABLE `code` (
`id`  int UNSIGNED NOT NULL AUTO_INCREMENT ,
`code`  int NULL ,
`codeName`  varchar(40) NULL ,
`codeType`  varchar(40) NULL ,
PRIMARY KEY (`id`)
);

update `user` set userType=1;
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('1', '1', '普通用户', '用户类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('2', '2', '世界BOSS', '用户类型');


INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('3', '1', '新兵', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('4', '2', '战士', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('5', '3', '法师', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('6', '4', '牧师', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('7', '5', '盗贼', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('8', '6', '圣骑士', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('9', '7', '萨满祭司', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('10', '8', '德鲁伊', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('11', '9', '术士', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('12', '10', '武僧', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('13', '11', '死亡骑士', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('14', '12', '猎人', '职业类型');
INSERT INTO `code` (`id`, `code`, `codeName`, `codeType`) VALUES ('15', '13', '恶魔猎手', '职业类型');

update equipment set attack = 250 where name="破旧的剑";
update equipment set defense = 100 where name="新手头盔";
update equipment set defense = 100 where name="新手胸甲";
update equipment set attack = 300 where name="青铜剑";
update battle set hp=1000 ,maxhp=1000 ;

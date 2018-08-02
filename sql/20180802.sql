CREATE TABLE `bank` (
`id`  int NOT NULL AUTO_INCREMENT ,
`userId`  int NULL ,
`money`  int NULL ,
`maxMoney`  int NULL ,
`bankType`  int NULL ,
PRIMARY KEY (`id`)
);


CREATE TABLE `collect` (
`id`  int NOT NULL AUTO_INCREMENT ,
`userId`  int NULL ,
`collect`  varchar(20) NULL ,
PRIMARY KEY (`id`)
);

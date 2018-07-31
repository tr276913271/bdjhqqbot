ALTER TABLE `equipment`
ADD COLUMN `probability`  int NULL AFTER `price`;
INSERT INTO `buket`.`code` (`code`, `codeName`, `codeType`) VALUES ('15', '小怪', '职业类型');

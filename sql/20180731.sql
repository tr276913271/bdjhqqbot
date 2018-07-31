ALTER TABLE `equipment`
ADD COLUMN `probability`  int NULL AFTER `price`;
INSERT INTO `buket`.`code` (`code`, `codeName`, `codeType`) VALUES ('15', '小怪', '职业类型');

update equipment set probability=30 where id in (1,2,3);
update equipment set probability=15 where id in (11,12,13);
update equipment set probability=10 where id in (14,15,16);
update equipment set probability=20 where id in (20);

update battle set attack=20 , defense = 20 where profession !=14;
update battle set attack=0  , defense = 0 where profession =14;

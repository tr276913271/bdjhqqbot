/*
Navicat MySQL Data Transfer

Source Server         : 10.9.21.18
Source Server Version : 50722
Source Host           : 10.9.21.18:65531
Source Database       : buket

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2018-07-16 14:46:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for battle
-- ----------------------------
DROP TABLE IF EXISTS `battle`;
CREATE TABLE `battle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(10) unsigned DEFAULT NULL,
  `hp` int(10) unsigned DEFAULT NULL,
  `experience` int(5) unsigned DEFAULT NULL,
  `attack` int(5) unsigned DEFAULT NULL,
  `defense` int(5) unsigned DEFAULT NULL,
  `head` int(5) unsigned DEFAULT NULL,
  `body` int(5) unsigned DEFAULT NULL,
  `weapon` int(5) unsigned DEFAULT NULL,
  `userId` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for equipment
-- ----------------------------
DROP TABLE IF EXISTS `equipment`;
CREATE TABLE `equipment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc` varchar(30) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `type` int(5) unsigned DEFAULT NULL,
  `attack` int(5) unsigned DEFAULT NULL,
  `defense` int(5) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for theft
-- ----------------------------
DROP TABLE IF EXISTS `theft`;
CREATE TABLE `theft` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userId` int(11) NOT NULL,
  `coin` int(11) DEFAULT NULL,
  `theftDate` date DEFAULT NULL,
  `theftUserid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `coin` int(11) DEFAULT NULL,
  `coinDate` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='群员属性';


INSERT INTO `equipment` VALUES ('1', null, '新手头盔', '1', '0', '10');
INSERT INTO `equipment` VALUES ('2', null, '破旧的剑', '2', '10', '0');
INSERT INTO `equipment` VALUES ('3', null, '新手胸甲', '3', '0', '10');
INSERT INTO `equipment` VALUES ('4', null, '青铜剑', '1', '15', '0');

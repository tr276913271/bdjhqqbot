/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : buket

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-07-15 12:35:28
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
-- Records of battle
-- ----------------------------

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
-- Records of equipment
-- ----------------------------
INSERT INTO `equipment` VALUES ('1', null, '新手头盔', '1', '0', '10');
INSERT INTO `equipment` VALUES ('2', null, '破旧的剑', '2', '10', '0');
INSERT INTO `equipment` VALUES ('3', null, '新手胸甲', '3', '0', '10');
INSERT INTO `equipment` VALUES ('4', null, '青铜剑', '1', '15', '0');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `coin` int(5) unsigned DEFAULT NULL,
  `coinDate` date DEFAULT NULL,
  `thiefDate` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='群员属性';

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'aaq', null, '2009-09-09', null);
INSERT INTO `user` VALUES ('7', 'aaq', null, null, null);

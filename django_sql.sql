/*
 Navicat MySQL Data Transfer

 Source Server         : 新连接
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : django_sql

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 27/06/2022 14:01:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_dorm
-- ----------------------------
DROP TABLE IF EXISTS `t_dorm`;
CREATE TABLE `t_dorm`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `card` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dorm` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_dorm
-- ----------------------------
INSERT INTO `t_dorm` VALUES (1, '0C1CE271', '213');
INSERT INTO `t_dorm` VALUES (2, '0C1CE272', '557');
INSERT INTO `t_dorm` VALUES (3, '564FEF8B', '508');
INSERT INTO `t_dorm` VALUES (4, '0C1CE273', '809');

-- ----------------------------
-- Table structure for t_nowcard
-- ----------------------------
DROP TABLE IF EXISTS `t_nowcard`;
CREATE TABLE `t_nowcard`  (
  `card` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_nowcard
-- ----------------------------
INSERT INTO `t_nowcard` VALUES ('0C1CE273', 1);

-- ----------------------------
-- Table structure for t_record
-- ----------------------------
DROP TABLE IF EXISTS `t_record`;
CREATE TABLE `t_record`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `card` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dorm` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `text` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_record
-- ----------------------------
INSERT INTO `t_record` VALUES (1, '0C1CE271', '213', '123', '2022-06-27 12:49:10');
INSERT INTO `t_record` VALUES (2, '0C1CE271', '213', '今天还没维修', '2022-06-27 12:49:38');
INSERT INTO `t_record` VALUES (3, '0C1CE271', '213', '维修了空调', '2022-06-27 12:49:49');
INSERT INTO `t_record` VALUES (4, '0C1CE272', '557', '冰箱维修好了，师傅很好说话', '2022-06-27 12:50:43');
INSERT INTO `t_record` VALUES (5, '0C1CE272', '557', '22222', '2022-06-27 12:51:41');
INSERT INTO `t_record` VALUES (6, '564FEF8B', '508', '恍恍惚惚', '2022-06-27 13:07:01');
INSERT INTO `t_record` VALUES (7, '564FEF8B', '508', '维修电脑ok', '2022-06-27 13:11:37');
INSERT INTO `t_record` VALUES (8, '0C1CE273', '809', '维修空调', '2022-06-27 13:12:55');

SET FOREIGN_KEY_CHECKS = 1;

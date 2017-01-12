CREATE TABLE `service_line` (
  `sid`       INT(11)     NOT NULL,
  `line_name` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`sid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `user_type` (
  `tid`       INT(11)     NOT NULL,
  `user_type` VARCHAR(10) NOT NULL DEFAULT '普通',
  PRIMARY KEY (`tid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `users` (
  `uid`       INT(11)     NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(10) NOT NULL,
  `password`  VARCHAR(20) NOT NULL,
  `user_type` INT(11)     NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `fk_user_type` (`user_type`),
  CONSTRAINT `fk_user_type` FOREIGN KEY (`user_type`) REFERENCES `user_type` (`tid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE TABLE `host_list` (
  `hid`          INT(11)     NOT NULL,
  `ip`           VARCHAR(20) NOT NULL,
  `service_line` INT(11)     NOT NULL,
  PRIMARY KEY (`hid`),
  KEY `fk_service_line` (`service_line`),
  CONSTRAINT `fk_service_line` FOREIGN KEY (`service_line`) REFERENCES `service_line` (`sid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE `relation` (
  `id`      INT(11) NOT NULL AUTO_INCREMENT,
  `user`    INT(11) NOT NULL,
  `host_ip` INT(11)          DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_ip` (`user`, `host_ip`)
    COMMENT '用户名和机器唯一',
  KEY `fk_relation_host` (`host_ip`),
  CONSTRAINT `fk_relation_host` FOREIGN KEY (`host_ip`) REFERENCES `host_list` (`hid`),
  CONSTRAINT `fk_relation_user` FOREIGN KEY (`user`) REFERENCES `users` (`uid`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
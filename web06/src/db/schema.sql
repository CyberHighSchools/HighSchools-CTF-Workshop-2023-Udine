CREATE USER 'app'@'%' IDENTIFIED BY 'EPxdlXxXYyeHJg1nXV35pP1905BEIE';
CREATE DATABASE IF NOT EXISTS challenge;
USE challenge;

DROP TABLE IF EXISTS users;

CREATE TABLE users
(
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        username varchar(255) UNIQUE,
        password varchar(255),
        is_admin boolean
);

DROP TABLE IF EXISTS posts;

CREATE TABLE posts
(
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        content varchar(255),
        user_id int NOT NULL REFERENCES users(id)
);
CREATE INDEX posts_user_id ON posts (user_id);

INSERT INTO users(id, username, password, is_admin) VALUES (1, 'admin','dzFdr5TojbTX7vf01VkxWJudOMyXIt', true);
INSERT INTO posts(content, user_id) VALUES ('Hey! Cerchi questa? flag{c0ntroll0_acc3s5i_IDOR}.', 1);
GRANT SELECT,INSERT ON challenge.users TO 'app'@'%';
GRANT SELECT,INSERT,UPDATE,DELETE ON challenge.posts TO 'app'@'%';
FLUSH PRIVILEGES;

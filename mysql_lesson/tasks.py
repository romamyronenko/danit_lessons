"""
Інтернет-магазин

Товари
Клієнти
Замовлення
Оплати

***

Соціальна мережа

Профілі
Публікації
Друзі
Лайки, коментарі


***
"""

"""
aiksudgf23euiq8y6gd8o2q37q4f3q234rfq234tg3q2t234r12345y2


hjvfhjvf
"""

import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1",
)


cursor = connect.cursor()

cursor.execute("create database if not exists social_db;")
cursor.execute("use social_db;")

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS `Profile` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`email` varchar(255) NOT NULL UNIQUE,
	`password` varchar(255) NOT NULL,
	`username` varchar(255) NOT NULL UNIQUE,
	`last_seen` datetime NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Friends` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`user1_id` int NOT NULL,
	`user2_id` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Publications` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`author_id` int NOT NULL,
	`title` varchar(255) NOT NULL,
	`content` text NOT NULL,
	`publication_date` timestamp NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Likes` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`publication_id` int NOT NULL,
	`user_id` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Comments` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`publication_id` int NOT NULL,
	`user_id` int NOT NULL,
	`content` varchar(255) NOT NULL,
	`publication_date` timestamp NOT NULL,
	`is_answer` boolean NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `CommentsAnswers` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`parent_id` int NOT NULL,
	`child_id` int NOT NULL,
	PRIMARY KEY (`id`)
);"""
)

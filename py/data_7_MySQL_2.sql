/* CREATE DATABASE */
CREATE DATABASE scraping;

/* USE DATABASE */
USE scraping;

/*CREATE TABLE */
CREATE TABLE pages (id BIGINT(7) NOT NULL AUTO_INCREMENT, 
title VARCHAR(200),
content VARCHAR(10000), 
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
PRIMARY KEY(id));






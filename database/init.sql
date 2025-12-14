CREATE DATABASE IF NOT EXISTS skilltrack;

USE skilltrack;

CREATE TABLE IF NOT EXISTS skills (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  skill VARCHAR(50),
  progress INT
);


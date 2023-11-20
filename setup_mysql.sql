-- This script prepares a MySQL server for the project.

-- Creates database
CREATE DATABASE IF NOT EXISTS zome_db;

-- Creates user
CREATE USER IF NOT EXISTS 'zome'@'localhost' IDENTIFIED BY 'zome_app_pwd';

-- Grants user privileges
GRANT ALL PRIVILEGES ON zome_db.* TO 'zome'@'localhost';
GRANT SELECT ON performance_schema.* TO 'zome'@'localhost';

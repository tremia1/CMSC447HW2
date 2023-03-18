DROP TABLE IF EXISTS users;


CREATE TABLE users(	
	user_id int NOT NULL PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	points int NOT NULL,
);
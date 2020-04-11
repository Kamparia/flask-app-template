
CREATE TABLE users(
	id serial PRIMARY KEY,
	user_id VARCHAR (50) UNIQUE NOT NULL,
	firstname VARCHAR (160) NOT NULL,
	lastname VARCHAR (160) NOT NULL,
	email VARCHAR (160) UNIQUE NOT NULL,
	pwdhash VARCHAR (355) NOT NULL,
	about VARCHAR (160),
	created_on TIMESTAMP,
	last_login TIMESTAMP
);
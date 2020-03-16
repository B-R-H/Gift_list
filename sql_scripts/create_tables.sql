CREATE TABLE user_roles (
	role VARCHAR(30),
	PRIMARY KEY (role)
);

CREATE TABLE user (
	id INT NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	permission VARCHAR(30) DEFAULT 'Guest',
	email VARCHAR(150) NOT NULL,
	password VARCHAR(500) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (permission) REFERENCES user_roles(role)
);

CREATE TABLE gift_list (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	description VARCHAR(1000),
	url VARCHAR(100),
	price FLOAT,
	PRIMARY KEY (id)
);

CREATE TABLE claimed_compilation (
	id INT NOT NULL AUTO_INCREMENT,
	gift_id INT NOT NULL,
	user_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (gift_id) REFERENCES gift_list(id),
	FOREIGN KEY (user_id) REFERENCES user(id)
);

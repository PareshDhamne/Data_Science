
CREATE TABLE account(
user_id SERIAL PRIMARY KEY,
username VARCHAR(20) UNIQUE NOT NULL,
password VARCHAR(20) NOT NULL,
email VARCHAR(250) UNIQUE NOT NULL,
created_on TIMESTAMP NOT NULL,
last_login TIMESTAMP
);

CREATE TABLE job(
job_id SERIAL PRIMARY KEY,
job_name VARCHAR(200) UNIQUE NOT NULL);

CREATE TABLE account_job(
user_id INTEGER REFERENCES account(user_id),
job_id INTEGER REFERENCES job(job_id),
hire_date TIMESTAMP)
;

/**INSERT**/
INSERT INTO account(username,password,email,created_on)
VALUES
('Ram','root','ram@sanjivani.org.in',CURRENT_TIMESTAMP);

INSERT INTO account(username,password,email,created_on)
VALUES
('Sham','root','Sham@sanjivani.org.in',CURRENT_TIMESTAMP);

select * from account;

INSERT INTO job(job_name)
VALUES ('Data Scientist');

select * from job;

INSERT INTO account_job(job_id,user_id,hire_date)
VALUES
(1,1,CURRENT_TIMESTAMP);

/**UPDATE**/
select * from account;
UPDATE account
SET last_login = CURRENT_TIMESTAMP
WHERE last_login IS NULL;

select * from account;

UPDATE account
SET last_login = CURRENT_TIMESTAMP;

select * from account;

SELECT * FROM job;

SELECT * FROM account_job;

UPDATE account_job
SET hire_date=account.created_on
FROM account
WHERE account_job.user_id=account.user_id;

select * from account_job;33

UPDATE account
SET last_login = CURRENT_TIMESTAMP
RETURNING email,created_on,last_login;

/**DELETE**/

INSERT INTO job(job_name)
VALUES
('cowboy');

SELECT * FROM job;

DELETE FROM job
WHERE job_name ='cowboy'
RETURNING job_id,job_name;

SELECT * from job;

/**ALTER**/

CREATE TABLE inforamtion(
info_id SERIAL PRIMARY KEY,
title VARCHAR(500) NOT NULL,
person VARCHAR(50) NOT NULL UNIQUE
);

SELECT * FROM inforamtion;

ALTER TABLE inforamtion
RENAME to new_info;

SELECT * FROM new_info;

ALTER TABLE new_info
RENAME COLUMN PERSON TO people;

select * from new_info;

INSERT INTO new_info(title)
VALUES
('some new title');

INSERT INTO new_info(title)
VALUES
('some_new_title');

ALTER TABLE new_info
ALTER COLUMN people
DROP NOT NULL;

INSERT INTO new_info(title)
VALUES
('some_new_title');

SELECT * FROM new_info;

ALTER TABLE new_info
DROP COLUMN people;

SELECT * FROM new_info;

ALTER TABLE new_info
DROP COLUMN people;

ALTER TABLE new_info
DROP COLUMN IF EXISTS people;


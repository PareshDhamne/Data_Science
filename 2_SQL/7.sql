CREATE TABLE students(
student_id SERIAL PRIMARY KEY,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
homeroom_number INT,
phone VARCHAR(20) NULL,
email VARCHAR(250) UNIQUE NOT NULL,
graduation_year INT
);

SELECT * FROM students;

CREATE TABLE teacher(
teacher_id SERIAL PRIMARY KEY,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
homeroom_number INT,
department VARCHAR(50),
email VARCHAR(250) UNIQUE NOT NULL,
phone VARCHAR(20)
);
	
SELECT * FROM teacher;

INSERT INTO students(first_name,last_name,homeroom_number,phone,email,graduation_year)
VALUES
('Rahul','Galande',5,'7775551234','Rahul.galande@gmail.com',2023);

SELECT * FROM students;

INSERT INTO teacher(first_name,last_name,homeroom_number,department,email,phone)
VALUES
('Chandrashekhar','Gogte',5,'Biology department','Chandrashekhar.gogte@gamil.com','7775554321');

SELECT * FROM teacher;

CREATE TABLE employees(
emp_id SERIAL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE CHECK (birthdate > '1900-01-01'),
	hire_date DATE CHECK (hire_date > birthdate),
	salary INTEGER CHECK (salary > 0)
);

INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES
('Jose','Portilla','1990-11-03','2010-01-01',100);

INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES
('Sammy','Smith','1990-11-03','2010-01-01',100);

SELECT * FROM employees;

/**GO TO DVDRENTAL**/

SELECT * FROM customer;

SELECT customer_id,
CASE
    WHEN (customer_id<=100) THEN 'Premium'
	WHEN (customer_id BETWEEN 100 and 200) THEN 'Plus'
	ELSE 'Normal'
END
FROM customer;

SELECT customer_id,
CASE
    WHEN (customer_id<=100) THEN 'Premium'
	WHEN (customer_id BETWEEN 100 and 200) THEN 'Plus'
	ELSE 'Normal'
END
FROM customer;
	
SELECT customer_id,
CASE customer_id   --customer_id is expression
     WHEN 2 THEN 'Winner'
	 WHEN 5 THEN 'Second Place'
	 ELSE 'Normal'
End AS raffle_results
FROM customer;

SELECT * FROM film;

SELECT rental_rate FROM film;

SELECT
CASE rental_rate
     WHEN 0.99 THEN 1
	 ELSE 0
END
FROM film;

SELECT
SUM(CASE rental_rate
   WHEN 0.99 THEN 1
   ELSE 0
END) AS number_of_bargains
FROM film;

SELECT
SUM(CASE rental_rate
   WHEN 0.99 THEN 1
   ELSE 0
END) AS bargains,
SUM(CASE rental_rate
   WHEN 2.99 THEN 1
   ELSE 0
END) AS regular
FROM film;

SELECT
SUM(CASE rental_rate
   WHEN 0.99 THEN 1
   ELSE 0
END) AS bargains,
SUM(CASE rental_rate
   WHEN 2.99 THEN 1
   ELSE 0
END) AS regular,
SUM(CASE rental_rate
   WHEN 4.99 THEN 1
   ELSE 0
END) AS premium
FROM film;


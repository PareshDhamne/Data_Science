/*Q1. Write a SQL statement to create a table named jobs 
including columns job_id, job_title, min_salary, max_salary 
and check whether the max_salary amount exceeding the upper limit 25000.
*/
DROP TABLE jobs;
CREATE TABLE jobs(
job_id SERIAL PRIMARY KEY,
job_title VARCHAR(30) NOT NULL,
min_salary DECIMAL(5,0),
max_salary DECIMAL (5,0)
	CHECK (max_salary >= 25000));

SELECT * FROM jobs;
	
/*Q2.Write a SQL statement to change the email column of the jobs table 
with 'not available' for all jobs*/
ALTER TABLE jobs
ADD COLUMN email VARCHAR(50) DEFAULT 'not available';
SELECT * FROM jobs;
     
/*Q3.Write a SQL statement to rename the table jobs to jobs_new.*/
ALTER TABLE jobs RENAME TO jobs_new;
SELECT * FROM jobs_new;


/*Q4.Write a SQL statement to add a column dept_id to the table locations.*/
ALTER TABLE jobs_new
ADD COLUMN dept_id INT;
SELECT * FROM jobs_new;


/*Q5. Write a SQL statement to insert a record 
with your own value into the table jobs_new against each column.*/
INSERT INTO jobs_new 
VALUES(1,'Developer',2500.5,50000.0,3);
INSERT INTO jobs_new 
VALUES(2,'PRogrammer',24000.5,70000.0,2);
SELECT * FROM jobs_new;


/*Q.6 Write a query to display the names (job_id,dept_id) .*/
SELECT job_id,dept_id from jobs_new;


/*Q.7 Write a query to get the maximum total salaries payable to employees.*/
SELECT MAX(max_salary) FROM jobs_new;

/*Q.8 Write a query to get the average salary and number of employees are working.*/
SELECT AVG(max_salary),AVG(min_salary),COUNT(*) 
FROM jobs_new;

/*Q.9 Create a table manager_details 
comprises of manager_id,manager_name ,dept_id and 
Write a query to make a join with two tables jobs_new and manager_details*/
CREATE TABLE manager_details(
manager_id SERIAL PRIMARY KEY,
manager_name VARCHAR(20) NOT NULL,
dept_id INT);
SELECT * FROM manager_details;
INSERT INTO manager_details
VALUES(1,'Ram',3);
INSERT INTO manager_details
VALUES(2,'Sam',2);

SELECT job_id,job_title,min_salary,max_salary,manager_id,manager_name FROM jobs_new
INNER JOIN manager_details
ON jobs_new.dept_id=manager_details.dept_id;

/*Q.10 Write a SQL subquery 
to find the emp_id  
of all employees  from 
jobs_new table who works in the IT department.*/
SELECT emp_id FROM jobs_new
WHERE department='IT DEPARTMENT';
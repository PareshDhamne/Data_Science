/**7/09/2023**/

SELECT * FROM address;

SELECT first_name,last_name,address FROM customer
INNER JOIN address
ON customer.address_id = address.address_id;

CREATE VIEW customer_info AS
SELECT first_name,last_name,address FROM customer
INNER JOIN address
ON customer.address_id = address.address_id;

SELECT * FROM customer_info;

CREATE OR REPLACE VIEW customer_info AS
SELECT first_name,last_name,address,district FROM customer
INNER JOIN address
ON customer.address_id = address.address_id;

SELECT * FROM customer_info;

ALTER VIEW customer_info RENAME to c_info; 

SELECT * FROM customer_info;
SELECT * FROM c_info;

DROP VIEW c_info;


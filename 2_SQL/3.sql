/**31 AUG 2023**/
select customer_id from payment;

select amount as rental_price from payment;

select count(amount) as num_transactions
from payment
group by customer_id;

select customer_id,sum(amount) as total_spent
from payment
group by customer_id;

select customer_id,sum(amount)
from payment
group by customer_id
having sum(amount)>100;

select customer_id,sum(amount) as total_spent
from payment
group by customer_id
having sum(amount) >100;
/*
select customer_id,sum(amount) as total_spent
from payment
group by customer_id
having total_spent >100;
**/

select customer_id,amount as new_name
from payment
where amount > 2;
/*
JOINS
*/

SELECT * FROM payment
inner join customer
on payment.customer_id=customer.customer_id;

select payment.payment_id,payment.customer_id,customer.first_name
from payment
inner join customer
on payment.customer_id=customer.customer_id;


--FULL OUTER JOIN

select * from customer
full outer join payment
on customer.customer_id = payment.customer_id
where customer.customer_id is null
or payment.payment_id is null;

select film.film_id,title,inventory_id,store_id
from film
left outer join inventory on
inventory.film_id = film.film_id;

select * from film;
select * from inventory;

select film.film_id,title,inventory_id,store_id
from film
left join inventory on
inventory.film_id = film.film_id
where inventory.film_id is null;

select * from customer;
--select * from address;

select email,district from customer
left join address on
address.address_id = customer.address_id
where district = 'California';

/**
select district,email from customer
left join address on
address.address_id = customer.address_id
where district='QLD';
**/

select * from film_actor;
select * from film;
select * from actor;

select title,first_name,last_name from actor
inner join film_actor
on actor.actor_id = film_actor.actor_id
inner join film
on film_actor.film_id = film.film_id
where first_name='Nick' and last_name='Wahlberg';

show all;

show Timezone;

select now();

select TIMEOFDAY();

select current_date;

select * from payment;

select extract(year from payment_date) as myyear
from payment;

select extract(month from payment_date) as pay_month
from payment;

select extract(QUARTER from payment_date)
as pay_month
from payment;

select AGE(payment_date)
from payment;

select TO_CHAR(payment_date,' ')
from payment;

select TO_CHAR(payment_date,'MM/dd/YYYY')
from payment;

select TO_CHAR(payment_date,'dd-MM-YYYY')
from payment;

--1 no
select
distinct(TO_CHAR(payment_date,'MONTH'))
FROM payment;

--2 no
s3
select count(*)
from payment
where EXTRACT(dow from payment_date)=1;

























































































































































































































































































































































































































































































































































































































































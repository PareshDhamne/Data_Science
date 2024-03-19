select * from film
where rental_rate>4 and replacement_cost>=19.99;

select * from film
where rental_rate>4 and replacement_cost>=19.99
and rating='R';

select title from film
where rental_rate>4 and replacement_cost>=19.99
and rating ='R';

select count(title) from film
where rental_rate>4 and replacement_cost>=19.99
and rating='R';

select count(*) from film
where rental_rate>4 and replacement_cost>=19.99
and rating='R';

select count(*) from film
where rating='R' or rating='PG-13';

select * from film
where rating !='R';

select * from film
where rating <>'R';

/*challenges*/
--No 1
select email from customer 
where first_name='Nancy' and last_name='Thomas';

--No 2
select description from film
where title='Outlaw Hanky';

--No 3
select * from address;

select phone from address
where address='259 Ipoh Drive';

/**CHALLENGES COMPLETED**/

select * from customer
order by first_name asc;

select * from customer
order by first_name desc;

/*--select * from customer_id 
order by store_id;*/

select store_id,first_name,last_name from customer
order by store_id,first_name;

select store_id,first_name,last_name from customer
order by store_id desc, first_name ASC;

select * from payment
order by payment_date desc
limit 5;

select * from payment
where amount <> 0.00
order by payment_date desc
limit 5;

select * from customer;

/**CHALLENGES**/
--1 no
select customer_id from payment
order by payment_date
limit 10;

--2 no
select title,length from film
order by length asc
limit 5;

--3 no
select count(title) from film
where length <= 50;

/** CHALLENGE COMPLETED **/

select * from payment
limit 2;

select * from payment
where amount between 8 and 9;

select count(*) from payment
where amount between 8 and 9;

select count(*) from payment
where amount not between 8 and 9;

select * from payment
where payment_date between '2007-02-01' and '2007-02-15';

select distinct(amount) from payment
order by amount;

select * from payment
where amount in (0.99,1.98,1.99);

select count(*) from payment
where amount in (0.99,1.98,1.99);

select count(*) from payment
where amount not in (0.99,1.98,1.99);

select * from customer
where first_name in ('John','Julie','Jake');

select * from customer
where first_name not in ('John','Julie','Jake');

select * from customer
where first_name like 'J%';

select count(*) from customer
where first_name like 'J%';

select * from customer
where first_name like 'J%' and last_name like 'S%';

select * from customer
where first_name ilike 'j%' and last_name ilike 's%';

select * from customer
where first_name like '%er%';

select * from customer
where first_name like '%her%';

select * from customer
where first_name like '_her%';

select * from customer
where first_name like 'A%'
order by last_name;

select * from customer
where first_name like 'A%' and last_name not like 'B%'
order by last_name;

/**CHALLENGES**/
--1 no
select * from payment;

select count(amount) from payment
where amount > 5;

--2 no
select * from actor;

select count(first_name) from actor
where first_name like 'P%';

-- 3 no
select * from address;
select count(distinct district) from address;

--4 no
select distinct district from address
order by district;

--5 no
select * from film;
select count(title) from film
where rating='R' and replacement_cost between 5 and 15;

--6 no
select count(title) from film
where title like '%Truman%';

/**CHALLENGES COMPLETED**/

select min(replacement_cost) from film;

select max(replacement_cost) from film;

select avg(replacement_cost) from film;

select Round(avg(replacement_cost),2) from film;

select sum(replacement_cost) from film;

select customer_id from payment
group by customer_id
order by customer_id;

select customer_id, sum(amount) from payment
group by customer_id;

select customer_id, sum(amount) from payment
group by customer_id
order by sum(amount);

select customer_id, sum(amount) from payment
group by customer_id
order by sum(amount) desc;

select customer_id,staff_id,sum(amount) from payment
group by staff_id,customer_id;

select customer_id,staff_id,sum(amount) from payment
group by staff_id,customer_id
order by customer_id;

select date(payment_date), sum(amount) from payment
group by date(payment_date)
order by sum(amount) desc;

/**ASSIGNMENT**/
select * from payment;

select staff_id,count(amount) from payment
group by staff_id
order by count(amount);

--2 NO
select * from film;
select avg(replacement_cost),rating from film
group by rating;

--3 no
select * from payment;

select customer_id,sum(amount) from payment
group by customer_id
order by sum(amount) desc
limit 5;

select customer_id,sum(amount) from payment
where customer_id not in (184,87,477)
group by customer_id;

select customer_id,sum(amount) from payment
group by customer_id
having sum(amount) > 100;

select * from customer;

select store_id,count(customer_id) from customer
group by store_id;

select store_id,count(*) from customer
group by store_id;

select store_id,count(*) from customer
group by store_id
having count(*) >300;

select store_id,count(*) from customer
group by store_id
having count(customer_id) >300;

/**CHALLENGES**/
select * from payment;

select customer_id,count(amount)from payment
group by customer_id
having count(*)>=40;

--2 no
select customer_id,sum(amount) from payment
where staff_id = 2
group by customer_id
having sum(amount) >100;

/**ASSESMENT TEST 1**/
--1 NO
select * from payment;

select customer_id,sum(amount) from payment
where staff_id=2
group by customer_id
having sum(amount)>=110;

--2 no
select count(*) from film
where title like 'J%';

--3 no
select * from customer;

select first_name,last_name from customer
where first_name like 'E%' and address_id < 500
order by customer_id desc
limit 1;




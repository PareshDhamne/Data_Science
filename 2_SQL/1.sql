select * from film;

select * from actor;

select * from city;

select count(category_id) from film_category;

select max(amount) from payment;

/*
adding comment use this
*/

select first_name ,last_name from actor;

select first_name,last_name
from actor
where first_name='Nick' and last_name='Davis';

select * from category;
select * from film_category where category_id=6;

select * from address where city_id=576;

select * from city;

select * from film
where rental_rate>4 and replacement_cost>=19.99;

select * from film
where rental_rate>4 and replacement_cost>=19.99
and rating='R';

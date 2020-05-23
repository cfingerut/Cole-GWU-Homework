
select * 
from actor 
where actor_id in 
(select actor_id from film_actor
where film_id = 
(select film_id
from film
where title = 'ALTER VICTORY'))


	

select * from staff
where first_name = 'Jon' and last_name = 'Stephens'




select title from film
where film_id in
(select film_id from inventory
where inventory_id in 
(select inventory_id from rental
where staff_id =
(select staff_id from staff
where first_name = 'Jon' and last_name = 'Stephens')))




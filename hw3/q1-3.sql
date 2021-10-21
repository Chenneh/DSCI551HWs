use sakila;
select a.actor_id, a.first_name, a.last_name, f.film_id, f.title
from actor a 
	inner join film_actor fa on a.actor_id=fa.actor_id
	inner join film f on f.film_id=fa.film_id
where a.actor_id=1
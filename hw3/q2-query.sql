use sakila;
select a.actor_id, a.first_name, a.last_name
from actor a
	inner join film_actor fa on a.actor_id=fa.actor_id
    inner join comedy_film cf on cf.film_id=fa.film_id
group by a.actor_id
order by a.actor_id desc;
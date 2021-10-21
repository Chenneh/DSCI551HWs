select a.actor_id
from actor a 
	inner join film_actor fa on fa.actor_id=a.actor_id
    inner join film f on f.film_id=fa.film_id
where f.length < 48
group by actor_id
order by a.actor_id asc;
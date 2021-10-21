select a.first_name, a.last_name
from actor a
	inner join film_actor fa on a.actor_id=fa.actor_id
group by a.first_name, a.last_name
having count(fa.film_id)>30
order by a.first_name, a.last_name;
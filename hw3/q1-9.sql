select title, release_year
from film
where film_id = Any(
	select film_id from film_actor
    where actor_id=1
)
order by title asc;
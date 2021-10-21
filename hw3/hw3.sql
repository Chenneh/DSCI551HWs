select a.actor_id, fc.category_id, count(category_id), group_concat(category_id)
from actor a
	left outer join film_actor fa on a.actor_id=fa.actor_id
	left outer join film_category fc on fa.film_id=fc.film_id
where a.first_name='Ed' and a.last_name='Chase'
group by a.actor_id, fc.category_id 

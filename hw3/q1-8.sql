use sakila;
select count(cate.category_id) as number_of_categories
from 
(
	select fc.category_id
	from actor a
		left outer join film_actor fa on a.actor_id=fa.actor_id
		left outer join film_category fc on fa.film_id=fc.film_id
	where a.first_name='Ed' and a.last_name='Chase'
	group by fc.category_id
) cate;
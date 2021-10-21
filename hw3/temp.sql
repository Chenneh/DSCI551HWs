select FID, title, group_concat(concat(a.first_name, ' ', a.last_name)) as actor_list
from nicer_but_slower_film_list nb
	inner join film_actor fa on fa.film_id=nb.FID
	inner join actor a on a.actor_id=fa.actor_id
where a.first_name='Temple' || a.last_name='Temple'
group by title
order by FID asc;
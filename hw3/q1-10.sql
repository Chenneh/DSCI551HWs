use sakila;
select l.name
from language l
	left join film f on l.language_id=f.language_id
where film_id is null
order by l.name


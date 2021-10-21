use sakila;
create view Comedy_film
as
select f.film_id, f.title
from film f
	inner join film_category fc on fc.film_id=f.film_id
    inner join category c on c.category_id=fc.category_id
where c.name='Comedy'
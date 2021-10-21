use sakila;
select actor_id, first_name, last_name, last_update
From actor
Where first_name Like '%er%'
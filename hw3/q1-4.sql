select a.address_id, a.address, a.city_id
from address a
	inner join city ci on a.city_id=ci.city_id
    inner join country co on ci.country_id=co.country_id
where co.country='Argentina';
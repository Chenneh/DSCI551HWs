select amount 
from payment
group by amount
order by amount desc limit 1,1;
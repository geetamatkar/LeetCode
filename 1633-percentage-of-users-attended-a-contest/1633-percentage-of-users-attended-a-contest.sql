# Write your MySQL query statement below
/*
select distinct contest_id, round(count(distinct u.user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
from users u right join register r
on u.user_id = r.user_id
group by contest_id
order by percentage desc,contest_id;
*/

select distinct contest_id, round(count(distinct r.user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
from register r
group by contest_id
order by percentage desc,contest_id;
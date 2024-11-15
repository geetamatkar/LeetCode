# Write your MySQL query statement below
select B.id
from weather A, weather B
where datediff(b.recordDate, a.recordDate) = 1 and B.temperature>A.temperature;

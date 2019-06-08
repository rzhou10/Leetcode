/*
    Classes More Than 5 Students
    Runtime: 195 ms
*/

select class from  courses group by class having count(distinct student)>=5
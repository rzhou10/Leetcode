/*
    Employees Earning More Than Their Managers
    Runtime: 279 ms
*/

select e.Name as Employee from Employee e inner join Employee m on e.ManagerId = m.Id where e.Salary > m.Salary
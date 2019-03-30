/*
    Second Highest Salary
    Runtime: 137 ms
*/

select max(Salary) as SecondHighestSalary from Employee where Salary < (select max(Salary) from Employee)
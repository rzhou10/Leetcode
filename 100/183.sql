/*
    Customers Who Never Order
    Runtime: 238 ms
*/

select C.name as 'Customers' from Customers C where C.id not in (select CustomerId from Orders)
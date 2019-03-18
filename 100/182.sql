/*
    Duplicate Emails
    Runtime: 194 ms
*/

select email from Person group by Email having count(*) > 1
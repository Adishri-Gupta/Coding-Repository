# Write your MySQL query statement below
SELECT max(SALARY) as SecondHighestSalary
from EMPLOYEE
where SALARY NOT IN (SELECT max(SALARY) from EMPLOYEE)
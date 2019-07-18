# Write your MySQL query statement below
SELECT a.NAME AS Employee
FROM Employee As a JOIN Employee as b
    ON a.ManagerId = b.Id
    AND a.Salary > b.Salary

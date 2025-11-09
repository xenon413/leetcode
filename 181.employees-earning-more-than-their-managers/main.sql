# Write your MySQL query statement below

SELECT e.name AS Employee FROM Employee AS e 
JOIN Employee AS m ON e.ManagerId = m.Id WHERE e.Salary > m.Salary
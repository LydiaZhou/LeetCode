# # Write your MySQL query statement below
# select d.Name as Department, e.Name as Employee, e.Salary as Salary
# from Employee e, Department d
# where e.DepartmentId = d.Id
# and e.salary = (select max(Salary) from Employee e2 where e2.DepartmentId = e.DepartmentId)

# #  Solution2 save time
# SELECT d.Name as Department, y.Name as Employee, y.Salary as Salary
# FROM
# ((SELECT DepartmentId, max(Salary) as max
# FROM Employee
# GROUP BY DepartmentId) x
# INNER JOIN
# Employee y
# ON x.DepartmentId = y.DepartmentId and x.max = y.Salary), Department d
# WHERE d.Id = y.DepartmentId

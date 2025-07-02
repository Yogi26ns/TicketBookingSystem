use foundation_training;
select concat(first_name,' ',last_name) as employee_name,department_name,city,country_name
from employees 
inner join departments using(department_id)
inner join locations using(location_id)
inner join countries using (country_id);

select city, count(employee_id) 
from locations join departments using(location_id)
join employees using(department_id)
group by city 
order by 2 desc;

select job_title, count(employee_id) 
from jobs join employees using(job_id)
group by job_title
order by 2 desc
limit 5;

select department_name,concat(first_name,' ',last_name) as "manager_name"
from departments D left join employees E on D.manager_id = E.manager_id;

select concat(first_name,' ',last_name) as "full_name" , department_name
from employees E left join departments D on E.department_id = D.department_id
order by 2;

select department_name,concat(first_name,' ',last_name) as "full_name" 
from employees right join departments using(department_id)
order by 2;

select country_name,concat(first_name,' ',last_name) as "full_name" 
from employees join departments using(department_id)
join locations using(location_id) 
right join countries using(country_id)
order by 2;

select city,concat(first_name,' ',last_name) as "full_name"
from employees join departments using(department_id)
right join locations using(location_id)
order by 2;

select department_name, count(department_id) as left_employees
from departments
join job_history using(department_id)
group by department_name
order by 2;

select concat(first_name,' ',last_name),department_id
from employees 
left join departments using(department_id)
union
select concat(first_name,' ',last_name),department_id
from employees 
right join departments using(department_id)
order by 2;

select concat(e1.first_name,' ',e1.last_name) as "emp_name" ,concat(e2.first_name,' ',e2.last_name) "manager_name"
from employees e1 join employees e2 on e1.manager_id = e2.employee_id;

select concat(e1.first_name,' ',e1.last_name) as "emp_name" ,concat(e2.first_name,' ',e2.last_name) "manager_name"
from employees e1 left join employees e2 on e1.manager_id = e2.employee_id
where e2.first_name is null;

select concat(e1.first_name,' ',e1.last_name) as "emp_name" ,concat(e2.first_name,' ',e2.last_name) "manager_name"
from employees e1 right join employees e2 on e1.manager_id = e2.employee_id
order by 1;

select * from employees cross join departments;

create view view_emp_mng as
select * from employees where manager_id in(100,101,102);

select * from view_emp_mng;

create or replace view total_dept_salary as
select department_id,sum(salary) as total_salary from employees
group by department_id;

select * from total_dept_salary;

create or replace view higher_salary_emp as
select concat(first_name,' ',last_name) as "emp_name",salary,total_salary
from employees join total_dept_salary using (department_id)
where salary>0.6*total_salary;

select * from higher_salary_emp;

create view view_empl_60 as
select department_id,sum(salary)*.60 sal_60 from employees
group by 1;

select first_name,salary,sal_60,department_id 
from employees 
join view_empl_60 using(department_id)
where employees.department_id = view_empl_60.department_id and employees.salary>view_empl_60.sal_60;

select * from view_empl_60;

/*
join
types of join(inner,left,right,full,natural,self,cross)
view
*/
-- List the following details of each employee: employee number, 
--last name, first name, sex, and salary.

select e.emp_no as "employee_number"
	, e.first_name as "first name"
	, e.last_name as "last name"
	, e.sex as "sex"
	, cast(s.salaries as money) as salary
	from employees e
		INNER JOIN salaries s on 
			s.emp_no = e.emp_no;


--List first name, last name, and hire date for employees who were hired in 1986.

select e.first_name as "First Name"
	, e.last_name as "Last Name"
	, e.hire_date as "Date Hired"
	from employees e
	where
		extract(year from hire_date) = '1986'

-- List the manager of each department with the following information: 
-- department number, department name, the manager's employee number, last name, first name.

select dm.dept_no as "Dept Number"
	, d.dept_name as "Department Name"
	, e.emp_no as "Manager's' Employee Number"
	, e.first_name as "First Name"
	, e.last_name as "Last Name"
		from dept_manager dm
		INNER JOIN  departments d on
			d.dept_no = dm.dept_no
		INNER JOIN employees e on
			e.emp_no = dm.emp_no; 




-- List the department of each employee with the following information: employee number, 
-- last name,first name, and department name.

select e.emp_no, e.first_name, e.last_name, d.dept_name
	from dept_emp de
		inner join employees e on
			de.emp_no = e.emp_no
	i	nner join departments d
		on de.dept_no = d.dept_no;



-- List first name, last name, and sex for employees whose first name 
-- is "Hercules" and last names begin with "B."

select first_name as "Emp First Name"
	, last_name as "Emp Last Name"
	, sex as "Sex"
		from employees 
		where first_name = 'Hercules' and last_name like 'B%';





-- List all employees in the Sales department, including their employee number, last name, 
-- first name, and department name.


select e.emp_no, e.first_name, e.last_name, d.dept_name
	from employees e
		inner join dept_emp de on
				e.emp_no = de.emp_no
		inner join departments d
			on d.dept_no= de.dept_no
			and d.dept_name = 'Sales';


-- List all employees in the Sales and Development departments, including their employee number, 
-- last name, first name, and department name.

select e.emp_no as "Employee Number"
	,e.last_name as "Employee Last Name"
	, e.first_name as "Employee First Name"
	, d.dept_name as "Dept Name"
	from employees e
		inner JOIN dept_emp de on
			de.emp_no = e.emp_no
			inner JOIN departments d on 
			d.dept_no = de.dept_no
			and d.dept_name in ('Sales','Development');





-- In descending order, list the frequency count of employee last names, i.e., how many employees 
-- share each last name.

select last_name as "Last Name"
,count(last_name) as "Frequency Count"
	from employees 
	group by last_name
	order by count(last_name) desc;
	
	
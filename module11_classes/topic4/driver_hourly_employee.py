"""
Program: driver_hourly_employee_.py
Author: Kelly Smith
Last day updated: 11-4-19

Driver for the hourly employee class
:param last_name - Employee's last name
:param first_name - Employee's first name
:param phone_number - Employee's phone number
:param address_street - Employee's street address
:param address_city - Employee's city and state
:param hourly_rate - Employee's hourly pay rate
:param start_date - Employee's start date
:return Employee's personal information, hourly pay rate and start date
"""

from module11_classes.topic4.employee_class import Employee
from module11_classes.topic4.hourly_employee_class import HourlyEmployee

new_emp = Employee('Smith', 'Kelly', '5151234567', '123 Main St', 'Des Moines, IA')
new_emp_hourly = HourlyEmployee(new_emp.last_name, new_emp.first_name, new_emp.phone_number, new_emp.address_1, new_emp.address_2, 10.00, '10-20-2019')
print(new_emp_hourly.display())
new_emp_hourly.give_raise(15.00)
print(new_emp_hourly.display())
del new_emp

"""
Program: salaried_employee_class.py
Author: Kelly Smith
Last day updated: 11-4-19

Program to get employee start date and salary
:param emp_salary - Employee's salary
:param start_date - Employee's start date
:return Employee's salary and start date
"""
from module11_classes.topic4.employee_class import Employee


class SalariedEmployee(Employee):

    def __init__(self, lanme, fname, pnumber, address_street, address_city, salary, sdate):
        super(SalariedEmployee, self).__init__(lanme, fname, pnumber, address_street, address_city)
        self.emp_salary = salary
        self.start_date = sdate

    def give_raise(self, salary):
        self.emp_salary = salary

    def display(self):
        return f'Employee Name: {self.first_name} {self.last_name}; Employee Phone Number: {self.phone_number}; Employee Address:{self.address_1},{self.address_2}; Employee Salary: ${self.emp_salary}; Employee Start Date: {self.start_date}'

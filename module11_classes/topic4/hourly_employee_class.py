"""
Program: hourly_employee_class.py
Author: Kelly Smith
Last day updated: 11-4-19

Program to get employee start date and salary
:param hourly_rate - Employee's hourly pay rate
:param start_date - Employee's start date
:return Employee's hourly pay rate and start date
"""

from module11_classes.topic4.employee_class import Employee


class HourlyEmployee(Employee):

    def __init__(self, lanme, fname, pnumber, address_street, address_city, hourly_rate, sdate):
        super(HourlyEmployee, self).__init__(lanme, fname, pnumber, address_street, address_city)
        self.pay_rate = hourly_rate
        self.start_date = sdate

    def give_raise(self, hourly_rate):
        self.pay_rate = hourly_rate

    def display(self):
        return f'Employee Name: {self.first_name} {self.last_name}; Employee Phone Number: {self.phone_number}; Employee Address:{self.address_1},{self.address_2}; Employee Hourly Rate: ${self.pay_rate}; Employee Start Date: {self.start_date}'

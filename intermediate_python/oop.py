class Employee:
    
    RAISE_AMT = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMT)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.RAISE_AMT = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)

import datetime
today = datetime.datetime.today()

print(Employee.is_workday(today))

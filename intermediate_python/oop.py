class Employee:
    
    RAISE_AMT = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@email.com'
        
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
    
class Developer(Employee):
    RAISE_AMT = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # equal to: Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
    

class Manager(Employee):
    RAISE_AMT = 1.04
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')
            
        
        
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)

dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer('Junu', 'Moon', 60000, 'JavaScript')

mgr_1 = Manager('David', 'Copher', 70000, [dev_1])

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)

# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)
# dev_1.apply_raise()
# print(dev_1.pay)
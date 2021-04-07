class Employee:
    
    RAISE_AMT = 1.04
    
    def __init__(self, first, last, pay=0):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self, name):
        print('Delete Name!')
        self.first = None
        self.last = None
        
    
    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMT) 
        
    def __repr__(self):  # Magic Method
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
    
    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return self.fullname().__len__()
        
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

emp_1 = Employee('John', 'Smith')
print(emp_1.fullname)

emp_1.first = "Jin"
emp_1.fullname = 'Corey Schcafer'

print(emp_1.fullname)
print(emp_1.email)
print(emp_1.pay)


# print(dev_1)

# print(repr(dev_1))
# print(str(dev_1))

# print(dev_1.__repr__())
# print(dev_1.__str__())

# print(1+2)

# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))

# print(dev_1 + mgr_1)

# print('test'.__len__())
# print(dev_1.__len__())


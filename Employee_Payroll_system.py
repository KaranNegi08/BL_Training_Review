# Task 2 – Employee Payroll System
# Scenario
# Build an employee payroll system that handles different employee types (e.g., RegularEmployee, Manager, Contractor) with different salary calculation rules.
# OOP‑Covered
# Abstraction, inheritance, polymorphism, encapsulation
# Instructions
# Create an abstract class Employee with id, name, email and an abstract calculateSalary().
# Create derived classes:
# RegularEmployee: salary = base pay.
# Manager: salary = base pay + 20% bonus.
# Contractor: salary = hourly rate × hours worked.
# Demonstrate:
# List of Employee objects.
# Polymorphic call to calculateSalary() for each.
# Access modifiers (private fields with public getters/setters).
# Input validation (e.g., basePay > 0).

from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, email, base_pay, hours_worked= None, hourly_rate= None):
        self.emp_id= emp_id
        self.name= name
        self.email= email
        self.base_pay = base_pay
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    @property
    def base_pay(self):
        return self._base_pay
        
    @base_pay.setter
    def base_pay(self, value):
        if value <= 0:
            print("Base pay must be greater than 0.")
            exit()
            
        self._base_pay = value
        

    @abstractmethod
    def calculate_salary(self):
        pass

class RegularEmployee(Employee):

    def calculate_salary(self):
        return float(self.base_pay)
    



class Manager(Employee):

    def calculate_salary(self):
        return float(self.base_pay + (0.2 * self.base_pay))



class Contractor(Employee):

    def calculate_salary(self):
        return float(self.hours_worked * self.hourly_rate)
    

emp1= RegularEmployee(1,"karan","karan@gmail.com", -1)
print(emp1.calculate_salary())

emp2= Manager(2,"dishant","dishant@gmail.com", 7000)
print(emp2.calculate_salary())

emp3= Contractor(3,"Rahul","rahul@gmail.com",1000, 48,50)
print(emp3.calculate_salary())
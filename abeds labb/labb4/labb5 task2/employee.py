from abc import ABC, abstractmethod

class Employee:
    def __init__(self, emp_id, name, email, department):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.department = department

    
    @abstractmethod
    def calculate_pay():
        pass

    def __str__(self):
        pass
class Employee:
    def __init__(self, emp_id, name, email, department):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.department = department

    def calculate_pay(self):
        """detta är en abstrakt metod som ska implementeras i subklasserna"""
        pass

    def __str__(self):
        return f"Employee: {self.name}, ID: {self.emp_id}, Email: {self.email}, Department: {self.department}"
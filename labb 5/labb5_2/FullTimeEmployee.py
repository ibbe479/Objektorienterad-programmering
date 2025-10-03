from employee import Employee

class FullTimeEmployee (Employee):
    def __init__(self, salary, benefits, emp_id, name, email, department):
        super().__init__(emp_id, name, email, department)
        self.salary = salary
        self.benefits = benefits

    def calculate_pay(self):
        return self.salary

    def __str__(self):
        return f"{super().__str__()}, Salary: {self.salary}, Benefits: {self.benefits}"
from employee import Employee
class Contractor (Employee):
    def __init__(self, rate, duration, emp_id, name, email, department):
        super().__init__(emp_id, name, email, department)
        self.rate = rate
        self.duration = duration

    def calculate_pay(self):
        return self.rate * self.duration

    def __str__(self):
        return f"{super().__str__()}, Rate: {self.rate}, Duration: {self.duration} hours"
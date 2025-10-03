from employee import Employee

class PartTimeEmployee (Employee):
    def __init__(self, hourly_rate, hours, emp_id, email, name, department):
        super().__init__(emp_id, name, email, department)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_pay(self):
        return self.hourly_rate * self.hours
    
    def __str__(self):
        return f"{super().__str__()}, Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours}"
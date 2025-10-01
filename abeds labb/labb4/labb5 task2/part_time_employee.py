from employee import Employee

class Part_time_emoployee(Employee):
    def __init__(self, emp_id, name, email, department,hourly_rate, hours):
        super().__init__(emp_id, name, email, department)

        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_pay():
        pass

    def __str__(self):
        return super().__str__()
    
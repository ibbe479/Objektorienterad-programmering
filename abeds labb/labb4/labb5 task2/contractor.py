from employee import Employee

class Part_time_emoployee(Employee):
    def __init__(self, emp_id, name, email, department,rate , duration):
        super().__init__(emp_id, name, email, department)

        self.rate = rate
        self.duration = duration

    def calculate_pay():
        pass

    def __str__(self):
        return super().__str__()
    
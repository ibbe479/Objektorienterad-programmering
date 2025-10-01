from employee import Employee

class Full_time_employee(Employee):
    def __init__(self, emp_id, name, email, department, salary, benefits,):
        super().__init__(emp_id, name, email, department)

        self.salary = salary
        self.benefits = benefits

    def calculate_pay():
        pass
        
    def __str__(self):
        return super().__str__()

from employee import Employee
from full_time_employee import Full_time_employee
from part_time_employee import Part_time_employee
from contractor import Contractor

class Employee_manager(Employee):

    def __init__(self):
        self.employee = []
    
    def create_employee(self, employee_type, emp_id, name, email, department, **kwargs):
        if employee_type == 'full_time_employee':
            salary = float(kwargs.get('salary', 0))
            benefits = float(kwargs.get('benefits', 0))

            employee = Full_time_employee(emp_id, name, email, department, salary, benefits)
        
        elif employee_type == 'part_time_employee':
            hourly_rate = float(kwargs.get('hourly_rate', 0))
            hours = float(kwargs.get('hours', 0))

            employee = Part_time_employee(emp_id, name, email, department, hourly_rate, hours)
        
        elif employee_type == 'contractor':
            rate = float(kwargs.get('rate', 0))
            duration = float(kwargs.get('duration', 0))

            employee = Contractor(emp_id, name, email, department, rate, duration)
        
        else:
            print("Invalid employee type")
            return False
        
        self.employee.append(employee)
        return True

    
    def remove_employee(self, emp_id):
        for i, emp in enumerate(self.employee):
            if emp.emp_id == emp_id:
                del self.employee[i]
                print("Employee removed")
                return
        print("Employee not found")
    
    def find_employee(self, emp_id=None):
        for emp in self.employee:
            if emp.emp_id == emp_id:
                print(f"Employee: {emp}")
                return emp
        print("Employee not found")
        return None
        
    
    def display_employee(self):
        if not self.employee:
            print("No employee to display")
            return
        print("\nEmployees:")
        for emp in self.employee:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Email: {emp.email}, Department: {emp.department}", end="")
            if isinstance(emp, Full_time_employee):
                print(f", Salary: {emp.salary}, Benefits: {emp.benefits}")
            elif isinstance(emp, Part_time_employee):
                print(f", Hourly rate: {emp.hourly_rate}, Hours: {emp.hours}")
            elif isinstance(emp, Contractor):
                print(f", Rate: {emp.rate}, Duration: {emp.duration}")
            else:
                print("")
    
    def total_payroll(self):
        total = 0
        for emp in self.employee:
            total += emp.calculate_pay()
        print(f"Total Payroll: {total}")
        return total

from employee import Employee
from fullTimeEmployee import FullTimeEmployee
from partTimeEmployee import PartTimeEmployee
from contractor import Contractor

class EmployeeManager:
    def __init__(self):
        self.employees = []

    
    def create_employee(self, employee_type, emp_id, name, email, department, **kwargs):
        if employee_type.lower() == "fulltime".lower():
            
        
            benifits=kwargs.get('benifits')
            salary=kwargs.get('salary')
            salary=float(salary)
            ny_emp= FullTimeEmployee(salary, benifits, emp_id, name, email,department) 
            self.employees.append(ny_emp)
            print(f"en ny fulltime employee har lagts till")

        elif employee_type.lower() == "parttime".lower():
            hourly_rate=float(hourly_rate)
            hours=float(hours)

            hourly_rate=kwargs.get('hourly_rate')
            hours=kwargs.get('hours')
            hourly_rate=float(hourly_rate)
            hours=float(hours)
            ny_emp= PartTimeEmployee(hourly_rate, hours, emp_id, email, name, department)
            self.employees.append(ny_emp)
            print(f"en ny partimte employee har lagts till")

        elif employee_type.lower() == "contractor".lower():

            rate=kwargs.get('rate')
            duration=kwargs.get('duration')
            rate=float(rate)
            duration=int(duration)
            ny_emp= Contractor(rate, duration, emp_id, name, email,department)
            self.employees.append(ny_emp)
            print(f"en ny contractor har lagts till")

            

    def remove_employee(self, emp_nr):
        emp_nr=int(emp_nr)
        for anstälnd in self.employees:

            if anstälnd.emp_id == emp_nr:
                self.employees.remove(anstälnd)
                print ("du har tafit bort en anstäldt")
                return
        print(f"anstäld med {emp_nr} hittades inte")
        

    def find_employee():
        pass

    def dispaly_all(self):
        if not self.employees:
            print ("finns inga produkter")
        else:
            for anstälda in self.employees:
                if isinstance(anstälda, FullTimeEmployee):
                    print (f"- {anstälda}")
                elif isinstance (anstälda, PartTimeEmployee):
                    print (f"- {anstälda}")
                elif isinstance(anstälda, Contractor):
                    print (f"- {anstälda}")

    def total_payroll():
        pass

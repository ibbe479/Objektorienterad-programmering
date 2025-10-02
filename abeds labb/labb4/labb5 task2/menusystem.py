from employee_manager import Employee_manager
from full_time_employee import Full_time_employee
from part_time_employee import Part_time_employee
from contractor import Contractor

class Menu_system(Employee_manager):
    def __init__(self):
        self.employee = Employee_manager()

    def show_menu(self):
        print("\nMenu:")
        print("1. Create employee")
        print("2. Remove employee")
        print("3. Find employee")
        print("4. Display employee")
        print("5. Total payroll")
        print("0. Exit")

    def add_employee_flow():
        pass

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option")

            if choice == "1":
                employee_type = input("Enter the employee type (fulltime/parttime/ contractor): ").lower()
                emp_id = input("Enter employee id: ")
                name = input("Enter employee name: ")
                email = input("Enter employee email: ")
                department = input("Enter employee department: ")

                kwargs = {}

                if employee_type == "fulltime":
                    kwargs["salary"] = input("Enter employee salary: ")
                    kwargs["benefits"] = input("Enter employee benefits: ")
                    employee_type = "full_time_employee"  

                elif employee_type == "parttime":
                    kwargs["hourly_rate"] = input("Enter employee hourly rate: ")
                    kwargs["hours"] = input("Enter employee hours: ")
                    employee_type = "part_time_employee"  

                elif employee_type == "contractor":
                    kwargs["rate"] = input("Enter employee rate: ")
                    kwargs["duration"] = input("Enter employee duration: ")
                    
                else:
                    print("Invalid employee type! Please enter 'fulltime', 'parttime', or 'contractor'.")
                    continue

                self.employee.create_employee(employee_type, emp_id, name, email, department, **kwargs)
                print("Employee created successfully!")
            
            elif choice == "2":
                employee_id = input("Enter Emp ID you want to remove: ")

                self.employee.remove_employee(employee_id)
            
            elif choice == "3":
                employee_id = input("enter employee ID you want to search: ")

                self.employee.find_employee(employee_id)
            
            elif choice == "4":
                self.employee.display_employee()
            
            elif choice == "5":
                self.employee.total_payroll()
            
            elif choice == "0":
                break
            
            else:
                print("Choose an input")



if __name__ == "__main__":
    menu_system = Menu_system()
    menu_system.run()
            
    
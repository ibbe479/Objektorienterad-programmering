from employeeManager import EmployeeManager

class MenuSystem:
    def __init__(self):
        self.manager = EmployeeManager()

    def show_menu(self):
        print("1. Create Employee")
        print("2. Remove Employee")
        print("3. Find Employee")
        print("4. Display Employees")
        print("5. Total Payroll")
        print("6. Exit")

    def add_employee_flow():
        pass

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select an option: ")

            if choice == "1":
                employee_type = input("vilken typ av anställd vill du lägga till? (fulltime, parttime, contractor): ")
                emp_id = input("skriv in anställdes id: ")
                name = input("skriv in anställdes namn: ")
                email = input("skriv in anställdes email: ")
                department = input("skriv in anställdes avdelning: ")

                kwargs = {}

                if employee_type.lower() == "fulltime".lower():
                    kwargs['salary'] = input("skriv in anställdes lön: ")
                    kwargs['benifits'] = input("skriv in anställdes förmåner: ")
                elif employee_type.lower() == "parttime".lower():
                    kwargs['hourly_rate'] = float(input("skriv in anställdes timlön: "))
                    kwargs['hours'] = float(input("skriv in antal arbetade timmar: "))
                elif employee_type.lower() == "contractor".lower(): 
                    kwargs['rate'] = float(input("skriv in anställdes taxa: "))
                    kwargs['duration'] = int(input("skriv in antal arbetade timmar: "))
                else:
                    print("ogiltig typ, försök igen.")
                    continue
                
                self.manager.create_employee(employee_type, emp_id, name, email, department, **kwargs)
             

            elif choice == "2":
                pass
            elif choice == "3":
                emp_nr=int(input("vad är emp nummret du vill ta bort"))
                self.manager.remove_employee(emp_nr)

            elif choice == "4":
                self.manager.dispaly_all()
            elif choice == "5":
                pass
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
    
if __name__ == "__main__":
    menu = MenuSystem()
    menu.run()
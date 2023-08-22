

class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        
        
    def calculate_salary(self,emp_salary,hours_worked):
            overtime=0
            if hours_worked>50:
                overtime=hours_worked-50                
            self.emp_salary=self.emp_salary+(overtime*(self.emp_salary/50))
            
                
    def assign_department(self,emp_department):
            self.emp_department=emp_department
            
            
    def print_employee_details(self):
                print("\nName :",self.emp_name)
                print("\nSalary :",self.emp_salary)
                print("\nid :",self.emp_id)
                print("\nDepartment :",self.emp_department)  
                
    
            
Employee1=Employee("ADAMS","E7876",50000,"ACCOUNTING")
Employee2=Employee("BHAGAT","E9090",40000,"rRE ")


Employee1.print_employee_details()
Employee2.print_employee_details()


Employee1.assign_department("OPERATIONS")
Employee1.calculate_salary(45000,52)
Employee2.calculate_salary(60000,60)


print("UPDATED SALARY IS")

Employee1.print_employee_details()
Employee2.print_employee_details()


# ------------------GET HERE MORE INFO--------

#https://realpython.com/inheritance-composition-python/

#********************-----------------------**************
class Employee:
    def __init__(self,id,name) -> None:
        self.id=id
        self.name=name


class SallaryEmployee(Employee):
    def __init__(self, id, name,weekly_salary) -> None:
        super().__init__(id, name)
        self.weekly_salary=weekly_salary
    
    def calculate_salary(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name,hour,rate) -> None:
        super().__init__(id, name)
        self.hour=hour
        self.rate = rate
    def calculate_salary(self):
        return self.hour*self.rate


class ComissionEmployee(SallaryEmployee):
    def __init__(self, id, name, weekly_salary,com) -> None:
        super().__init__(id, name, weekly_salary)
        self.com=com

    def calculate_salary(self):
        fixed= super().calculate_salary()
        return fixed+self.com

class PyRollSystem:
    def calculate(self,employee):
        print('Calculatin Emplyee salary')
        for emp in employee:
            print(f'{emp.id} - {emp.name}')
            print(f'amonut {emp.calculate_salary()}')








salary_employee = SallaryEmployee(1, 'John Smith', 1500)
hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = ComissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = PyRollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commission_employee
])


# ob = Employee()
# raise Employee()
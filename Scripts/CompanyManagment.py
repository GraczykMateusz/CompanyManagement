from Company import Company
from Employee import Employee

class CompanyManagment:

    companies_list = []
    employees_list = []

    @classmethod
    def import_data(cls):
        cls.__import_companies()
        cls.__import_employees()

    @classmethod
    def __import_employees(cls):
        
        with open('../Data/EmployeesData.txt', 'r') as f:
            
            temp = []
            
            for line in f:
                line = line.strip()
                temp.append(line)

                if line == '#':
                    for company in cls.companies_list:
                        if company.get_company_name() == temp[5]:

                            name = temp[0]
                            surname = temp[1]
                            personal_id = temp[2]
                            address = temp[3]
                            birthday = temp[4]
                            company_name = temp[5]
                            salary = temp[6]

                            temp.clear()

                            employee = Employee(name, surname, personal_id, address, birthday, company_name, salary)
                            cls.employees_list.append(employee)

                            break

            temp.clear()

    @classmethod
    def __import_companies(cls):
        
        with open('../Data/CompaniesData.txt', 'r') as f:
            
            temp = []
            
            for line in f:
                line = line.strip()
                temp.append(line)

                if line == '#':
                    founder_name = temp[0]
                    founder_surname = temp[1]
                    company_name = temp[2]
                    company_address = temp[3]
                    tax_id = temp[4] 
                    foundation_year = temp[5]

                    temp.clear()

                    company = Company(founder_name, founder_surname, company_name, company_address, tax_id, foundation_year)
                    cls.companies_list.append(company)

            temp.clear()

    @classmethod
    def check_employee_existance(cls, personal_id):
        for employee in CompanyManagment.employees_list:
            if employee.get_personal_id() == personal_id:
                return True, employee
        return False, None

    @classmethod
    def check_company_existance(cls, company_name):
        for company in CompanyManagment.companies_list:
            if company.get_company_name() == company_name:
                return True, company
        return False, None
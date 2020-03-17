from Company import Company
from Employee import Employee

class CompanyManagmet:

    companies_list = []
    employees_list = []

    @classmethod
    def import_data(cls):
        cls.__import_companies()
        cls.__import_employees()

    @classmethod
    def __import_employees(cls):
        
        temp = []
        
        with open('../Data/EmployeesData.txt', 'r') as f:
            for line in f:
                line = line.strip()
                temp.append(line)
                print(line)

                if line == '#':
                    for company in cls.companies_list:
                        print("Company name: " + company.get_company_name())
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


    @classmethod
    def __import_companies(cls):
        
        temp = []
        
        with open('../Data/CompaniesData.txt', 'r') as f:
            for line in f:
                line = line.strip()
                temp.append(line)
                print(line)

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

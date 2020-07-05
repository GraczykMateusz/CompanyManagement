from Company import Company
from Employee import Employee

class CompanyManagement:
    '''
    CompanyManagement class is responsible for manages companies and
    their employees. It imports companies with employees from
    txt database when program is starting. Checks existence of
    companies and employees on the basis of:
    - company_tax_id for companies;
    - personal_id, company_tax_id(optional) for employees.
    '''
    companies_list = []
    employees_list = []

    @classmethod
    def import_data(cls):
        cls.__import_companies()
        cls.__import_employees()

    @classmethod
    def __import_employees(cls):
        try:
            with open('../Data/EmployeesData.txt', 'r') as f:
                
                lines_arr = []
                
                for line in f:
                    line = line.strip()
                    lines_arr.append(line)

                    if line == '#':
                        for company in cls.companies_list:
                            if company.get_tax_id() == lines_arr[0]:

                                company_tax_id = lines_arr[0]
                                personal_id = lines_arr[1]
                                name = lines_arr[2]
                                surname = lines_arr[3]
                                address = lines_arr[4]
                                birthday = lines_arr[5]
                                salary = lines_arr[6]

                                lines_arr.clear()

                                employee = Employee(
                                    name, surname, personal_id,
                                    address, birthday, company_tax_id,
                                    salary
                                )    
                                cls.employees_list.append(employee)

                                break

                lines_arr.clear()
        except:
            pass

    @classmethod
    def __import_companies(cls):
        try:
            with open('../Data/CompaniesData.txt', 'r') as f:
                
                lines_arr = []
                
                for line in f:
                    line = line.strip()
                    lines_arr.append(line)

                    if line == '#':
                        tax_id = lines_arr[0]
                        founder_name = lines_arr[1]
                        founder_surname = lines_arr[2]
                        company_name = lines_arr[3]
                        company_address = lines_arr[4]
                        foundation_year = lines_arr[5]

                        lines_arr.clear()

                        company = Company(
                            founder_name, founder_surname, company_name,
                            company_address, tax_id, foundation_year
                        )    
                        cls.companies_list.append(company)

                lines_arr.clear()
        except:
            pass

    @classmethod
    def check_employee_existence(cls, personal_id, company_tax_id=None):
        for employee in CompanyManagement.employees_list:
            if (employee.get_personal_id() == personal_id and 
                company_tax_id == None):
                return True, employee

            if (employee.get_personal_id() == personal_id and
                employee.get_company_tax_id() == company_tax_id):
                return True, employee

        return False, None

    @classmethod
    def check_company_existence(cls, company_tax_id):
        for company in CompanyManagement.companies_list:
            if company.get_tax_id() == company_tax_id:
                return True, company
                
        return False, None

    @classmethod
    def add_company(cls):
        pass

    @classmethod
    def delete_company(cls):
        pass

    @classmethod
    def list_companies(cls):
        pass
    
    @classmethod
    def find_company(cls):
        pass

    @classmethod
    def add_employee(cls):
        pass

    @classmethod
    def delete_employee(cls):
        pass

    @classmethod
    def list_employees(cls):
        pass

    @classmethod
    def find_employee(cls):
        pass
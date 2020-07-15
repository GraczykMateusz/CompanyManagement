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
        except BaseException:
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
        except BaseException:
            pass

    @classmethod
    def check_employee_existence(cls, personal_id, company_tax_id=None):
        for employee in CompanyManagement.employees_list:
            if (employee.get_personal_id() == personal_id and
                    company_tax_id is None):
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
    def add_company(
        cls, is_complete, founder_name,
        founder_surname, company_name, company_address,
        tax_id, foundation_year
    ):
        EMPTY = ''
        company_exists, company = CompanyManagement.check_company_existence(
            tax_id)

        if (company_exists == False and
            founder_name != EMPTY and
            founder_surname != EMPTY and
            company_name != EMPTY and
            company_address != EMPTY and
            tax_id != EMPTY and
                foundation_year != EMPTY):

            with open('../Data/CompaniesData.txt', 'a') as f:

                company = Company(
                    founder_name, founder_surname, company_name,
                    company_address, tax_id, foundation_year
                )

                CompanyManagement.companies_list.append(company)

                f.write(company.get_tax_id() + '\n')
                f.write(company.get_founder_name() + '\n')
                f.write(company.get_founder_surname() + '\n')
                f.write(company.get_company_name() + '\n')
                f.write(company.get_company_address() + '\n')
                f.write(company.get_foundation_year() + '\n')
                f.write('#' + '\n')

                is_complete.set("Success")

        elif (company_exists and
              founder_name != EMPTY and
              founder_surname != EMPTY and
              company_name != EMPTY and
              company_address != EMPTY and
              tax_id != EMPTY and
              foundation_year != EMPTY):

            is_complete.set("Already Exists")

        else:
            is_complete.set("Failed")

    @classmethod
    def delete_company(cls, is_complete, tax_id):
        EMPTY = ''
        END_LINE_SYMBOL = '#'
        found_company_to_delete = False
        found_employee_to_delete = False

        company_exists, company = CompanyManagement.check_company_existence(
            tax_id)

        if company_exists:
            # REMOVE ALL EMPLOYEES FROM THE COMPANY [DATABASE]
            with open('../Data/EmployeesData.txt', 'r') as f:
                lines = f.readlines()

            with open('../Data/EmployeesData.txt', 'w') as f:
                for line in lines:
                    if line.strip("\n") == company.get_tax_id():
                        found_employee_to_delete = True

                    if line.strip(
                            "\n") == END_LINE_SYMBOL and found_employee_to_delete:
                        found_employee_to_delete = False
                    elif found_employee_to_delete:
                        pass
                    else:
                        f.write(line)

            # REMOVE ALL EMPLOYEES FROM THE COMPANY [PROGRAM]
            emp_to_del_list = []

            for employee in CompanyManagement.employees_list:
                if employee.get_company_tax_id() == company.get_tax_id():
                    emp_to_del_list.append(employee)

            for emp_to_del in emp_to_del_list:
                    CompanyManagement.employees_list.remove(emp_to_del)

            # DELETE THE COMPANY [DATABASE]
            with open('../Data/CompaniesData.txt', 'r') as f:
                lines = f.readlines()

            with open('../Data/CompaniesData.txt', 'w') as f:
                for line in lines:
                    if line.strip("\n") == company.get_tax_id():
                        found_company_to_delete = True

                    if line.strip(
                            "\n") == END_LINE_SYMBOL and found_company_to_delete:
                        found_company_to_delete = False
                    elif found_company_to_delete:
                        pass
                    else:
                        f.write(line)

            # DELETE THE COMPANY [PROGRAM]
            CompanyManagement.companies_list.remove(company)

            is_complete.set("Success")

        else:
            is_complete.set("Failed")

    @classmethod
    def add_employee(
        cls, is_complete, name,
        surname, personal_id, address,
        birthday, company_tax_id, salary
    ):
        EMPTY = ''
        company_exists, company = CompanyManagement.check_company_existence(
            company_tax_id)
        employee_exists, employee = CompanyManagement.check_employee_existence(
            personal_id, company_tax_id)

        if (company_exists and
                employee_exists == False and
                name != EMPTY and
                surname != EMPTY and
                personal_id != EMPTY and
                address != EMPTY and
                birthday != EMPTY and
                company_tax_id != EMPTY and
                salary != EMPTY
            ):

            with open('../Data/EmployeesData.txt', 'a') as f:

                employee = Employee(name, surname, personal_id,
                                    address, birthday, company_tax_id,
                                    salary
                                    )

                CompanyManagement.employees_list.append(employee)

                f.write(employee.get_company_tax_id() + '\n')
                f.write(employee.get_personal_id() + '\n')
                f.write(employee.get_name() + '\n')
                f.write(employee.get_surname() + '\n')
                f.write(employee.get_address() + '\n')
                f.write(employee.get_birthday() + '\n')
                f.write(employee.get_salary() + '\n')
                f.write('#' + '\n')

                is_complete.set("Success")

        elif (company_exists and
              employee_exists and
              name != EMPTY and
              surname != EMPTY and
              personal_id != EMPTY and
              address != EMPTY and
              birthday != EMPTY and
              company_tax_id != EMPTY and
              salary != EMPTY):

            is_complete.set("Already Exists")

        else:
            is_complete.set("Failed")

    @classmethod
    def delete_employee(
        cls, is_complete, company_tax_id,
        personal_id
    ):
        EMPTY = ''
        END_LINE_SYMBOL = '#'
        found_employee_to_delete = False
        temp_company_tax_id = None

        employee_exists, employee = CompanyManagement.check_employee_existence(
            personal_id, company_tax_id)

        if (employee_exists and
            personal_id != EMPTY and
                company_tax_id != EMPTY):

            with open('../Data/EmployeesData.txt', 'r') as f:
                lines = f.readlines()

            with open('../Data/EmployeesData.txt', 'w') as f:
                for line in lines:

                    if line.strip("\n") == employee.get_company_tax_id():
                        temp_company_tax_id = line.strip("\n")

                    elif line.strip("\n") == employee.get_personal_id() and temp_company_tax_id is not None:
                        found_employee_to_delete = True

                    elif line.strip("\n") == END_LINE_SYMBOL and found_employee_to_delete:
                        found_employee_to_delete = False
                        temp_company_tax_id = None

                    elif found_employee_to_delete:
                        pass

                    elif temp_company_tax_id is not None and found_employee_to_delete == False:
                        f.write(temp_company_tax_id + '\n')
                        temp_company_tax_id = None
                        f.write(line)
                    else:
                        f.write(line)

            CompanyManagement.employees_list.remove(employee)

            is_complete.set("Success")

        else:
            is_complete.set("Failed")

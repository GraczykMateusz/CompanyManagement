import mysql.connector

from CompanyManagement import CompanyManagement


class Server:
    '''
    The class is responsible for connecting to the server to download or send data.
    My default database:
    host="localhost",
    user="root",
    passwd="123",
    database="Company_Management_Database"
    '''
    @classmethod
    def submit_send_database(
        cls, is_complete, host_name=None,
        user_name=None, db=None, password=None
    ):
        try:
            my_db = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=password)

            my_cursor = my_db.cursor()

            drop_old_database = "DROP DATABASE IF EXISTS " + db
            create_new_database = "CREATE DATABASE IF NOT EXISTS " + db

            my_cursor.execute(drop_old_database)
            my_cursor.execute(create_new_database)

            my_db = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=password,
                database=db
            )

            my_cursor = my_db.cursor()

            create_new_companies_table = (
                "CREATE TABLE IF NOT EXISTS Companies "
                "(Tax_ID VARCHAR(255), Founder_Name VARCHAR(255), Founder_Surname VARCHAR(255), "
                "Company_Name VARCHAR(255), Company_Address VARCHAR(255), Foundation_Year VARCHAR(255))")

            create_new_employees_table = (
                "CREATE TABLE IF NOT EXISTS Employees "
                "(Company_Tax_ID VARCHAR(255), Personal_ID VARCHAR(255), Name VARCHAR(255), "
                "Surname VARCHAR(255), Address VARCHAR(255), Birthday VARCHAR(255), "
                "Salary VARCHAR(255))")

            my_cursor.execute(create_new_companies_table)
            my_cursor.execute(create_new_employees_table)

            add_company_sql = (
                "INSERT INTO Companies "
                "(Tax_ID, Founder_Name, Founder_Surname, "
                "Company_Name, Company_Address, Foundation_Year) "
                "VALUES "
                "(%(Tax_ID)s, %(Founder_Name)s, %(Founder_Surname)s, "
                "%(Company_Name)s,%(Company_Address)s, %(Foundation_Year)s)"
            )

            add_employee_sql = (
                "INSERT INTO Employees "
                "(Company_Tax_ID, Personal_ID, Name, "
                "Surname, Address, Birthday, "
                "Salary)"
                "VALUES "
                "(%(Company_Tax_ID)s, %(Personal_ID)s, %(Name)s, "
                "%(Surname)s, %(Address)s, %(Birthday)s, "
                "%(Salary)s)"
            )

            for company in CompanyManagement.companies_list:

                company = {
                    'Tax_ID': company.get_tax_id(),
                    'Founder_Name': company.get_founder_name(),
                    'Founder_Surname': company.get_founder_surname(),
                    'Company_Name': company.get_company_name(),
                    'Company_Address': company.get_company_address(),
                    'Foundation_Year': company.get_foundation_year()
                }

                my_cursor.execute(add_company_sql, company)

            for employee in CompanyManagement.employees_list:

                employee = {
                    'Company_Tax_ID': employee.get_company_tax_id(),
                    'Personal_ID': employee.get_personal_id(),
                    'Name': employee.get_name(),
                    'Surname': employee.get_surname(),
                    'Address': employee.get_address(),
                    'Birthday': employee.get_birthday(),
                    'Salary': employee.get_salary()
                }

                my_cursor.execute(add_employee_sql, employee)

            my_db.commit()

            my_cursor.close()

            is_complete.set("Success")

        except BaseException:
            is_complete.set("Failed")

    @classmethod
    def submit_download_database(
        cls, is_complete, host_name=None,
        user_name=None, db=None, password=None
    ):
        try:
            my_db = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=password,
                database=db)

            my_cursor = my_db.cursor()

            CompanyManagement.companies_list.clear()
            CompanyManagement.employees_list.clear()

            my_cursor.execute("SELECT * FROM Companies")
            result = my_cursor.fetchall()

            # Delete data from txt
            with open('../Data/CompaniesData.txt', 'w') as f:
                pass

            with open('../Data/EmployeesData.txt', 'w') as f:
                pass

            lines_arr = []

            for row in result:
                for data in row:
                    lines_arr.append(data)
                    if len(lines_arr) == 6:
                        tax_id = lines_arr[0]
                        founder_name = lines_arr[1]
                        founder_surname = lines_arr[2]
                        company_name = lines_arr[3]
                        company_address = lines_arr[4]
                        foundation_year = lines_arr[5]

                        CompanyManagement.add_company(
                            is_complete,
                            founder_name,
                            founder_surname,
                            company_name,
                            company_address,
                            tax_id,
                            foundation_year)

                        lines_arr.clear()

            my_cursor.execute("SELECT * FROM Employees")
            result = my_cursor.fetchall()

            for row in result:
                for data in row:
                    lines_arr.append(data)
                    if len(lines_arr) == 7:
                        company_tax_id = lines_arr[0]
                        personal_id = lines_arr[1]
                        name = lines_arr[2]
                        surname = lines_arr[3]
                        address = lines_arr[4]
                        birthday = lines_arr[5]
                        salary = lines_arr[6]

                        CompanyManagement.add_employee(
                            is_complete,
                            name,
                            surname,
                            personal_id,
                            address,
                            birthday,
                            company_tax_id,
                            salary)

                        lines_arr.clear()

            my_cursor.close()

        except BaseException:
            is_complete.set("Failed")

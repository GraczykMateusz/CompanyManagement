class Employee: 
    def __init__(self, name, surname, personal_id, address, birthday, company_tax_id, salary):
        self.__name = name
        self.__surname = surname
        self.__personal_id = personal_id
        self.__address = address
        self.__birthday = birthday
        self.__company_tax_id = company_tax_id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_personal_id(self):
        return self.__personal_id

    def get_address(self):
        return self.__address

    def get_birthday(self):
        return self.__birthday

    def get_company_tax_id(self):
        return self.__company_tax_id

    def get_salary(self):
        return self.__salary
        
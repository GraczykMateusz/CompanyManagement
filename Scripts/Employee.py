class Employee:
    def __init__(self, name, surname, company_name, address, personal_id, birthday):
        self.__name = name
        self.__surname = surname
        self.__company_name = company_name
        self.__address = address
        self.__personal_id = personal_id
        self.__birthday = birthday

        def get_name():
            return self.__name

        def get_surname():
            return self.__surname

        def get_company_name():
            return self.__company_name

        def get_address():
            return self.__address

        def get_personal_id():
            return self.__personal_id
        
        def get_birthday():
            return self.__birthday
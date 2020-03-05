class Company:
    def __init__(self, founder_name, founder_surname, company_name, company_address, tax_id, foundation_year):
        self.__founder_name = founder_name
        self.__founder_surname = founder_surname
        self.__company_name = company_name
        self.__company_address = company_address
        self.__tax_id = tax_id
        self.__foundation_year = foundation_year

        def get_founder_name():
            return self.__founder_name

        def get_founder_surname():
            return self.__founder_surname

        def get_company_name():
            return self.__company_name

        def get_company_address():
            return self.__company_address

        def get_tax_id():
            return self.__tax_id
        
        def get_foundation_year():
            return self.__foundation_year
class Company:
    '''
    Create a company object with data
    '''
    def __init__(
        self, founder_name, founder_surname,
        company_name, company_address, tax_id,
        foundation_year
    ):
        self.__founder_name = founder_name
        self.__founder_surname = founder_surname
        self.__company_name = company_name
        self.__company_address = company_address
        self.__tax_id = tax_id
        self.__foundation_year = foundation_year

    def get_founder_name(self):
        return self.__founder_name

    def get_founder_surname(self):
        return self.__founder_surname

    def get_company_name(self):
        return self.__company_name

    def get_company_address(self):
        return self.__company_address

    def get_tax_id(self):
        return self.__tax_id

    def get_foundation_year(self):
        return self.__foundation_year

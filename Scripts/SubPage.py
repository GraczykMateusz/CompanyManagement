from Company import Company
from Employee import Employee
from Page import Page

import tkinter as tk

class SubPage(Page):

    def __init__(self):
        pass

    company_list = []
    employee_list = []

    def add_company(self):
        self.top = tk.Toplevel()
        self._set_sub_window("600x400")
        self._add_sub_background("../Pictures/Background/raw_background.png")
        
    @classmethod
    def delete_company(cls):
        print('TEST 2')
        pass
    
    @classmethod
    def list_company(cls):
        print('TEST 3')
        pass

    @classmethod
    def find_company(cls):
        print('TEST 4')
        pass

    @classmethod
    def add_employee(cls):
        print('TEST 5')
        pass
    
    @classmethod
    def delete_employee(cls):
        print('TEST 6')
        pass

    @classmethod
    def list_employee(cls):
        print('TEST 7')
        pass

    @classmethod
    def find_employee(cls):
        print('TEST 8')
        pass

    @staticmethod
    def send_database():
        print('TEST 9')
        pass

    @staticmethod
    def download_database():
        print('TEST 10')
        pass

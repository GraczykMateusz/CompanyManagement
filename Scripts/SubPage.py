from Company import Company
from Employee import Employee
from Page import Page

import tkinter as tk

class SubPage(Page):

    def __init__(self):

        self.window_add_company = None
        self.window_delete_company = None
        self.window_find_company = None
        self.window_list_company = None

        self.window_add_employee = None
        self.window_delete_employee = None
        self.window_find_employee = None
        self.window_list_employee = None
    
        self.company_list = []
        self.employee_list = []

    def add_company(self):
        self.window_add_company = self.check_window_existence(self.window_add_company)

        SubPage._set_sub_window(self.window_add_company, "1175x775")
        SubPage._add_sub_background(self.window_add_company, "../Pictures/Background/employee_background_tip.png")
        
    def delete_company(self):
        print('TEST 2')
    
    def list_company(self):
        print('TEST 3')

    def find_company(self):
        print('TEST 4')

    def add_employee(self):
        print('TEST 5')
    
    def delete_employee(self):
        print('TEST 6')

    def list_employee(self):
        print('TEST 7')

    def find_employee(self):
        print('TEST 8')

    def send_database(self):
        print('TEST 9')

    def download_database(self):
        print('TEST 10')

    def check_window_existence(self, top):
        if top is not None:
            top.destroy()
        top = tk.Toplevel()
        return top

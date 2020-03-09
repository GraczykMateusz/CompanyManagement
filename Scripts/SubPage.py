from Company import Company
from Employee import Employee
from Page import Page

import tkinter as tk

class SubPage(Page):

    def __init__(self, geometry="1175x775"):

        self.__window_add_company = None
        self.__window_delete_company = None
        self.__window_find_company = None
        self.__window_list_company = None

        self.__window_add_employee = None
        self.__window_delete_employee = None
        self.__window_find_employee = None
        self.__window_list_employee = None
    
        self.__geometry = geometry

        self.__company_list = []
        self.__employee_list = []

    def add_company(self):
        self.__window_add_company = self.check_window_existence(self.__window_add_company)

        self.window_config(self.__window_add_company, "../Pictures/Background/employee_add_background_tip.png")

        self.entry = tk.Entry(self.__window_add_company)
        self.entry.place(x=370,y=200)
        
    def delete_company(self):
        self.__window_delete_company = self.check_window_existence(self.__window_delete_company)
    
    def list_company(self):
        self.__window_list_company = self.check_window_existence(self.__window_list_company)

    def find_company(self):
        self.__window_find_company = self.check_window_existence(self.__window_find_company)

    def add_employee(self):
        self.__window_add_employee = self.check_window_existence(self.__window_add_employee)
    
    def delete_employee(self):
        self.__window_delete_employee = self.check_window_existence(self.__window_delete_employee)

    def list_employee(self):
        self.__window_list_employee = self.check_window_existence(self.__window_list_employee)

    def find_employee(self):
        self.__window_find_employee = self.check_window_existence(self.__window_find_employee)

    def send_database(self):
        print('TEST 9')

    def download_database(self):
        print('TEST 10')

    def check_window_existence(self, top):
        if top is not None:
            top.destroy()
        top = tk.Toplevel()
        return top

    def window_config(self, top, background):
        SubPage._set_window(top, self.__geometry)
        SubPage._add_background(top, background)
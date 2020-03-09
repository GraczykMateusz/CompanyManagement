from Company import Company
from Employee import Employee
from Page import Page
from StartPage import StartPage

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
        self.__entry_list = []

    def add_company(self):
        self.__window_add_company = self.check_window_existence(self.__window_add_company)

        if StartPage.tip.get() == True:
            self.window_config(self.__window_add_company, "../Pictures/Background/employee_add_background_tip.png", "../Pictures/Icons/company_add_image.png")
        else:
            self.window_config(self.__window_add_company, "../Pictures/Background/employee_add_background.png", "../Pictures/Icons/company_add_image.png")

        self.add_entry(277)
        self.add_entry(366)
        self.add_entry(453)
        self.add_entry(538)
        self.add_entry(630)

        self.add_entry(277, 840)
        self.add_entry(366, 840)

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

    def check_window_tip(self):
        pass

    def check_window_existence(self, top):
        if top is not None:
            top.destroy()
        top = tk.Toplevel()
        return top

    def window_config(self, top, background, path_to_image):
        SubPage._set_window(top, self.__geometry)
        SubPage._add_window_icon(top, path_to_image)
        SubPage._add_background(top, background)

    def add_entry(self, position_y, position_x=485):
        entry = tk.Entry(self.__window_add_company, justify='center', bd=4, width=18, bg='grey', font = ('DejaVu Serif', 13, 'bold'))
        entry.place(x = position_x, y = position_y)
        self.__entry_list.append(entry)
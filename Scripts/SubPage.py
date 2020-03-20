from Page import Page

from Company import Company
from Employee import Employee
from CompanyManagment import CompanyManagmet

import tkinter as tk

class SubPage(Page):

    def __init__(self, geometry="1175x775"):

        self.__geometry = geometry

        self.__window_add_company = None
        self.__window_delete_company = None
        self.__window_find_company = None
        self.__window_list_company = None

        self.__window_add_employee = None
        self.__window_delete_employee = None
        self.__window_find_employee = None
        self.__window_list_employee = None

        self.__entry_list = []

    def view_add_company(self):
        
        self.__window_add_company = self.check_window_existence(self.__window_add_company)
        
        if self.tip == True:
            self.window_config(self.__window_add_company, "../Pictures/Background/company_add_background_tip.png", "../Pictures/Icons/company_add_image.png")
        else:
            self.window_config(self.__window_add_company, "../Pictures/Background/company_add_background.png", "../Pictures/Icons/company_add_image.png")
        
        SubPage.submit_button(self.__window_add_company, self.printujdupe)

        '''
        self.add_entry(self.__window_add_company, 277)
        self.add_entry(self.__window_add_company, 366)
        self.add_entry(self.__window_add_company, 453)
        self.add_entry(self.__window_add_company, 538)
        self.add_entry(self.__window_add_company, 630)
        '''

    def view_delete_company(self):
        self.__window_delete_company = self.check_window_existence(self.__window_delete_company)
    
    def view_list_company(self):
        self.__window_list_company = self.check_window_existence(self.__window_list_company)

    def view_find_company(self):
        self.__window_find_company = self.check_window_existence(self.__window_find_company)

    def view_add_employee(self):
        self.__window_add_employee = self.check_window_existence(self.__window_add_employee)

        if self.tip == True:
            self.window_config(self.__window_add_employee, "../Pictures/Background/employee_add_background_tip.png", "../Pictures/Icons/employee_add_image.png")
        else:
            self.window_config(self.__window_add_employee, "../Pictures/Background/employee_add_background.png", "../Pictures/Icons/employee_add_image.png")
        
        self.name = tk.Variable()
        self.surname = tk.Variable()
        self.personal_id = tk.Variable()
        self.address = tk.Variable()
        self.birthday = tk.Variable()
        self.company_name = tk.Variable()
        self.salary = tk.Variable()

        self.add_entry(self.__window_add_employee, self.name, 277)
        self.add_entry(self.__window_add_employee, self.surname, 366)
        self.add_entry(self.__window_add_employee, self.personal_id, 453)
        self.add_entry(self.__window_add_employee, self.address, 538)
        self.add_entry(self.__window_add_employee, self.birthday, 630)

        self.add_entry(self.__window_add_employee, self.company_name, 277, 840)
        self.add_entry(self.__window_add_employee, self.salary, 366, 840)
        
        SubPage.submit_button(self.__window_add_employee, self.submit_employee)

    def view_delete_employee(self):
        self.__window_delete_employee = self.check_window_existence(self.__window_delete_employee)

    def view_list_employee(self):
        self.__window_list_employee = self.check_window_existence(self.__window_list_employee)

    def view_find_employee(self):
        self.__window_find_employee = self.check_window_existence(self.__window_find_employee)

    def view_send_database(self):        
        print('TEST 9')

    def view_download_database(self):
        print(self.name.get())
        print(self.surname.get())
        print(self.personal_id.get())
        print(self.address.get())
        print(self.birthday.get())
        print(self.company_name.get())
        print(self.salary.get())
        print('TEST 10')

    def check_window_tip(self, tip):
        self.tip = tip

    def check_window_existence(self, top):
        if top is not None:
            top.destroy()
        top = tk.Toplevel()
        return top

    def window_config(self, top, background, path_to_image):
        SubPage._set_window(top, self.__geometry)
        SubPage._add_window_icon(top, path_to_image)
        SubPage._add_background(top, background)
    
    def add_entry(self, window, save, position_y, position_x=485):

        entry = tk.Entry(window, justify='center', bd=4, text=save, width=18, bg='grey', font = ('DejaVu Serif', 13, 'bold'))
        entry.place(x = position_x, y = position_y)
        self.__entry_list.append(entry)

    def submit_button(self, event):
        self.submit_button = tk.Button(self, command=event, text="SUBMIT", font = ('DejaVu Serif', 16, 'bold'))
        self.submit_button.place(x=1030, y=720)

    def submit_employee(self):

        for company in CompanyManagmet.companies_list:
            if company.get_company_name() == self.company_name.get():
                with open('../Data/EmployeesData.txt', 'a') as f:
                
                    employee = Employee(self.name.get(),
                                         self.surname.get(),
                                          self.personal_id.get(),
                                           self.address.get(),
                                            self.birthday.get(),
                                             self.company_name.get(),
                                              self.salary.get())

                    CompanyManagmet.employees_list.append(employee)

                    f.write(employee.get_name() + '\n')
                    f.write(employee.get_surname() + '\n')
                    f.write(employee.get_personal_id() + '\n')
                    f.write(employee.get_address() + '\n')
                    f.write(employee.get_birthday() + '\n')
                    f.write(employee.get_company_name() + '\n')
                    f.write(employee.get_salary() + '\n')
                    f.write('#' + '\n')

                    break

    def submit_company(self):
        company = Company()
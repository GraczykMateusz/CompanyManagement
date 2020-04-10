from Page import Page
from Company import Company
from Employee import Employee
from CompanyManagment import CompanyManagment

import tkinter as tk
import time as tm

#
import mysql.connector
#

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

        self.__window_download_database = None
        self.__window_send_database = None

        self.__entry_list = []

    def view_add_company(self):
        
        self.__window_add_company = self.check_window_existence(self.__window_add_company)
        
        if self.tip == True:
            self.window_config(self.__window_add_company, "../Pictures/Background/company_add_background_tip.png", "../Pictures/Icons/company_add_image.png")
        else:
            self.window_config(self.__window_add_company, "../Pictures/Background/company_add_background.png", "../Pictures/Icons/company_add_image.png")

        self.founder_name = tk.Variable()
        self.founder_surname = tk.Variable()
        self.company_name = tk.Variable()
        self.company_address = tk.Variable()
        self.tax_id = tk.Variable()
        self.foundation_year = tk.Variable()

        self.add_entry(self.__window_add_company, self.founder_name, 275)
        self.add_entry(self.__window_add_company, self.founder_surname, 361)
        self.add_entry(self.__window_add_company, self.company_name, 452)
        self.add_entry(self.__window_add_company, self.company_address, 539)
        self.add_entry(self.__window_add_company, self.tax_id, 622)
        self.add_entry(self.__window_add_company, self.foundation_year, 709)
        
        SubPage.submit_button(self.__window_add_company, self.submit_add_company)

    def view_delete_company(self):
        self.__window_delete_company = self.check_window_existence(self.__window_delete_company)

        if self.tip == True:
            self.window_config(self.__window_delete_company, "../Pictures/Background/company_delete_background_tip.png", "../Pictures/Icons/company_delete_image.png")
        else:
            self.window_config(self.__window_delete_company, "../Pictures/Background/company_delete_background.png", "../Pictures/Icons/company_delete_image.png")
        
        self.tax_id = tk.Variable()

        self.add_entry(self.__window_delete_company, self.tax_id, 320)

        SubPage.submit_button(self.__window_delete_company, self.submit_delete_company)


    def view_list_company(self):
        self.__window_list_company = self.check_window_existence(self.__window_list_company)

        self.window_config(self.__window_list_company, "../Pictures/Background/raw_background.png", "../Pictures/Icons/company_list_image.png")

        self.list_box_frame = tk.Frame(self.__window_list_company)
        self.list_box_frame.place(relx=0.3, rely=0.6, anchor='center')
        
        self.list_box = tk.Listbox(self.list_box_frame, width=30, height=16, bg='black', fg='white', font = ('DejaVu Serif', 20, 'bold'))
        self.list_box.pack(side="left", fill="y")

        counter = 1
        for company in CompanyManagment.companies_list:
            self.list_box.insert(tk.END, str(counter) + ".COMPANY")
            self.list_box.insert(tk.END, company.get_founder_name() + ' ' + company.get_founder_surname())
            self.list_box.insert(tk.END, company.get_company_name())
            self.list_box.insert(tk.END, company.get_company_address())
            self.list_box.insert(tk.END, company.get_tax_id())
            self.list_box.insert(tk.END, company.get_foundation_year())
            self.list_box.insert(tk.END, '____________________________________________')
            counter += 1
        
        self.scrollbar = tk.Scrollbar(self.list_box_frame, orient="vertical")
        self.scrollbar.config(command=self.list_box.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.list_box.config(yscrollcommand=self.scrollbar.set)

    def view_find_company(self):
        self.__window_find_company = self.check_window_existence(self.__window_find_company)

        self.window_config(self.__window_find_company, "../Pictures/Background/company_find_background.png", "../Pictures/Icons/company_find_image.png")

        self.list_box_frame = tk.Frame(self.__window_find_company)
        self.list_box_frame.place(relx=0.3, rely=0.6, anchor='center')
        
        self.list_box = tk.Listbox(self.list_box_frame, width=30, height=16, bg='black', fg='white', font = ('DejaVu Serif', 20, 'bold'))
        self.list_box.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self.list_box_frame, orient="vertical")
        self.scrollbar.config(command=self.list_box.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.list_box.config(yscrollcommand=self.scrollbar.set)

        self.tax_id = tk.Variable()

        self.add_entry(self.__window_find_company, self.tax_id, 424, 840)

        SubPage.submit_button(self.__window_find_company, self.submit_find_company)

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
        self.company_tax_id = tk.Variable()
        self.salary = tk.Variable()

        self.add_entry(self.__window_add_employee, self.name, 277)
        self.add_entry(self.__window_add_employee, self.surname, 366)
        self.add_entry(self.__window_add_employee, self.personal_id, 453)
        self.add_entry(self.__window_add_employee, self.address, 538)
        self.add_entry(self.__window_add_employee, self.birthday, 630)

        self.add_entry(self.__window_add_employee, self.company_tax_id, 277, 840)
        self.add_entry(self.__window_add_employee, self.salary, 366, 840)
        
        SubPage.submit_button(self.__window_add_employee, self.submit_add_employee)

    def view_delete_employee(self):
        self.__window_delete_employee = self.check_window_existence(self.__window_delete_employee)
        
        if self.tip == True:
            self.window_config(self.__window_delete_employee, "../Pictures/Background/employee_delete_background_tip.png", "../Pictures/Icons/employee_delete_image.png")
        else:
            self.window_config(self.__window_delete_employee, "../Pictures/Background/employee_delete_background.png", "../Pictures/Icons/employee_delete_image.png")

        self.personal_id = tk.Variable()
        self.company_tax_id = tk.Variable()

        self.add_entry(self.__window_delete_employee, self.company_tax_id, 322)
        self.add_entry(self.__window_delete_employee, self.personal_id, 406)

        SubPage.submit_button(self.__window_delete_employee, self.submit_delete_employee)

    def view_list_employee(self):
        self.__window_list_employee = self.check_window_existence(self.__window_list_employee)

        self.window_config(self.__window_list_employee, "../Pictures/Background/raw_background.png", "../Pictures/Icons/employee_list_image.png")

        self.list_box_frame = tk.Frame(self.__window_list_employee)
        self.list_box_frame.place(relx=0.3, rely=0.6, anchor='center')
        
        self.list_box = tk.Listbox(self.list_box_frame, width=30, height=16, bg='black', fg='white', font = ('DejaVu Serif', 20, 'bold'))
        self.list_box.pack(side="left", fill="y")

        counter = 1
        for employee in CompanyManagment.employees_list:
            self.list_box.insert(tk.END, str(counter) + ".COMPANY")
            self.list_box.insert(tk.END, employee.get_name() + ' ' + employee.get_surname())
            self.list_box.insert(tk.END, employee.get_personal_id())
            self.list_box.insert(tk.END, employee.get_address())
            self.list_box.insert(tk.END, employee.get_birthday())
            self.list_box.insert(tk.END, employee.get_company_tax_id())
            self.list_box.insert(tk.END, employee.get_salary())
            self.list_box.insert(tk.END, '____________________________________________')
            counter += 1
        
        self.scrollbar = tk.Scrollbar(self.list_box_frame, orient="vertical")
        self.scrollbar.config(command=self.list_box.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.list_box.config(yscrollcommand=self.scrollbar.set)
        
    def view_find_employee(self):
        self.__window_find_employee = self.check_window_existence(self.__window_find_employee)

        self.window_config(self.__window_find_employee, "../Pictures/Background/employee_find_background.png", "../Pictures/Icons/employee_find_image.png")

        self.list_box_frame = tk.Frame(self.__window_find_employee)
        self.list_box_frame.place(relx=0.3, rely=0.6, anchor='center')
        
        self.list_box = tk.Listbox(self.list_box_frame, width=30, height=16, bg='black', fg='white', font = ('DejaVu Serif', 20, 'bold'))
        self.list_box.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self.list_box_frame, orient="vertical")
        self.scrollbar.config(command=self.list_box.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.list_box.config(yscrollcommand=self.scrollbar.set)

        self.personal_id = tk.Variable()
        self.company_tax_id = tk.Variable()

        self.add_entry(self.__window_find_employee, self.personal_id, 310, 840)
        self.add_entry(self.__window_find_employee, self.company_tax_id, 424, 840)

        SubPage.submit_button(self.__window_find_employee, self.submit_find_employee)

    def view_send_database(self): 
        self.__window_send_database = self.check_window_existence(self.__window_send_database)

        if self.tip == True:
            self.window_config(self.__window_send_database, "../Pictures/Background/database_send_background_tip.png", "../Pictures/Icons/employee_find_image.png")
        else:
            self.window_config(self.__window_send_database, "../Pictures/Background/database_send_background.png", "../Pictures/Icons/employee_find_image.png")

        self.host = tk.Variable()
        self.user = tk.Variable()
        self.database = tk.Variable()
        self.password = tk.Variable()

        self.add_entry(self.__window_send_database, self.host, 313)
        self.add_entry(self.__window_send_database, self.user, 410)
        self.add_entry(self.__window_send_database, self.database, 506)
        self.add_entry(self.__window_send_database, self.password, 603)

        SubPage.submit_button(self.__window_send_database, self.submit_send_database)

    def view_download_database(self):
        print('TEST 10')

    def check_window_tip(self, tip):
        self.tip = tip

    def check_window_existence(self, top):
        if top is not None:
            top.destroy()

        self.__entry_list.clear()

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

    def submit_add_employee(self):
        empty = ''
        company_exists, company = CompanyManagment.check_company_existance(self.company_tax_id.get())
        employee_exists, employee = CompanyManagment.check_employee_existance(self.personal_id.get(), self.company_tax_id.get())

        if (company_exists == True and
            employee_exists == False and
            self.name.get() != empty and
            self.surname.get() != empty and
            self.personal_id.get() != empty and
            self.address.get() != empty and
            self.birthday.get() != empty and
            self.company_tax_id.get() != empty and
            self.salary.get() != empty):

            with open('../Data/EmployeesData.txt', 'a') as f:
            
                employee = Employee(self.name.get(),
                                    self.surname.get(),
                                    self.personal_id.get(),
                                    self.address.get(),
                                        self.birthday.get(),
                                        self.company_tax_id.get(),
                                        self.salary.get())

                CompanyManagment.employees_list.append(employee)

                f.write(employee.get_company_tax_id() + '\n')
                f.write(employee.get_personal_id() + '\n')
                f.write(employee.get_name() + '\n')
                f.write(employee.get_surname() + '\n')
                f.write(employee.get_address() + '\n')
                f.write(employee.get_birthday() + '\n')
                f.write(employee.get_salary() + '\n')
                f.write('#' + '\n')

                self.__success_image = tk.PhotoImage(file = '../Pictures/Icons/success.png')
                self.__success = tk.Label(self.__window_add_employee, borderwidth=0, highlightthickness=0, image = self.__success_image)
                self.__success.place(x=1038, y=695)
            
                self.__window_add_employee.after(3000, self.__success.destroy)

        elif (company_exists == True and
            employee_exists == True and
            self.name.get() != empty and
            self.surname.get() != empty and
            self.personal_id.get() != empty and
            self.address.get() != empty and
            self.birthday.get() != empty and
            self.company_tax_id.get() != empty and
            self.salary.get() != empty):

            self.__already_exists_image = tk.PhotoImage(file = '../Pictures/Icons/already_exists.png')
            self.__already_exists = tk.Label(self.__window_add_employee, borderwidth=0, highlightthickness=0, image = self.__already_exists_image)
            self.__already_exists.place(x=1038, y=695)
        
            self.__window_add_employee.after(3000, self.__already_exists.destroy)

        else:
            self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
            self.__failed = tk.Label(self.__window_add_employee, borderwidth=0, highlightthickness=0, image = self.__failed_image)
            self.__failed.place(x=1038, y=695)
            
            self.__window_add_employee.after(3000, self.__failed.destroy)
        
    def submit_delete_employee(self):
        EMPTY = ''
        END_LINE_SYMBOL = '#'
        found_employee_to_delete = False
        temp_company_tax_id = None

        employee_exists, employee = CompanyManagment.check_employee_existance(self.personal_id.get(), self.company_tax_id.get())

        if (employee_exists == True and
            self.personal_id.get() != EMPTY and
            self.company_tax_id.get() != EMPTY):

            with open('../Data/EmployeesData.txt', 'r') as f:
                lines = f.readlines()
                
            with open('../Data/EmployeesData.txt', 'w') as f:
                for line in lines:
                    
                    if line.strip("\n") == employee.get_company_tax_id():
                        temp_company_tax_id = line.strip("\n")

                    elif line.strip("\n") == employee.get_personal_id() and temp_company_tax_id != None :
                        found_employee_to_delete = True
                    
                    elif line.strip("\n") == END_LINE_SYMBOL and found_employee_to_delete == True:
                        found_employee_to_delete = False
                        temp_company_tax_id = None

                    elif found_employee_to_delete == True:
                        pass

                    elif temp_company_tax_id != None and found_employee_to_delete == False:
                        f.write(temp_company_tax_id + '\n')
                        temp_company_tax_id = None
                        f.write(line)
                    else:
                        f.write(line)

            CompanyManagment.employees_list.remove(employee)

            self.__success_image = tk.PhotoImage(file = '../Pictures/Icons/success.png')
            self.__success = tk.Label(self.__window_delete_employee, borderwidth=0, highlightthickness=0, image = self.__success_image)
            self.__success.place(x=1038, y=695)
        
            self.__window_delete_employee.after(3000, self.__success.destroy)

        else:
                self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
                self.__failed = tk.Label(self.__window_delete_employee, borderwidth=0, highlightthickness=0, image = self.__failed_image)
                self.__failed.place(x=1038, y=695)
            
                self.__window_delete_employee.after(3000, self.__failed.destroy)

    def submit_add_company(self):
        EMPTY = ''
        company_exists, company = CompanyManagment.check_company_existance(self.tax_id.get())

        if (company_exists == False and
            self.founder_name.get()  != EMPTY and
            self.founder_surname.get() != EMPTY and
            self.company_name.get() != EMPTY and
            self.company_address.get() != EMPTY and
            self.tax_id.get() != EMPTY and
            self.foundation_year.get() != EMPTY):

            with open('../Data/CompaniesData.txt', 'a') as f:
            
                company = Company(self.founder_name.get(), self.founder_surname.get(), self.company_name.get(), self.company_address.get(), self.tax_id.get(), self.foundation_year.get())
                
                CompanyManagment.companies_list.append(company)

                f.write(company.get_tax_id() + '\n')
                f.write(company.get_founder_name() + '\n')
                f.write(company.get_founder_surname() + '\n')
                f.write(company.get_company_name() + '\n')
                f.write(company.get_company_address() + '\n')
                f.write(company.get_foundation_year() + '\n')
                f.write('#' + '\n')

                self.__success_image = tk.PhotoImage(file = '../Pictures/Icons/success.png')
                self.__success = tk.Label(self.__window_add_company, borderwidth=0, highlightthickness=0, image = self.__success_image)
                self.__success.place(x=1038, y=695)
            
                self.__window_add_company.after(3000, self.__success.destroy)
        
        elif (company_exists == True and
            self.founder_name.get() != EMPTY and
            self.founder_surname.get() != EMPTY and
            self.company_name.get() != EMPTY and
            self.company_address.get() != EMPTY and
            self.tax_id.get() != EMPTY and
            self.foundation_year.get() != EMPTY):

            self.__already_exists_image = tk.PhotoImage(file = '../Pictures/Icons/already_exists.png')
            self.__already_exists = tk.Label(self.__window_add_company, borderwidth=0, highlightthickness=0, image = self.__already_exists_image)
            self.__already_exists.place(x=1038, y=695)
        
            self.__window_add_company.after(3000, self.__already_exists.destroy)

        else:
            self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
            self.__failed = tk.Label(self.__window_add_company, borderwidth=0, highlightthickness=0, image = self.__failed_image)
            self.__failed.place(x=1038, y=695)
        
            self.__window_add_company.after(3000, self.__failed.destroy)

    def submit_delete_company(self):
        EMPTY = ''
        END_LINE_SYMBOL = '#'
        found_company_to_delete = False
        found_employee_to_delete = False
        
        company_exists, company = CompanyManagment.check_company_existance(self.tax_id.get())

        if company_exists == True:
            # REMOVE ALL EMPLOYEES FROM THE COMPANY [DATABASE]
            with open('../Data/EmployeesData.txt', 'r') as f:
                lines = f.readlines()
                
            with open('../Data/EmployeesData.txt', 'w') as f:
                for line in lines:
                    if line.strip("\n") == company.get_tax_id():
                        found_employee_to_delete = True

                    if line.strip("\n") == END_LINE_SYMBOL and found_employee_to_delete == True:
                        found_employee_to_delete = False
                    elif found_employee_to_delete == True:
                        pass
                    else:
                        f.write(line)

            # REMOVE ALL EMPLOYEES FROM THE COMPANY [PROGRAM]
            for employee in CompanyManagment.employees_list:
                if employee.get_company_tax_id() == company.get_tax_id():
                    CompanyManagment.employees_list.remove(employee)

            # DELETE THE COMPANY [DATABASE]
            with open('../Data/CompaniesData.txt', 'r') as f:
                lines = f.readlines()
                
            with open('../Data/CompaniesData.txt', 'w') as f:
                for line in lines:
                    if line.strip("\n") == company.get_tax_id():
                        found_company_to_delete = True

                    if line.strip("\n") == END_LINE_SYMBOL and found_company_to_delete == True:
                        found_company_to_delete = False
                    elif found_company_to_delete == True:
                        pass
                    else:
                        f.write(line)    

            # DELETE THE COMPANY [PROGRAM]
            CompanyManagment.companies_list.remove(company)

            self.__success_image = tk.PhotoImage(file = '../Pictures/Icons/success.png')
            self.__success = tk.Label(self.__window_delete_company, borderwidth=0, highlightthickness=0, image = self.__success_image)
            self.__success.place(x=1038, y=695)
        
            self.__window_delete_company.after(3000, self.__success.destroy)

        else:
            self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
            self.__failed = tk.Label(self.__window_delete_company, borderwidth=0, highlightthickness=0, image = self.__failed_image)
            self.__failed.place(x=1038, y=695)
        
            self.__window_delete_company.after(3000, self.__failed.destroy)

    def submit_find_employee(self):
        EMPTY = ''
        if self.personal_id.get() != EMPTY and self.company_tax_id.get() != EMPTY:
            employee_exists, employee = CompanyManagment.check_employee_existance(self.personal_id.get(), self.company_tax_id.get())
        
            if employee_exists == True:

                self.list_box_frame = tk.Frame(self.__window_find_employee)
                self.list_box_frame.place(relx=0.3, rely=0.6, anchor='center')
                
                self.list_box = tk.Listbox(self.list_box_frame, width=30, height=16, bg='black', fg='white', font = ('DejaVu Serif', 20, 'bold'))
                self.list_box.pack(side="left", fill="y")

                self.list_box.insert(tk.END, "EMPLOYEE")
                self.list_box.insert(tk.END, employee.get_name() + ' ' + employee.get_surname())
                self.list_box.insert(tk.END, employee.get_personal_id())
                self.list_box.insert(tk.END, employee.get_address())
                self.list_box.insert(tk.END, employee.get_birthday())
                self.list_box.insert(tk.END, employee.get_company_tax_id())
                self.list_box.insert(tk.END, employee.get_salary())
                self.list_box.insert(tk.END, '____________________________________________')
            
                self.scrollbar = tk.Scrollbar(self.list_box_frame, orient="vertical")
                self.scrollbar.config(command=self.list_box.yview)
                self.scrollbar.pack(side="right", fill="y")

                self.list_box.config(yscrollcommand=self.scrollbar.set)

                self.__success_image = tk.PhotoImage(file = '../Pictures/Icons/success.png')
                self.__success = tk.Label(self.__window_find_employee, borderwidth=0, highlightthickness=0, image = self.__success_image)
                self.__success.place(x=1038, y=695)
            
                self.__window_find_employee.after(3000, self.__success.destroy)

            else:
                self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
                self.__failed = tk.Label(self.__window_find_employee, borderwidth=0, highlightthickness=0, image = self.__failed_image)
                self.__failed.place(x=1038, y=695)
            
                self.__window_find_employee.after(3000, self.__failed.destroy)

        elif self.personal_id.get() != EMPTY and self.company_tax_id.get() == EMPTY:
            employee_exists, employee = CompanyManagment.check_employee_existance(self.personal_id.get())

            if employee_exists == True:

                self.list_box_frame = tk.Frame(self.__window_find_employee)
                self.list_box_frame.place(relx=0.3, rely=0.6, anchor='center')
                
                self.list_box = tk.Listbox(self.list_box_frame, width=30, height=16, bg='black', fg='white', font = ('DejaVu Serif', 20, 'bold'))
                self.list_box.pack(side="left", fill="y")

                counter = 0

                for employee in CompanyManagment.employees_list:
                    if employee.get_personal_id() == self.personal_id.get():
                        self.list_box.insert(tk.END, str(counter) + ".EMPLOYEE")
                        self.list_box.insert(tk.END, employee.get_name() + ' ' + employee.get_surname())
                        self.list_box.insert(tk.END, employee.get_personal_id())
                        self.list_box.insert(tk.END, employee.get_address())
                        self.list_box.insert(tk.END, employee.get_birthday())
                        self.list_box.insert(tk.END, employee.get_company_tax_id())
                        self.list_box.insert(tk.END, employee.get_salary())
                        self.list_box.insert(tk.END, '____________________________________________')
                        counter += 1
                
                self.scrollbar = tk.Scrollbar(self.list_box_frame, orient="vertical")
                self.scrollbar.config(command=self.list_box.yview)
                self.scrollbar.pack(side="right", fill="y")

                self.list_box.config(yscrollcommand=self.scrollbar.set)

                self.__success_image = tk.PhotoImage(file = '../Pictures/Icons/success.png')
                self.__success = tk.Label(self.__window_find_employee, borderwidth=0, highlightthickness=0, image = self.__success_image)
                self.__success.place(x=1038, y=695)
            
                self.__window_find_employee.after(3000, self.__success.destroy)

            else:
                self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
                self.__failed = tk.Label(self.__window_find_employee, borderwidth=0, highlightthickness=0, image = self.__failed_image)
                self.__failed.place(x=1038, y=695)
            
                self.__window_find_employee.after(3000, self.__failed.destroy)

        else:
            self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
            self.__failed = tk.Label(self.__window_find_employee, borderwidth=0, highlightthickness=0, image = self.__failed_image)
            self.__failed.place(x=1038, y=695)
        
            self.__window_find_employee.after(3000, self.__failed.destroy)

    def submit_find_company(self):
        EMPTY = ''

        if self.tax_id.get() != EMPTY:
            company_exists, company = CompanyManagment.check_company_existance(self.tax_id.get())
        
            if company_exists == True:

                self.list_box_frame = tk.Frame(self.__window_find_company)
                self.list_box_frame.place(relx=0.3, rely=0.6, anchor='center')
                
                self.list_box = tk.Listbox(self.list_box_frame, width=30, height=16, bg='black', fg='white', font = ('DejaVu Serif', 20, 'bold'))
                self.list_box.pack(side="left", fill="y")

                self.list_box.insert(tk.END, "COMPANY")
                self.list_box.insert(tk.END, company.get_founder_name() + ' ' + company.get_founder_surname())
                self.list_box.insert(tk.END, company.get_company_name())
                self.list_box.insert(tk.END, company.get_company_address())
                self.list_box.insert(tk.END, company.get_tax_id())
                self.list_box.insert(tk.END, company.get_foundation_year())
                self.list_box.insert(tk.END, '____________________________________________')
                            
                self.scrollbar = tk.Scrollbar(self.list_box_frame, orient="vertical")
                self.scrollbar.config(command=self.list_box.yview)
                self.scrollbar.pack(side="right", fill="y")

                self.list_box.config(yscrollcommand=self.scrollbar.set)

                self.__success_image = tk.PhotoImage(file = '../Pictures/Icons/success.png')
                self.__success = tk.Label(self.__window_find_company, borderwidth=0, highlightthickness=0, image = self.__success_image)
                self.__success.place(x=1038, y=695)
            
                self.__window_find_company.after(3000, self.__success.destroy)
            
            else:
                self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
                self.__failed = tk.Label(self.__window_find_employee, borderwidth=0, highlightthickness=0, image = self.__failed_image)
                self.__failed.place(x=1038, y=695)
            
                self.__window_find_employee.after(3000, self.__failed.destroy)

        else:
            self.__failed_image = tk.PhotoImage(file = '../Pictures/Icons/failed.png')
            self.__failed = tk.Label(self.__window_find_employee, borderwidth=0, highlightthickness=0, image = self.__failed_image)
            self.__failed.place(x=1038, y=695)
        
            self.__window_find_employee.after(3000, self.__failed.destroy)

#------------------------------------------

    def submit_send_database(self, host_name="localhost", user_name="root", password="123"):

        my_db = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
        )

        my_cursor = my_db.cursor()

        drop_old_database = "DROP DATABASE IF EXISTS Company_Managment_Database"
        create_new_database = "CREATE DATABASE IF NOT EXISTS Company_Managment_Database"

        my_cursor.execute(drop_old_database)
        my_cursor.execute(create_new_database)

        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123",
            database="Company_Managment_Database"
        )

        my_cursor = my_db.cursor()
        
        create_new_companies_table = (
            "CREATE TABLE IF NOT EXISTS Companies "
            "(Founder_Name VARCHAR(255), Founder_Surname VARCHAR(255), Company_Name VARCHAR(255), "
            "Company_Address VARCHAR(255), Tax_ID VARCHAR(255), Foundation_Year VARCHAR(255))"
        )
        
        create_new_employees_table = (
            "CREATE TABLE IF NOT EXISTS Employees "
            "(Name VARCHAR(255), Surname VARCHAR(255), Personal_ID VARCHAR(255), "
            "Address VARCHAR(255), Birthday VARCHAR(255), Company_Tax_ID VARCHAR(255), "
            "Salary VARCHAR(255))"
        )
        
        my_cursor.execute(create_new_companies_table)
        my_cursor.execute(create_new_employees_table)
        
        add_company_sql = (
            "INSERT INTO Companies "
            "(Founder_Name, Founder_Surname, Company_Name, "
            "Company_Address, Tax_ID, Foundation_Year) "
            "VALUES "
            "(%(Founder_Name)s, %(Founder_Surname)s, %(Company_Name)s, "
            "%(Company_Address)s, %(Tax_ID)s, %(Foundation_Year)s)"
        )
        
        add_employee_sql = (
            "INSERT INTO Employees "
            "(Name, Surname, Personal_ID, Address, "
            "Birthday, Company_Tax_ID, Salary) "
            "VALUES "
            "(%(Name)s, %(Surname)s, %(Personal_ID)s, "
            "%(Address)s, %(Birthday)s, %(Company_Tax_ID)s, "
            "%(Salary)s)"
        )

        for company in CompanyManagment.companies_list:
            
            company = {
                'Founder_Name': company.get_founder_name(),
                'Founder_Surname': company.get_founder_surname(),
                'Company_Name': company.get_company_name(),
                'Company_Address': company.get_company_address(),
                'Tax_ID': company.get_tax_id(),
                'Foundation_Year': company.get_foundation_year()
            }
            
            my_cursor.execute(add_company_sql, company)       
        
        for employee in CompanyManagment.employees_list:

            employee = {
                'Name': employee.get_name(),
                'Surname': employee.get_surname(),
                'Personal_ID': employee.get_personal_id(),
                'Address': employee.get_address(),
                'Birthday': employee.get_birthday(),
                'Company_Tax_ID': employee.get_company_tax_id(),
                'Salary': employee.get_salary()
            }

            my_cursor.execute(add_employee_sql, employee)

        my_db.commit()
        
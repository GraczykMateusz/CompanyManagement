import tkinter as tk
import time as tm

from Page import Page
from CompanyManagement import CompanyManagement
from Server import Server


class SubPage(Page):
    '''
    The SubPage class is responsible for subwindows display
    '''

    def __init__(self, geometry="1175x775"):

        self.__geometry = geometry

        self.__entry_list = []

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

        self.__comp_add_is_complete = tk.StringVar()
        self.__comp_del_is_complete = tk.StringVar()

        self.__emp_add_is_complete = tk.StringVar()
        self.__emp_del_is_complete = tk.StringVar()

        self.__server_download_is_complete = tk.StringVar()
        self.__server_send_is_complete = tk.StringVar()

    def checks_tip(self, tip):
        self.__tip = tip

    def __check_window_existence(self, top):
        if top is not None:
            top.destroy()

        self.__entry_list.clear()

        top = tk.Toplevel()
        return top

    def __window_config(self, top, background, path_to_image):
        SubPage._set_window(top, self.__geometry)
        SubPage._add_window_icon(top, path_to_image)
        SubPage._add_background(top, background)

    def __add_entry(self, window, save, position_y, position_x=485):
        entry = tk.Entry(
            window, justify='center', bd=4,
            text=save, width=18, bg='grey',
            font=('DejaVu Serif', 13, 'bold')
        )
        entry.place(x=position_x, y=position_y)
        self.__entry_list.append(entry)

    def __submit_button(self, event):
        self.__submit_button = tk.Button(
            self, command=event, text="SUBMIT",
            font=('DejaVu Serif', 16, 'bold')
        )
        self.__submit_button.place(x=1030, y=720)

    def complete(self, window, is_complete):
        if is_complete.get() == "Success":
            self.__image = tk.PhotoImage(
                file='../Pictures/Icons/success.png'
            )

        elif is_complete.get() == "Failed":
            self.__image = tk.PhotoImage(
                file='../Pictures/Icons/failed.png'
            )

        else:
            self.__image = tk.PhotoImage(
                file='../Pictures/Icons/already_exists.png'
            )

        self.__complete = tk.Label(
            window, borderwidth=0, highlightthickness=0,
            image=self.__image
        )
        self.__complete.place(x=1038, y=695)

        window.after(3000, self.__complete.destroy)

#---------------------------- View Methods START ----------------------------#

    def view_add_company(self):
        self.__window_add_company = self.__check_window_existence(
            self.__window_add_company)

        if self.__tip:
            self.__window_config(
                self.__window_add_company,
                "../Pictures/Background/company_add_background_tip.png",
                "../Pictures/Icons/company_add_image.png"
            )
        else:
            self.__window_config(
                self.__window_add_company,
                "../Pictures/Background/company_add_background.png",
                "../Pictures/Icons/company_add_image.png"
            )

        self.__founder_name = tk.Variable()
        self.__founder_surname = tk.Variable()
        self.__company_name = tk.Variable()
        self.__company_address = tk.Variable()
        self.__tax_id = tk.Variable()
        self.__foundation_year = tk.Variable()

        self.__add_entry(self.__window_add_company, self.__founder_name, 275)
        self.__add_entry(
            self.__window_add_company,
            self.__founder_surname,
            361)
        self.__add_entry(self.__window_add_company, self.__company_name, 452)
        self.__add_entry(
            self.__window_add_company,
            self.__company_address,
            539)
        self.__add_entry(self.__window_add_company, self.__tax_id, 622)
        self.__add_entry(
            self.__window_add_company,
            self.__foundation_year,
            709)

        SubPage.__submit_button(
            self.__window_add_company,
            lambda: CompanyManagement.add_company(
                self.__comp_add_is_complete,
                self.__founder_name.get(),
                self.__founder_surname.get(),
                self.__company_name.get(),
                self.__company_address.get(),
                self.__tax_id.get(),
                self.__foundation_year.get()))

        self.__comp_add_is_complete.trace(
            'w', lambda var, indx, mode: self.complete(
                self.__window_add_company, self.__comp_add_is_complete))

    def view_delete_company(self):
        self.__window_delete_company = self.__check_window_existence(
            self.__window_delete_company)

        if self.__tip:
            self.__window_config(
                self.__window_delete_company,
                "../Pictures/Background/company_delete_background_tip.png",
                "../Pictures/Icons/company_delete_image.png")
        else:
            self.__window_config(
                self.__window_delete_company,
                "../Pictures/Background/company_delete_background.png",
                "../Pictures/Icons/company_delete_image.png")

        self.__tax_id = tk.Variable()

        self.__add_entry(self.__window_delete_company, self.__tax_id, 320)

        SubPage.__submit_button(
            self.__window_delete_company,
            lambda: CompanyManagement.delete_company(
                self.__comp_del_is_complete, self.__tax_id.get()
            )
        )

        self.__comp_del_is_complete.trace(
            'w', lambda var, indx, mode: self.complete(
                self.__window_delete_company, self.__comp_del_is_complete))

    def view_list_company(self):
        self.__window_list_company = self.__check_window_existence(
            self.__window_list_company)

        self.__window_config(
            self.__window_list_company,
            "../Pictures/Background/company_list_background.png",
            "../Pictures/Icons/company_list_image.png")

        self.__list_box_frame = tk.Frame(self.__window_list_company)
        self.__list_box_frame.place(relx=0.3, rely=0.6, anchor='center')

        self.__list_box = tk.Listbox(
            self.__list_box_frame,
            width=30,
            height=16,
            bg='black',
            fg='white',
            font=(
                'DejaVu Serif',
                20,
                'bold'))
        self.__list_box.pack(side="left", fill="y")

        counter = 0
        for company in CompanyManagement.companies_list:
            counter += 1
            self.__list_box.insert(tk.END, str(counter) + ".COMPANY")
            self.__list_box.insert(
                tk.END,
                company.get_founder_name() +
                ' ' +
                company.get_founder_surname())
            self.__list_box.insert(tk.END, company.get_company_name())
            self.__list_box.insert(tk.END, company.get_company_address())
            self.__list_box.insert(tk.END, company.get_tax_id())
            self.__list_box.insert(tk.END, company.get_foundation_year())
            self.__list_box.insert(
                tk.END, '____________________________________________')

        self.__scrollbar = tk.Scrollbar(
            self.__list_box_frame, orient="vertical")
        self.__scrollbar.config(command=self.__list_box.yview)
        self.__scrollbar.pack(side="right", fill="y")

        self.__list_box.config(yscrollcommand=self.__scrollbar.set)

        self.__total = tk.Label(
            self.__window_list_company,
            font=(
                'DejaVu Serif',
                '30'),
            bg='black',
            fg='white',
            text=str(counter))

        if counter >= 0 and counter < 10:
            self.__total.place(x=910, y=383)
        elif counter >= 10 and counter < 100:
            self.__total.place(x=900, y=383)
        elif counter >= 100 and counter < 1000:
            self.__total.place(x=890, y=383)
        elif counter >= 1000 and counter < 10000:
            self.__total.place(x=880, y=383)
        elif counter >= 10000:
            self.__total = tk.Label(
                self.__window_list_company,
                font=(
                    'DejaVu Serif',
                    '30'),
                bg='black',
                fg='white',
                text='10000+')
            self.__total.place(x=860, y=383)
        else:
            self.__total = tk.Label(
                self.__window_list_company,
                font=(
                    'DejaVu Serif',
                    '30'),
                bg='black',
                fg='white',
                text='#Error#')
            self.__total.place(x=840, y=383)

    def view_find_company(self):
        self.__window_find_company = self.__check_window_existence(
            self.__window_find_company)

        if self.__tip:
            self.__window_config(
                self.__window_find_company,
                "../Pictures/Background/company_find_background_tip.png",
                "../Pictures/Icons/company_find_image.png")
        else:
            self.__window_config(
                self.__window_find_company,
                "../Pictures/Background/company_find_background.png",
                "../Pictures/Icons/company_find_image.png")

        self.__list_box_frame = tk.Frame(self.__window_find_company)
        self.__list_box_frame.place(relx=0.3, rely=0.6, anchor='center')

        self.__list_box = tk.Listbox(
            self.__list_box_frame,
            width=30,
            height=16,
            bg='black',
            fg='white',
            font=(
                'DejaVu Serif',
                20,
                'bold'))
        self.__list_box.pack(side="left", fill="y")

        self.__scrollbar = tk.Scrollbar(
            self.__list_box_frame, orient="vertical")
        self.__scrollbar.config(command=self.__list_box.yview)
        self.__scrollbar.pack(side="right", fill="y")

        self.__list_box.config(yscrollcommand=self.__scrollbar.set)

        self.__tax_id = tk.Variable()

        self.__add_entry(self.__window_find_company, self.__tax_id, 358, 840)

        SubPage.__submit_button(
            self.__window_find_company,
            self.__submit_find_company)

    def view_add_employee(self):
        self.__window_add_employee = self.__check_window_existence(
            self.__window_add_employee)

        if self.__tip:
            self.__window_config(
                self.__window_add_employee,
                "../Pictures/Background/employee_add_background_tip.png",
                "../Pictures/Icons/employee_add_image.png")
        else:
            self.__window_config(
                self.__window_add_employee,
                "../Pictures/Background/employee_add_background.png",
                "../Pictures/Icons/employee_add_image.png")

        self.__name = tk.Variable()
        self.__surname = tk.Variable()
        self.__personal_id = tk.Variable()
        self.__address = tk.Variable()
        self.__birthday = tk.Variable()
        self.__company_tax_id = tk.Variable()
        self.__salary = tk.Variable()

        self.__add_entry(self.__window_add_employee, self.__name, 277)
        self.__add_entry(self.__window_add_employee, self.__surname, 366)
        self.__add_entry(self.__window_add_employee, self.__personal_id, 453)
        self.__add_entry(self.__window_add_employee, self.__address, 538)
        self.__add_entry(self.__window_add_employee, self.__birthday, 630)

        self.__add_entry(
            self.__window_add_employee,
            self.__company_tax_id,
            277,
            840)
        self.__add_entry(self.__window_add_employee, self.__salary, 366, 840)

        SubPage.__submit_button(
            self.__window_add_employee,
            lambda: CompanyManagement.add_employee(
                self.__emp_add_is_complete,
                self.__name.get(),
                self.__surname.get(),
                self.__personal_id.get(),
                self.__address.get(),
                self.__birthday.get(),
                self.__company_tax_id.get(),
                self.__salary.get()))

        self.__emp_add_is_complete.trace(
            'w', lambda var, indx, mode: self.complete(
                self.__window_add_employee, self.__emp_add_is_complete))

    def view_delete_employee(self):
        self.__window_delete_employee = self.__check_window_existence(
            self.__window_delete_employee)

        if self.__tip:
            self.__window_config(
                self.__window_delete_employee,
                "../Pictures/Background/employee_delete_background_tip.png",
                "../Pictures/Icons/employee_delete_image.png")
        else:
            self.__window_config(
                self.__window_delete_employee,
                "../Pictures/Background/employee_delete_background.png",
                "../Pictures/Icons/employee_delete_image.png")

        self.__company_tax_id = tk.Variable()
        self.__personal_id = tk.Variable()

        self.__add_entry(
            self.__window_delete_employee,
            self.__company_tax_id,
            322)
        self.__add_entry(
            self.__window_delete_employee,
            self.__personal_id,
            406)

        SubPage.__submit_button(
            self.__window_delete_employee,
            lambda: CompanyManagement.delete_employee(
                self.__emp_del_is_complete,
                self.__company_tax_id.get(),
                self.__personal_id.get()))

        self.__emp_del_is_complete.trace(
            'w', lambda var, indx, mode: self.complete(
                self.__window_delete_employee, self.__emp_del_is_complete))

    def view_list_employee(self):
        self.__window_list_employee = self.__check_window_existence(
            self.__window_list_employee)

        self.__window_config(
            self.__window_list_employee,
            "../Pictures/Background/employee_list_background.png",
            "../Pictures/Icons/employee_list_image.png")

        self.__list_box_frame = tk.Frame(self.__window_list_employee)
        self.__list_box_frame.place(relx=0.3, rely=0.6, anchor='center')

        self.__list_box = tk.Listbox(
            self.__list_box_frame,
            width=30,
            height=16,
            bg='black',
            fg='white',
            font=(
                'DejaVu Serif',
                20,
                'bold'))
        self.__list_box.pack(side="left", fill="y")

        counter = 0
        for employee in CompanyManagement.employees_list:
            counter += 1
            self.__list_box.insert(tk.END, str(counter) + ".EMPLOYEE")
            self.__list_box.insert(
                tk.END,
                employee.get_name() +
                ' ' +
                employee.get_surname())
            self.__list_box.insert(tk.END, employee.get_personal_id())
            self.__list_box.insert(tk.END, employee.get_address())
            self.__list_box.insert(tk.END, employee.get_birthday())
            self.__list_box.insert(tk.END, employee.get_company_tax_id())
            self.__list_box.insert(tk.END, employee.get_salary())
            self.__list_box.insert(
                tk.END, '____________________________________________')

        self.__scrollbar = tk.Scrollbar(
            self.__list_box_frame, orient="vertical")
        self.__scrollbar.config(command=self.__list_box.yview)
        self.__scrollbar.pack(side="right", fill="y")

        self.__list_box.config(yscrollcommand=self.__scrollbar.set)

        self.__total = tk.Label(
            self.__window_list_employee,
            font=(
                'DejaVu Serif',
                '30'),
            bg='black',
            fg='white',
            text=str(counter))

        if counter >= 0 and counter < 10:
            self.__total.place(x=910, y=383)
        elif counter >= 10 and counter < 100:
            self.__total.place(x=900, y=383)
        elif counter >= 100 and counter < 1000:
            self.__total.place(x=890, y=383)
        elif counter >= 1000 and counter < 10000:
            self.__total.place(x=880, y=383)
        elif counter >= 10000:
            self.__total = tk.Label(
                self.__window_list_employee,
                font=(
                    'DejaVu Serif',
                    '30'),
                bg='black',
                fg='white',
                text='10000+')
            self.__total.place(x=860, y=383)
        else:
            self.__total = tk.Label(
                self.__window_list_employee,
                font=(
                    'DejaVu Serif',
                    '30'),
                bg='black',
                fg='white',
                text='#Error#')
            self.__total.place(x=840, y=383)

    def view_find_employee(self):
        self.__window_find_employee = self.__check_window_existence(
            self.__window_find_employee)

        if self.__tip:
            self.__window_config(
                self.__window_find_employee,
                "../Pictures/Background/employee_find_background_tip.png",
                "../Pictures/Icons/employee_find_image.png")
        else:
            self.__window_config(
                self.__window_find_employee,
                "../Pictures/Background/employee_find_background.png",
                "../Pictures/Icons/employee_find_image.png")

        self.__list_box_frame = tk.Frame(self.__window_find_employee)
        self.__list_box_frame.place(relx=0.3, rely=0.6, anchor='center')

        self.__list_box = tk.Listbox(
            self.__list_box_frame,
            width=30,
            height=16,
            bg='black',
            fg='white',
            font=(
                'DejaVu Serif',
                20,
                'bold'))
        self.__list_box.pack(side="left", fill="y")

        self.__scrollbar = tk.Scrollbar(
            self.__list_box_frame, orient="vertical")
        self.__scrollbar.config(command=self.__list_box.yview)
        self.__scrollbar.pack(side="right", fill="y")

        self.__list_box.config(yscrollcommand=self.__scrollbar.set)

        self.__personal_id = tk.Variable()
        self.__company_tax_id = tk.Variable()

        self.__add_entry(self.__window_find_employee,
                         self.__personal_id, 310, 840)
        self.__add_entry(
            self.__window_find_employee,
            self.__company_tax_id,
            424,
            840)

        SubPage.__submit_button(
            self.__window_find_employee,
            self.submit_find_employee)

    def view_send_database(self):
        self.__window_send_database = self.__check_window_existence(
            self.__window_send_database)

        if self.__tip:
            self.__window_config(
                self.__window_send_database,
                "../Pictures/Background/database_send_background_tip.png",
                "../Pictures/Icons/send_image.png")
        else:
            self.__window_config(
                self.__window_send_database,
                "../Pictures/Background/database_send_background.png",
                "../Pictures/Icons/send_image.png")

        self.__host = tk.Variable()
        self.__user = tk.Variable()
        self.__database = tk.Variable()
        self.__password = tk.Variable()

        self.__add_entry(self.__window_send_database, self.__host, 313)
        self.__add_entry(self.__window_send_database, self.__user, 410)
        self.__add_entry(self.__window_send_database, self.__database, 506)
        self.__add_entry(self.__window_send_database, self.__password, 603)

        SubPage.__submit_button(
            self.__window_send_database,
            lambda: Server.submit_send_database(
                self.__server_send_is_complete,
                self.__host.get(),
                self.__user.get(),
                self.__database.get(),
                self.__password.get()))

        self.__server_send_is_complete.trace(
            'w', lambda var, indx, mode: self.complete(
                self.__window_send_database, self.__server_send_is_complete))

    def view_download_database(self):
        self.__window_download_database = self.__check_window_existence(
            self.__window_download_database)

        if self.__tip:
            self.__window_config(
                self.__window_download_database,
                "../Pictures/Background/database_download_background_tip.png",
                "../Pictures/Icons/download_image.png")
        else:
            self.__window_config(
                self.__window_download_database,
                "../Pictures/Background/database_download_background.png",
                "../Pictures/Icons/download_image.png")

        self.__host = tk.Variable()
        self.__user = tk.Variable()
        self.__database = tk.Variable()
        self.__password = tk.Variable()

        self.__add_entry(self.__window_download_database, self.__host, 313)
        self.__add_entry(self.__window_download_database, self.__user, 410)
        self.__add_entry(self.__window_download_database, self.__database, 506)
        self.__add_entry(self.__window_download_database, self.__password, 603)

        SubPage.__submit_button(
            self.__window_download_database,
            lambda: Server.submit_download_database(
                self.__server_download_is_complete,
                self.__host.get(),
                self.__user.get(),
                self.__database.get(),
                self.__password.get()))

        self.__server_download_is_complete.trace(
            'w', lambda var, indx, mode: self.complete(
                self.__window_download_database, self.__server_download_is_complete))

#----------------------------- View Methods END -----------------------------#

#--------------------------- Submit Methods START ---------------------------#

    def submit_find_employee(self):
        EMPTY = ''
        counter = 0

        if self.__personal_id.get() != EMPTY and self.__company_tax_id.get() != EMPTY:
            employee_exists, employee = CompanyManagement.check_employee_existence(
                self.__personal_id.get(), self.__company_tax_id.get())

            if employee_exists:

                self.__list_box_frame = tk.Frame(self.__window_find_employee)
                self.__list_box_frame.place(
                    relx=0.3, rely=0.6, anchor='center')

                self.__list_box = tk.Listbox(
                    self.__list_box_frame,
                    width=30,
                    height=16,
                    bg='black',
                    fg='white',
                    font=(
                        'DejaVu Serif',
                        20,
                        'bold'))
                self.__list_box.pack(side="left", fill="y")

                counter += 1
                self.__list_box.insert(tk.END, str(counter) + ".EMPLOYEE")
                self.__list_box.insert(
                    tk.END,
                    employee.get_name() +
                    ' ' +
                    employee.get_surname())
                self.__list_box.insert(tk.END, employee.get_personal_id())
                self.__list_box.insert(tk.END, employee.get_address())
                self.__list_box.insert(tk.END, employee.get_birthday())
                self.__list_box.insert(tk.END, employee.get_company_tax_id())
                self.__list_box.insert(tk.END, employee.get_salary())
                self.__list_box.insert(
                    tk.END, '____________________________________________')

                self.__scrollbar = tk.Scrollbar(
                    self.__list_box_frame, orient="vertical")
                self.__scrollbar.config(command=self.__list_box.yview)
                self.__scrollbar.pack(side="right", fill="y")

                self.__list_box.config(yscrollcommand=self.__scrollbar.set)

                self.__success_image = tk.PhotoImage(
                    file='../Pictures/Icons/success.png')
                self.__success = tk.Label(
                    self.__window_find_employee,
                    borderwidth=0,
                    highlightthickness=0,
                    image=self.__success_image)
                self.__success.place(x=1038, y=695)

                self.__window_find_employee.after(3000, self.__success.destroy)

            else:
                self.__failed_image = tk.PhotoImage(
                    file='../Pictures/Icons/failed.png')
                self.__failed = tk.Label(
                    self.__window_find_employee,
                    borderwidth=0,
                    highlightthickness=0,
                    image=self.__failed_image)
                self.__failed.place(x=1038, y=695)

                self.__window_find_employee.after(3000, self.__failed.destroy)

        elif self.__personal_id.get() != EMPTY and self.__company_tax_id.get() == EMPTY:
            employee_exists, employee = CompanyManagement.check_employee_existence(
                self.__personal_id.get())

            if employee_exists:

                self.__list_box_frame = tk.Frame(self.__window_find_employee)
                self.__list_box_frame.place(
                    relx=0.3, rely=0.6, anchor='center')

                self.__list_box = tk.Listbox(
                    self.__list_box_frame,
                    width=30,
                    height=16,
                    bg='black',
                    fg='white',
                    font=(
                        'DejaVu Serif',
                        20,
                        'bold'))
                self.__list_box.pack(side="left", fill="y")

                for employee in CompanyManagement.employees_list:
                    if employee.get_personal_id() == self.__personal_id.get():
                        counter += 1
                        self.__list_box.insert(
                            tk.END, str(counter) + ".EMPLOYEE")
                        self.__list_box.insert(
                            tk.END, employee.get_name() + ' ' + employee.get_surname())
                        self.__list_box.insert(
                            tk.END, employee.get_personal_id())
                        self.__list_box.insert(tk.END, employee.get_address())
                        self.__list_box.insert(tk.END, employee.get_birthday())
                        self.__list_box.insert(
                            tk.END, employee.get_company_tax_id())
                        self.__list_box.insert(tk.END, employee.get_salary())
                        self.__list_box.insert(
                            tk.END, '____________________________________________')

                self.__scrollbar = tk.Scrollbar(
                    self.__list_box_frame, orient="vertical")
                self.__scrollbar.config(command=self.__list_box.yview)
                self.__scrollbar.pack(side="right", fill="y")

                self.__list_box.config(yscrollcommand=self.__scrollbar.set)

                self.__success_image = tk.PhotoImage(
                    file='../Pictures/Icons/success.png')
                self.__success = tk.Label(
                    self.__window_find_employee,
                    borderwidth=0,
                    highlightthickness=0,
                    image=self.__success_image)
                self.__success.place(x=1038, y=695)

                self.__window_find_employee.after(3000, self.__success.destroy)

            else:
                self.__failed_image = tk.PhotoImage(
                    file='../Pictures/Icons/failed.png')
                self.__failed = tk.Label(
                    self.__window_find_employee,
                    borderwidth=0,
                    highlightthickness=0,
                    image=self.__failed_image)
                self.__failed.place(x=1038, y=695)

                self.__window_find_employee.after(3000, self.__failed.destroy)

        else:
            self.__failed_image = tk.PhotoImage(
                file='../Pictures/Icons/failed.png')
            self.__failed = tk.Label(
                self.__window_find_employee,
                borderwidth=0,
                highlightthickness=0,
                image=self.__failed_image)
            self.__failed.place(x=1038, y=695)

            self.__window_find_employee.after(3000, self.__failed.destroy)

    def __submit_find_company(self):
        EMPTY = ''

        if self.__tax_id.get() != EMPTY:
            company_exists, company = CompanyManagement.check_company_existence(
                self.__tax_id.get())

            if company_exists:

                self.__list_box_frame = tk.Frame(self.__window_find_company)
                self.__list_box_frame.place(
                    relx=0.3, rely=0.6, anchor='center')

                self.__list_box = tk.Listbox(
                    self.__list_box_frame,
                    width=30,
                    height=16,
                    bg='black',
                    fg='white',
                    font=(
                        'DejaVu Serif',
                        20,
                        'bold'))
                self.__list_box.pack(side="left", fill="y")

                self.__list_box.insert(tk.END, "1.COMPANY")
                self.__list_box.insert(
                    tk.END,
                    company.get_founder_name() +
                    ' ' +
                    company.get_founder_surname())
                self.__list_box.insert(tk.END, company.get_company_name())
                self.__list_box.insert(tk.END, company.get_company_address())
                self.__list_box.insert(tk.END, company.get_tax_id())
                self.__list_box.insert(tk.END, company.get_foundation_year())
                self.__list_box.insert(
                    tk.END, '____________________________________________')

                self.__scrollbar = tk.Scrollbar(
                    self.__list_box_frame, orient="vertical")
                self.__scrollbar.config(command=self.__list_box.yview)
                self.__scrollbar.pack(side="right", fill="y")

                self.__list_box.config(yscrollcommand=self.__scrollbar.set)

                self.__success_image = tk.PhotoImage(
                    file='../Pictures/Icons/success.png')
                self.__success = tk.Label(
                    self.__window_find_company,
                    borderwidth=0,
                    highlightthickness=0,
                    image=self.__success_image)
                self.__success.place(x=1038, y=695)

                self.__window_find_company.after(3000, self.__success.destroy)

            else:
                self.__failed_image = tk.PhotoImage(
                    file='../Pictures/Icons/failed.png')
                self.__failed = tk.Label(
                    self.__window_find_employee,
                    borderwidth=0,
                    highlightthickness=0,
                    image=self.__failed_image)
                self.__failed.place(x=1038, y=695)

                self.__window_find_employee.after(3000, self.__failed.destroy)

        else:
            self.__failed_image = tk.PhotoImage(
                file='../Pictures/Icons/failed.png')
            self.__failed = tk.Label(
                self.__window_find_employee,
                borderwidth=0,
                highlightthickness=0,
                image=self.__failed_image)
            self.__failed.place(x=1038, y=695)

            self.__window_find_employee.after(3000, self.__failed.destroy)

#---------------------------- Submit Methods END ----------------------------#

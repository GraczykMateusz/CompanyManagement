import tkinter as tk

from Page import Page
from SubPage import SubPage


class StartPage(tk.Tk, Page):
    '''Create main window with all settings'''
    tip = None

    def __init__(
        self, geometry="1200x800",
        background="../Pictures/Background/background.png",
        icon="../Pictures/Icons/icon.png"
    ):
        tk.Tk.__init__(self)

        self.sub_window = SubPage()

        # Image lists and image counters
        self.__emp_button_imgs = []
        self.__emp_buttons_counter = 0

        self.__comp_button_imgs = []
        self.__comp_buttons_counter = 0

        self.__db_button_imgs = []
        self.__db_buttons_counter = 0

        # Settings
        self._set_window(geometry)
        self._add_background(background)
        self._add_window_icon(icon)

        # Employee management buttons
        self.add_employee_button(
            "../Pictures/Buttons/employee_add_button.png",
            490, self.sub_window.view_add_employee
        )
        self.add_employee_button(
            "../Pictures/Buttons/employee_delete_button.png",
            550, self.sub_window.view_delete_employee
        )
        self.add_employee_button(
            "../Pictures/Buttons/employee_list_button.png",
            610, self.sub_window.view_list_employee
        )
        self.add_employee_button(
            "../Pictures/Buttons/employee_find_button.png",
            670, self.sub_window.view_find_employee
        )

        # Company management buttons
        self.add_company_button(
            "../Pictures/Buttons/company_add_button.png",
            490, self.sub_window.view_add_company
        )
        self.add_company_button(
            "../Pictures/Buttons/company_delete_button.png",
            550, self.sub_window.view_delete_company
        )
        self.add_company_button(
            "../Pictures/Buttons/company_list_button.png",
            610, self.sub_window.view_list_company
        )
        self.add_company_button(
            "../Pictures/Buttons/company_find_button.png",
            670, self.sub_window.view_find_company
        )

        # Database management buttons
        self.add_database_button(
            "../Pictures/Buttons/database_download_button.png",
            490, self.sub_window.view_download_database
        )
        self.add_database_button(
            "../Pictures/Buttons/database_send_button.png",
            550, self.sub_window.view_send_database
        )

        self.add_tip_button()

    def add_employee_button(self, button_img, position_y, event):
        position_x = 220

        self.__emp_button_imgs.append(tk.PhotoImage(file=button_img))
        self.__emp_button = tk.Button(
            self, command=lambda: event(),
            image=self.__emp_button_imgs[self.__emp_buttons_counter],
            bd=0, highlightbackground="black", activebackground="blue"
        )
        self.__emp_button.place(x=position_x, y=position_y)
        self.__emp_buttons_counter += 1

    def add_company_button(self, button_img, position_y, event):
        position_x = 520

        self.__comp_button_imgs.append(tk.PhotoImage(file=button_img))
        self.__comp_button = tk.Button(
            self, command=lambda: event(),
            image=self.__comp_button_imgs[self.__comp_buttons_counter],
            bd=0, highlightbackground="black", activebackground="blue"
        )
        self.__comp_button.place(x=position_x, y=position_y)
        self.__comp_buttons_counter += 1

    def add_database_button(self, button_img, position_y, event):
        position_x = 820

        self.__db_button_imgs.append(tk.PhotoImage(file=button_img))
        self.__db_button = tk.Button(
            self, command=lambda: event(),
            image=self.__db_button_imgs[self.__db_buttons_counter],
            bd=0, highlightbackground="black", activebackground="blue"
        )
        self.__db_button.place(x=position_x, y=position_y)
        self.__db_buttons_counter += 1

    def add_tip_button(self):
        StartPage.tip = tk.BooleanVar()
        StartPage.tip.set(True)
        self.sub_window.checks_tip(StartPage.tip.get())

        self.__tip_button_on = tk.Radiobutton(
            self,
            command=lambda: self.sub_window.checks_tip(StartPage.tip.get()),
            width="4", bd=0, text="ON ",
            bg="grey", variable=StartPage.tip, value=True
        )
        self.__tip_button_off = tk.Radiobutton(
            self,
            command=lambda: self.sub_window.checks_tip(StartPage.tip.get()),
            width="4", bd=0, text="OFF",
            bg='grey', variable=StartPage.tip, value=False
        )

        self.__tip_button_on.place(x=1105, y=710)
        self.__tip_button_off.place(x=1105, y=731)

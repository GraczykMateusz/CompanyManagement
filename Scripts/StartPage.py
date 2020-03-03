import tkinter as tk
from Page import Page

class StartPage(Page):
    
    def __init__(self, geometry="1200x800", background="../Pictures/Background/background.png", icon="../Pictures/Icons/icon.png"):
        self.root = tk.Tk()
        self._set_window(geometry)
        self._add_background(background)
        self._add_window_icon(icon)

        self.__employee_button_images_list = []
        self.__employee_buttons_counter=0

        self.__company_button_images_list = []
        self.__company_buttons_counter=0

        self.__database_button_images_list = []
        self.__database_buttons_counter=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

    def add_employee_button(self, button_image, position_y, event):
        position_x=220

        self.__employee_button_images_list.append(tk.PhotoImage(file = button_image))
        self.__employee_button=tk.Button(self.root, command = lambda: event(), bd=0, highlightbackground='black', image = self.__employee_button_images_list[self.__employee_buttons_counter])
        self.__employee_button.place(x = position_x, y = position_y)
        self.__employee_buttons_counter += 1

    def add_company_button(self, button_image, position_y, event):
        position_x=520

        self.__company_button_images_list.append(tk.PhotoImage(file = button_image))
        self.__company_button=tk.Button(self.root, command = lambda: event(), bd=0, highlightbackground='black', image = self.__company_button_images_list[self.__company_buttons_counter])
        self.__company_button.place(x = position_x, y = position_y)
        self.__company_buttons_counter += 1

    def add_database_button(self, button_image, position_y, event):
        position_x=820

        self.__database_button_images_list.append(tk.PhotoImage(file=button_image))
        self.__database_button=tk.Button(self.root, command = lambda: event(), bd=0, highlightbackground='black', image = self.__database_button_images_list[self.__database_buttons_counter])
        self.__database_button.place(x = position_x, y = position_y)
        self.__database_buttons_counter += 1



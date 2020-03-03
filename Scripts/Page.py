import tkinter as tk

class Page:

    def _set_window(self, geometry):
        self.root.geometry(geometry)
        self.root.resizable(width=False, height=False)
        self.root.title("CompanyManagment by Mateusz Graczyk")

    def _set_sub_window(self, geometry):
        self.top.geometry(geometry)
        self.top.resizable(width=False, height=False)
        self.top.title("CompanyManagment by Mateusz Graczyk")

    def _add_background(self, path_to_image):
        self.__background_image = tk.PhotoImage(file = path_to_image)
        self.__background = tk.Label(self.root, image = self.__background_image)
        self.__background.place(x=-1, y=-1)

    def _add_sub_background(self, path_to_image):
        self.__background_image = tk.PhotoImage(file = path_to_image)
        self.__background = tk.Label(self.top, image = self.__background_image)
        self.__background.place(x=-1, y=-1)

    def _add_window_icon(self, path_to_image):
        self.root.iconphoto(True, tk.PhotoImage(file = path_to_image))

    def mainloop(self):
        self.root.mainloop()
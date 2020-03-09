import tkinter as tk

class Page:

    def _set_window(self, geometry):
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        self.title("CompanyManagment by Mateusz Graczyk")

    def _add_background(self, path_to_image):
        self.__background_image = tk.PhotoImage(file = path_to_image)
        self.__background = tk.Label(self, image = self.__background_image)
        self.__background.place(x=-1, y=-1)

    def _add_window_icon(self, path_to_image):
        self.iconphoto(True, tk.PhotoImage(file = path_to_image))

    def mainloop(self):
        self.mainloop()
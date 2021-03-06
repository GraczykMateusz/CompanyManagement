import tkinter as tk


class Page:
    '''
    The StartPage and SubPage classes inherit from the Page class
    '''

    def _set_window(self, geometry):
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        self.title("CompanyManagement by Mateusz Graczyk")

    def _add_background(self, path_to_img):
        self.__background_img = tk.PhotoImage(file=path_to_img)
        self.__background = tk.Label(
            self, borderwidth=0, highlightthickness=0,
            image=self.__background_img
        )
        self.__background.place(x=0, y=0)

    def _add_window_icon(self, path_to_img):
        self.iconphoto(True, tk.PhotoImage(file=path_to_img))

    def _mainloop(self):
        self.mainloop()

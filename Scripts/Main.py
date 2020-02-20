from Displayer import Displayer

if __name__ == "__main__":
    window = Displayer()
    window.add_background("/home/wm/Programs/CompanyManagment/Pictures/Background/background.png")
    window.add_window_icon("/home/wm/Programs/CompanyManagment/Pictures/Icons/icon.png")

    window.add_employee_button("employee_add_button.png", 490)
    window.add_employee_button("employee_delete_button.png", 550)
    window.add_employee_button("employee_list_button.png", 610)
    window.add_employee_button("employee_find_button.png", 670)

    window.add_company_button("company_add_button.png", 490)
    window.add_company_button("company_delete_button.png", 550)
    window.add_company_button("company_list_button.png", 610)
    window.add_company_button("company_find_button.png", 670)

    window.add_database_button("database_download_button.png", 490)
    window.add_database_button("database_send_button.png", 550)

    window.mainloop()

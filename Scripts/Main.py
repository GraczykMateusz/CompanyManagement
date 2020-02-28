from Displayer import Displayer
from Manager import Manager

if __name__ == "__main__":
    window = Displayer()
    window.add_background("../Pictures/Background/background.png")
    window.add_window_icon("../Pictures/Icons/icon.png")

    window.add_employee_button("../Pictures/Buttons/employee_add_button.png", 490, Manager.add_employee)
    window.add_employee_button("../Pictures/Buttons/employee_delete_button.png", 550, Manager.delete_employee)
    window.add_employee_button("../Pictures/Buttons/employee_list_button.png", 610, Manager.list_employee)
    window.add_employee_button("../Pictures/Buttons/employee_find_button.png", 670, Manager.find_employee)

    window.add_company_button("../Pictures/Buttons/company_add_button.png", 490, Manager.add_company)
    window.add_company_button("../Pictures/Buttons/company_delete_button.png", 550, Manager.delete_company)
    window.add_company_button("../Pictures/Buttons/company_list_button.png", 610, Manager.list_company)
    window.add_company_button("../Pictures/Buttons/company_find_button.png", 670, Manager.find_company)

    window.add_database_button("../Pictures/Buttons/database_download_button.png", 490, Manager.download_database)
    window.add_database_button("../Pictures/Buttons/database_send_button.png", 550, Manager.send_database)

    window.mainloop()

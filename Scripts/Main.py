from StartPage import StartPage
from SubPage import SubPage

if __name__ == "__main__":
    
    window = StartPage()
    sub_window = SubPage()

    window.add_employee_button("../Pictures/Buttons/employee_add_button.png", 490, sub_window.add_employee)
    window.add_employee_button("../Pictures/Buttons/employee_delete_button.png", 550, sub_window.delete_employee)
    window.add_employee_button("../Pictures/Buttons/employee_list_button.png", 610, sub_window.list_employee)
    window.add_employee_button("../Pictures/Buttons/employee_find_button.png", 670, sub_window.find_employee)

    window.add_company_button("../Pictures/Buttons/company_add_button.png", 490, sub_window.add_company)
    window.add_company_button("../Pictures/Buttons/company_delete_button.png", 550, sub_window.delete_company)
    window.add_company_button("../Pictures/Buttons/company_list_button.png", 610, sub_window.list_company)
    window.add_company_button("../Pictures/Buttons/company_find_button.png", 670, sub_window.find_company)

    window.add_database_button("../Pictures/Buttons/database_download_button.png", 490, sub_window.download_database)
    window.add_database_button("../Pictures/Buttons/database_send_button.png", 550, sub_window.send_database)

    window.mainloop()

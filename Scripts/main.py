from CompanyManagement import CompanyManagement
from StartPage import StartPage

if __name__ == "__main__":
    CompanyManagement.import_data()

    window = StartPage()
    window.mainloop()
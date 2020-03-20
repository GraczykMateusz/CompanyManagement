from CompanyManagment import CompanyManagmet
from StartPage import StartPage

if __name__ == "__main__":
    
    CompanyManagmet.import_data()

    window = StartPage()
    window.mainloop()

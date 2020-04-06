from CompanyManagment import CompanyManagment
from StartPage import StartPage

if __name__ == "__main__":
    
    CompanyManagment.import_data()

    window = StartPage()
    window.mainloop()
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
class dd:
    def addemplyee(self):
            # Connect to the SQLite database
            connection = sqlite3.connect('library.db', check_same_thread=False)
            cursor = connection.cursor()

    def __init__(self, root):
          self.name = str()
          self.domen = str()
          self.monyfirst = int()
          self.deree = int()
          self.year = int()
          self.joinnum = int()
          self.certificate = str()
          self.cheldreen = int()
          self.job_adrees = str()
          self.marital_status = str()
          self.jobhusband = str()
          #معلومات المخصصات          

          #الشهادات للمخصصات
          self.certificate1 = 0.15
          self.certificate2 = 0.15
          self.certificate3 = 0.25
          self.certificate4 = 0.35
          self.certificate5 = 0.45
          self.certificate6 = 0.55
          self.certificate7 = 0.75
          self.certificate8 = 0.100
          # المواقع النائية
          self.remotelocation = 0.50
          # عائلية
          self.famliy = 50000
          #اطفال
          self.baby = 100000 # only 4
          #منصب الأداري
          self.positionadmin_divisionhead = 0.15
          self.positionadmin_domen = 0.20
          self.admin = 0.50
          #الاداري التدريسي
          self.admindomen = 1000000
          self.mqrrqsin = 150000
          self.adminqsim = 250000
          #هندسية
          self.engneernotwork = 0.35
          self.engneerwork = 0.50
          #لقب علمي
          self.techerhelp = 0.15
          self.techer = 0.25
          self.potecher_help = 0.35
          self.potecher = 0.50
          #مهنية قانونية
          self.qanony = 0.20
          #خطورة
          self.guard = 43750
          self.drivernorml = 785000
          self.drive_r_udasti = 131250
          #خدمة جامعية
          self.techring = 0.100
          self.techncal = 0.100
          self.admin_kh = 0.75
          #موقع جغرافي
          self.mapall = 20000
          #الأستقطاعات
          self.retirement = 0.10
          self.hshed = int()
          self.protection = 0.0025
          self.bank = int()
          self.pr_co = int()
          self.tax = int()
          self.club_student = int()
          self.fines = int()
          self.implement = int()


          root = root
          root.title("برنامج حساب الرواتب")

          screen_width = root.winfo_screenwidth()
          screen_height = root.winfo_screenheight()
          root.geometry(f'{screen_width}x{screen_height}+1+1')

          framebutton = Frame(root, highlightthickness=2, highlightbackground='black')
          framebutton.grid(row=0, column=0, padx=20, pady=20)

          but1test = tk.Button(framebutton, width=30, font=("Arial", 19, "bold"), text='test1', highlightthickness=2,height=20)
          but1test.grid(row=0,column=0)

          but2test = tk.Button(framebutton, width=30, font=("Arial", 19, "bold"), text='test1', highlightthickness=2,height=20)
          but2test.grid(row=1,column=0)

          but3test = tk.Button(framebutton, width=30, font=("Arial", 19, "bold"), text='test1', highlightthickness=2,height=20)
          but3test.grid(row=1,column=1)

          but4test = tk.Button(framebutton, width=30, font=("Arial", 19, "bold"), text='test1', highlightthickness=2)
          but4test.grid(row=0,column=1)

          root.grid_rowconfigure(0, weight=1)
          root.grid_rowconfigure(1, weight=1)
          root.grid_columnconfigure(0, weight=1)
          root.grid_columnconfigure(2, weight=1)

    
root = tk.Tk()
book = dd(root)
root.mainloop()

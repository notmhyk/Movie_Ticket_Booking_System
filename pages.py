import tkinter as tk
from tkinter import Tk, ttk
import db_handler
import models
from datetime import datetime, timedelta
from PIL import ImageTk, Image
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import filedialog
import string
import os
from datetime import date

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        self.show_canvas()
        self.show_widgets()

    def show_widgets(self):
        rows = 3
        roww = 13
        columns = 16
        for row in range(25):
            weight = 0 if row == 24 else 1
            self.grid_rowconfigure(row, weight=weight)
        for row in range(rows):  
            tk.Label(self, bg='white').grid(row=row+0, column=0)
        for row in range(rows): 
            tk.Label(self, bg='white').grid(row=row+5, column=0)
        for row in range(roww):
            tk.Label(self, bg='white').grid(row=row+11, column=0)
        for col in range(columns):
            tk.Label(self, bg='white').grid(row=2, column=col+2)

        tk.Label(self, text="No account yet? ", font=("Montserrat", 10), fg='#3A3B3C', bg='white').grid(row=20, column=0, columnspan=2)
        self.signup = tk.Label(self, text="Sign-up ", font=("Montserrat ", 10, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.signup.grid(row=20, column=1)
        self.login = tk.Label(self, text="LOGIN", font=("Montserrat ", 70, "bold"), fg='#3A3B3C', bg='white')
        self.user_ent = tk.Entry(self, width=40)
        self.user_ent.configure(bg='#F5F5F5')
        self.pass_ent = tk.Entry(self,show='*', width=40)
        self.pass_ent.configure(bg='#F5F5F5')
        self.btn = tk.Button(self, text="Login", font=('Montserrat', 10, 'bold'), fg='#3A3B3C', bg='#E5E4E2', command= self.on_click_login)

        tk.Label(self, text="Account name:", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=9, column=0,sticky='e',padx=(0, 10))
        tk.Label(self, text="Password:", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=10, column=0, sticky='e',padx=(0, 10))

        self.login.grid(row=5, column=0, columnspan=2, padx=(0, 10))
        self.btn.grid(row=11, column=1, columnspan=3, sticky='w', padx=10, pady=10, ipadx=20, ipady=5)
        self.user_ent.grid(row=9, column=1, sticky='w')
        self.pass_ent.grid(row=10, column=1, sticky='w')
        
        self.signup.bind('<Button-1>', self.on_click_signup)
        
    def show_canvas(self):
        current_date = date.today()
        tomorrow_date = current_date + timedelta(days=1)
        self.folder_path2 = tomorrow_date.strftime("%m_%d_%Y")
        self.folder_path = current_date.strftime("%m_%d_%Y")
        self.file_names2 = os.listdir(self.folder_path2)
        self.file_names = os.listdir(self.folder_path)
        self.images = []
        self.images2 = []
        for file_name2 in self.file_names2:
            image_path2 = os.path.join(self.folder_path2, file_name2)
            with open(image_path2, "rb") as file:
                file.read()
            image = Image.open(image_path2)
            image = image.resize((220, 270))
            photo = ImageTk.PhotoImage(image)
            self.images2.append(photo)

        for file_name in self.file_names:
            self.image_path = os.path.join(self.folder_path, file_name)
            with open(self.image_path, "rb") as file:
                        file.read()
            self.image = Image.open(self.image_path)
            self.image = self.image.resize((220, 270))
            self.photo = ImageTk.PhotoImage(self.image)
            self.images.append(self.photo)

        self.canvas_width = self.winfo_screenwidth() //1
        self.canvas_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='#FFA500')
        self.canvas.grid(row=0, column=19, rowspan=25, sticky='nsew')
        
        self.now_showing_label = tk.Label(self, text="NOW SHOWING", font=("Montserrat", 30, "bold"),
                                     fg='white', bg='#FFA500')
        self.canvas.create_window(self.canvas_width // 7, self.canvas_height // 23, window=self.now_showing_label)

        self.now_showing_moive1 = tk.Label(self, image=self.images[0])
        self.canvas.create_window(self.canvas_width // 9.2, self.canvas_height //3.7, window=self.now_showing_moive1)

        self.now_showing_moive2 = tk.Label(self, image=self.images[1])
        self.canvas.create_window(self.canvas_width // 3.3, self.canvas_height //3.7, window=self.now_showing_moive2)

        self.now_showing_moive3 = tk.Label(self, image=self.images[2])
        self.canvas.create_window(self.canvas_width // 2.01, self.canvas_height //3.7, window=self.now_showing_moive3)


        self.now_showing_label2 = tk.Label(self, text="UPCOMING", font=("Montserrat", 23, "bold"),
                                     fg='white', bg='#FFA500')
        self.canvas.create_window(self.canvas_width // 9, self.canvas_height // 2.049, window=self.now_showing_label2)

        self.now_showing_moive4 = tk.Label(self, image=self.images2[0])
        self.canvas.create_window(self.canvas_width // 9.2, self.canvas_height //1.42, window=self.now_showing_moive4)

        self.now_showing_moive5 = tk.Label(self, image=self.images2[1])
        self.canvas.create_window(self.canvas_width // 3.3, self.canvas_height //1.42, window=self.now_showing_moive5)

        self.now_showing_moive6 = tk.Label(self, image=self.images2[2])
        self.canvas.create_window(self.canvas_width // 2.01, self.canvas_height //1.42, window=self.now_showing_moive6)

    def on_click_signup(self, event):
        self.parent.change_window('Sign-upPage')

    def on_click_login(self):
        username = self.user_ent.get()
        password = self.pass_ent.get()
        if username == '':
            messagebox.showerror("Invalid Login", "Invalid username")
            return
        elif password == '':
            messagebox.showerror("Invalid Login", "Invalid password")
            return

        if self.parent.db_handler.admin_login(username, password):
            self.user_ent.delete(0, tk.END)
            self.pass_ent.delete(0, tk.END)
            self.parent.change_window('ViewDatabase')
        elif self.parent.db_handler.emp_login(username, password):
            self.user_ent.delete(0, tk.END)
            self.pass_ent.delete(0, tk.END)
            self.parent.change_window('MovieSelection')
        else:
            messagebox.showerror("Invalid Login", "Invalid username or password")

class SignUpPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white') 
        self.show_canvas()
        self.show_widgets()
    def show_widgets(self):
        tk.Label(self, bg='white').grid(row=1, column=0)
        tk.Label(self, text='Sign-Up', font=("Montserrat", 70, "bold"), fg='#3A3B3C', bg='white').grid(row=0, column=1, sticky='w')
        tk.Label(self, text='Employee Information: ', font=("Montserrat", 25, "bold"), width=25, fg='#3A3B3C', bg='white').grid(row=2, column=1, sticky='w')
        tk.Label(self, text='Name:', font=("Montserrat", 20, "bold"),  fg='#3A3B3C', bg='white', width=33).grid(row=3, column=1, sticky='w')
        tk.Label(self, text='Birthdate: ', font=("Montserrat", 20, "bold"),  fg='#3A3B3C', bg='white', width=30).grid(row=4, column=1, sticky='w')
        tk.Label(self, text='Contact no: ', font=("Montserrat", 20, "bold"),  fg='#3A3B3C', bg='white', width=29).grid(row=5, column=1, sticky='w')
        tk.Label(self, text='Email Address: ', font=("Montserrat", 20, "bold"),  fg='#3A3B3C', bg='white', width=27).grid(row=6, column=1, sticky='w')
        tk.Label(self, text='Employee no: ', font=("Montserrat", 20, "bold"), fg='#3A3B3C', bg='white', width=28).grid(row=7, column=1, sticky='w')

        tk.Label(self, text='Account Information: ', font=("Montserrat", 25, "bold"), width=23, fg='#3A3B3C', bg='white').grid(row=8, column=1, sticky='w')
        tk.Label(self, text='Account Name:', font=("Montserrat", 20, "bold"),  fg='#3A3B3C', bg='white', width=26).grid(row=9, column=1, sticky='w')
        tk.Label(self, text='Password:', font=("Montserrat", 20, "bold"),  fg='#3A3B3C', bg='white', width=30).grid(row=10, column=1, sticky='w')
        tk.Label(self, text='Confirm Password:', font=("Montserrat", 20, "bold"),  fg='#3A3B3C', bg='white', width=23).grid(row=11, column=1, sticky='w')
        
        self.emp_name = tk.Entry(self, width=40)
        self.emp_name.configure(bg='#F5F5F5')
        self.emp_birth = tk.Entry(self, width=40)
        self.emp_birth.configure(bg='#F5F5F5')
        self.emp_contact= tk.Entry(self, width=40)
        self.emp_contact.configure(bg='#F5F5F5')
        self.emp_email = tk.Entry(self, width=40)
        self.emp_email.configure(bg='#F5F5F5')
        self.emp_number = tk.Entry(self, width=40)
        self.emp_number.configure(bg='#F5F5F5')

        self.emp_accname = tk.Entry(self, width=40)
        self.emp_accname.configure(bg='#F5F5F5')
        self.emp_pass = tk.Entry(self, width=40, show='*')
        self.emp_pass.configure(bg='#F5F5F5')
        self.emp_conpass = tk.Entry(self, width=40, show='*')
        self.emp_conpass.configure(bg='#F5F5F5')

        self.save_btn = tk.Button(self, text="Sign-Up",font=('Montserrat', 10, 'bold'), fg='#3A3B3C', bg='#E5E4E2', command=self.on_click_sign_up)
        self.save_btn.grid(row=12, column=1, columnspan=2, ipadx=30, ipady=5)

        self.back_btn = tk.Button(self, text="Back",font=('Montserrat', 10, 'bold'), fg='#3A3B3C', bg='#E5E4E2', command=self.on_return_login)
        self.back_btn.grid(row=12, column=2, columnspan=2, ipadx=30, ipady=5)

        self.emp_name.grid(row= 3, column=1, sticky='e')
        self.emp_birth.grid(row= 4, column=1, sticky='e')
        self.emp_contact.grid(row= 5, column=1, sticky='e')
        self.emp_email.grid(row= 6, column=1, sticky='e')
        self.emp_number.grid(row= 7, column=1, sticky='e')

        self.emp_accname.grid(row= 9, column=1, sticky='e')
        self.emp_pass.grid(row= 10, column=1, sticky='e')
        self.emp_conpass.grid(row= 11, column=1, sticky='e')

    def show_canvas(self):
        for row in range(40):
            weight = 0 if row == 40 else 1
            self.grid_rowconfigure(row, weight=weight)

        self.canvas_width = self.winfo_screenwidth() //1
        self.canvas_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='#FFA500')
        self.canvas.grid(row=0, column=35, rowspan=35, sticky='nsew')

    def on_click_sign_up(self):
        name = self.emp_name.get()
        birthdate = self.emp_birth.get()
        contact = self.emp_contact.get()
        email = self.emp_email.get()
        emp_num = self.emp_number.get()
        username = self.emp_accname.get()
        password = self.emp_pass.get()
        confirm_password = self.emp_conpass.get()
        if name == '':
            messagebox.showerror('Error', 'Name is empty!') 
            return 
        elif not name.isalpha():
            messagebox.showerror('Error', 'Name should only contain alphabetic characters!')
            return 
        elif birthdate == '':
            messagebox.showerror('Error', 'Birthday is empty!') 
            return 
        elif contact == '':
            messagebox.showerror('Error', 'Contact number is empty!')
            return 
        elif not contact.isdigit():
            messagebox.showerror('Error', 'Contact number should only contain digits!')
            return 
        elif email == '':
            messagebox.showerror('Error', 'Email is empty!')    
            return        
        elif emp_num == '':
            messagebox.showerror('Error', 'Employee number is empty') 
            return           
        elif not emp_num.isdigit():
            messagebox.showerror('Error', 'Employee number should only contain digits!')
            return 
        elif username == '':
            messagebox.showerror('Error', 'Username is empty!')
            return 
        elif password == '':
            messagebox.showerror('Error', 'Password is empty!')
            return 
        elif confirm_password == '':
            messagebox.showerror('Error', 'Confirm password is empty!')
            return 
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        else:
            employee = models.Account_emp()
            employee.name = name
            employee.birthdate = birthdate
            employee.contact = contact
            employee.email = email
            employee.emp_num = emp_num
            employee.user = username
            employee.password = password
            db_conn = db_handler.DBHandler()
            db_conn.insert_employee(employee)
            db_conn.close()


            messagebox.showinfo("Success", "Employee account created successfully!")
            self.emp_name.delete(0, tk.END)
            self.emp_birth.delete(0, tk.END)
            self.emp_contact.delete(0, tk.END)
            self.emp_email.delete(0, tk.END)
            self.emp_number.delete(0, tk.END)
            self.emp_accname.delete(0, tk.END)
            self.emp_pass.delete(0, tk.END)
            self.emp_conpass.delete(0, tk.END)
            self.parent.change_window('LoginPage')
    def on_return_login(self):
        confirmed = messagebox.askyesno('Confirmation', 'Are you sure you want to cancel?')
        if confirmed: 
            self.emp_name.delete(0, tk.END)
            self.emp_birth.delete(0, tk.END)
            self.emp_contact.delete(0, tk.END)
            self.emp_email.delete(0, tk.END)
            self.emp_number.delete(0, tk.END)
            self.emp_accname.delete(0, tk.END)
            self.emp_pass.delete(0, tk.END)
            self.emp_conpass.delete(0, tk.END)
            self.parent.change_window('LoginPage')
        else:
            return

class MovieSelection(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        self.original_movie_names = []
        self.selected_date = datetime.now().strftime("%m_%d_%Y")
        self.original_movie_amounts = []
        self.show_widgets()
    def show_widgets(self):
        
        rows = 3
        movie_row = 1
        for row in range(rows):  
            tk.Label(self, bg='white').grid(row=row+1, column=0)
        for row in range(movie_row):  
            tk.Label(self, bg='white').grid(row=row+5, column=0)

        self.combo_box = ttk.Combobox(self, state="readonly")
        # self.combo_box.bind("<<ComboboxSelected>>", self.populate_dates)
        self.combo_box.bind("<<ComboboxSelected>>", self.update_folder_path)
        self.combo_box.grid(row=4, column=0)
        
        self.movie_selection = tk.Label(self, text="Movie Selection", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=27, height=2, cursor='hand2')
        self.movie_selection.grid(row=0, column=0)
        self.seat_selection = tk.Label(self, text="Seat Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.seat_selection.grid(row=0, column=1)
        self.confirmation = tk.Label(self, text="Confirmation", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.confirmation.grid(row=0, column=2)

        self.date_lb = tk.Label(self, text="Date: ", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white')
        self.date_lb.grid(row=4, column=0,padx=78, sticky='w')

        self.logout = tk.Button(self, text="Logout", font=("Montserrat", 15, "bold"), fg='white', bg="#3A3B3C", command=self.on_click_logout)
        self.logout.grid(row=4, column=2, ipadx=30, pady=20)

        self.movie1 = tk.Label(self)
        self.movie1.grid(row=7, column=0, ipady=10)
        self.movie2 = tk.Label(self)
        self.movie2.grid(row=7, column=1, ipady=10)
        self.movie3 = tk.Label(self)
        self.movie3.grid(row=7, column=2, ipady=10)

        self.seat_selection.bind('<Enter>', self.on_enter_seats)
        self.seat_selection.bind('<Leave>', self.on_leave_seats)
        self.seat_selection.bind('<Button-1>', self.on_click_seats)

        self.confirmation.bind('<Enter>', self.on_enter_confirmation)
        self.confirmation.bind('<Leave>', self.on_leave_confirmation)
        self.confirmation.bind('<Button-1>', self.on_click_confirmation)
        self.populate_dates()
        self.set_initial_value()
        self.get_movies()
    def get_movies(self):
        key = self.combo_box.get()
        db_conn = db_handler.DBHandler()
        rows = db_conn.search_movie_selection(key)
        db_conn.close()
        
        self.original_movie_names.clear()
        self.original_movie_amounts.clear()

        self.movie_labels = [] 

        for i, movie in enumerate(rows):
            movie_name = movie.name
            movie_amount = movie.amount 

            label = None
            if i == 0:
                label = self.movie1
                label.bind("<Button-1>", lambda event, name=movie_name, amount=movie_amount, dates=self.selected_date: self.label_clicked(name, amount, dates))
            elif i == 1:
                label = self.movie2
                label.bind("<Button-1>", lambda event, name=movie_name, amount=movie_amount, dates=self.selected_date: self.label_clicked2(name, amount, dates))
            elif i == 2:
                label = self.movie3
                label.bind("<Button-1>", lambda event, name=movie_name, amount=movie_amount, dates=self.selected_date: self.label_clicked3(name, amount, dates))
            if label is not None:
                label.config(text=movie_name)

                image_path = os.path.join(self.folder_path, f"{movie_name}.jpg")  
                try:
                    image = Image.open(image_path)
                    image = image.resize((300, 400))
                    photo = ImageTk.PhotoImage(image)
                    
                    label.config(image=photo)
                    label.image = photo
                    
                    self.original_movie_names.append(movie_name)
                    self.original_movie_amounts.append(movie_amount)
                except FileNotFoundError:
                    messagebox.showinfo("Error",f"Image file not found: {image_path}" )

    def label_clicked(self, movie_name, movie_amount, dates, ):
        self.parent.change_window("SeatSelection1", movie_name, movie_amount, dates)
    def label_clicked2(self, movie_name, movie_amount, dates, ):
        self.parent.change_window("SeatSelection2", movie_name, movie_amount, dates)
    def label_clicked3(self, movie_name, movie_amount, dates, ):
        self.parent.change_window("SeatSelection3", movie_name, movie_amount, dates)
    
        
    def populate_dates(self, event=None):
        self.combo_box['values'] = []

        current_date = datetime.now()
        start_date = current_date
        end_date = start_date + timedelta(days=6)

        dates = []
        while start_date <= end_date:
            date_string = start_date.strftime("%m/%d/%Y")
            dates.append(date_string)
            start_date += timedelta(days=1)

        self.combo_box['values'] = dates
        current_date_index = self.combo_box.current()

        if current_date_index > 0:
            self.combo_box.bind("<<ComboboxSelected>>", self.update_folder_path)
            for i, label in enumerate([self.movie1, self.movie2, self.movie3]):
                label.config(text=self.original_movie_names[i])
                label.bind("<Button-1>", lambda event, name=self.original_movie_names[i], amount=self.original_movie_amounts[i]: self.label_clicked(name, amount))
        selected_date = dates[0]
        self.selected_date = datetime.now().strptime(selected_date, "%m/%d/%Y").strftime("%m_%d_%Y")
        self.folder_path = self.selected_date
        self.get_movies()
    def update_folder_path(self, event):
        # current_date_index = self.combo_box.current()
        selected_date = self.combo_box.get()
        self.selected_date = datetime.strptime(selected_date, "%m/%d/%Y").strftime("%m_%d_%Y")
        self.folder_path = self.selected_date
        self.get_movies()

    def set_initial_value(self):
        current_date = datetime.now().strftime("%m/%d/%Y")
        self.combo_box.set(current_date)
        self.get_movies()

    def on_enter_seats(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_seats(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_enter_confirmation(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_leave_confirmation(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_click_seats(self, event):
        messagebox.showerror("Error", "Please choose a movie")
        return
    def on_click_confirmation(self, event):
        messagebox.showerror("Error", "Please choose a movie")
        return
    def on_click_logout(self):
        self.parent.change_window('LoginPage')

class SeatSelection1(tk.Frame):
    selected_seats1 = set()
    final_selected_seats = set()
    def __init__(self, master, movie_name, movie_amount, dates):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.movie_name = movie_name
        self.movie_amount = movie_amount
        self.movie_dates = dates

        self.configure(bg='white')
        self.show_widgets()
    def show_widgets(self):
        self.movie_selection = tk.Label(self, text="Movie Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.movie_selection.grid(row=0, column=0)
        self.seat_selection = tk.Label(self, text="Seat Selection", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=27, height=2, cursor='hand2')
        self.seat_selection.grid(row=0, column=1)
        self.confirmation = tk.Label(self, text="Confirmation", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.confirmation.grid(row=0, column=2)

        tk.Label(self, text="Available", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=1, column=0, pady=20)
        tk.Label(self, text="Pre-occupied", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=2, column=0)
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2).grid(row=1, column=0, padx=85, pady=20, sticky='e')
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='#800000',width=2).grid(row=2, column=0, padx=85, sticky='e')
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='white', bg='white').grid(row=3, column=0)

        self.checkDB_btn = tk.Button(self, text="Next", font=("Montserrat", 15, "bold"), fg='white', bg="#00FF00", command=self.on_click_save)
        self.checkDB_btn.grid(row=3, column=2, ipadx=40)

        self.logout = tk.Button(self, text="Logout", font=("Montserrat", 15, "bold"), fg='white', bg="#3A3B3C", command=self.on_click_logout)
        self.logout.grid(row=1, column=2, ipadx=30)

        self.movie_selection.bind('<Enter>', self.on_enter_movie)
        self.movie_selection.bind('<Leave>', self.on_leave_movie)
        self.movie_selection.bind('<Button-1>', self.on_click_movie)

        self.confirmation.bind('<Enter>', self.on_enter_confirmation)
        self.confirmation.bind('<Leave>', self.on_leave_confirmation)
        self.confirmation.bind('<Button-1>', self.on_click_confirmation)
        
        tk.Label(self,bg="white").grid(row=3, column=0)
        
        self.click_seat = 0

        self.seat_left = [
            ['A11', 'A12', 'A13', 'A14', 'A15'],
            ['B11', 'B12', 'B13', 'B14', 'B15'],
            ['C11', 'C12', 'C13', 'C14', 'C15'],
            ['D11', 'D12', 'D13', 'D14', 'D15'],
            ['E11', 'E12', 'E13', 'E14', 'E15'],
        ]
        for rows, seat in enumerate(self.seat_left):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+4, column=0, padx=(50*row, 70*(4-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))

                # if seats in SeatSelection1.selected_seats1:
                if seats in self.selected_seats1 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')

        self.seat_center = [
            ['A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27'],
            ['B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27'],
            ['C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27'],
            ['D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27'],
            ['E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27'],
            ['F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27'],
        ]

        for rows, seat in enumerate(self.seat_center):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+3, column=1, padx=(50*row, 50*(7-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))

                # if seats in SeatSelection1.selected_seats1:
                if seats in self.selected_seats1 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')
        
        self.seat_right = [
            ['A31', 'A32', 'A33', 'A34', 'A35'],
            ['B31', 'B32', 'B33', 'B34', 'B35'],
            ['C31', 'C32', 'C33', 'C34', 'C35'],
            ['D31', 'D32', 'D33', 'D34', 'D35'],
            ['E31', 'E32', 'E33', 'E34', 'E35'],
        ]
        for rows, seat in enumerate(self.seat_right):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+4, column=2, padx=(50*row, 70*(4-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))

                # if seats in SeatSelection1.selected_seats1:
                if seats in self.selected_seats1 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')

    def on_seat_click(self, label):
        seat = label.cget("text")
        if label.cget("bg") == "#800000":
            label.config(bg="#C0C0C0", fg='#3A3B3C')
            self.click_seat -= 1
            SeatSelection1.selected_seats1.remove(seat)
        else:
            label.config(bg="#800000", fg='white')
            self.click_seat += 1
            SeatSelection1.selected_seats1.add(seat)

    def on_enter_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_movie(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_enter_confirmation(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_leave_confirmation(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))

    def on_click_movie(self, event):
        yes_no = messagebox.askokcancel("Info", "Are you sure you want to cancel this movie?")
        if yes_no:
            self.parent.change_window('MovieSelection')
        else:
            return

    def on_click_confirmation(self, event):
        seats = self.selected_seats1.copy()
        num_seats = len(seats)
        amount = self.movie_amount
        total = num_seats * amount
        name = self.movie_name
        dates = self.movie_dates
        
        self.parent.change_window('Confirmation1', name, amount, dates, total, seats, num_seats)
        self.final_selected_seats.update(seats)
        self.selected_seats1.clear()
    def on_click_save(self):
        seats = self.selected_seats1.copy()
        num_seats = len(seats)
        amount = self.movie_amount
        total = num_seats * amount
        name = self.movie_name
        dates = self.movie_dates
        
        self.parent.change_window('Confirmation1', name, amount, dates, total, seats, num_seats)
        self.final_selected_seats.update(seats)
        self.selected_seats1.clear()
    def on_click_logout(self):
        self.parent.change_window('LoginPage')

class SeatSelection2(tk.Frame):
    selected_seats2 = set()
    final_selected_seats = set()
    def __init__(self, master, movie_name, movie_amount, dates):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.movie_name = movie_name
        self.movie_amount = movie_amount
        self.movie_dates = dates
        
        self.configure(bg='white')
        self.show_widgets()
    def show_widgets(self):
        self.movie_selection = tk.Label(self, text="Movie Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.movie_selection.grid(row=0, column=0)
        self.seat_selection = tk.Label(self, text="Seat Selection", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=27, height=2, cursor='hand2')
        self.seat_selection.grid(row=0, column=1)
        self.confirmation = tk.Label(self, text="Confirmation", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.confirmation.grid(row=0, column=2)

        tk.Label(self, text="Available", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=1, column=0, pady=20)
        tk.Label(self, text="Pre-occupied", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=2, column=0)
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2).grid(row=1, column=0, padx=85, pady=20, sticky='e')
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='#800000',width=2).grid(row=2, column=0, padx=85, sticky='e')
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='white', bg='white').grid(row=3, column=0)

        self.checkDB_btn = tk.Button(self, text="Next", font=("Montserrat", 15, "bold"), fg='white', bg="#00FF00", command=self.on_click_save)
        self.checkDB_btn.grid(row=3, column=2, ipadx=40)

        self.logout = tk.Button(self, text="Logout", font=("Montserrat", 15, "bold"), fg='white', bg="#3A3B3C", command=self.on_click_logout)
        self.logout.grid(row=1, column=2, ipadx=30)

        self.movie_selection.bind('<Enter>', self.on_enter_movie)
        self.movie_selection.bind('<Leave>', self.on_leave_movie)
        self.movie_selection.bind('<Button-1>', self.on_click_movie)

        self.confirmation.bind('<Enter>', self.on_enter_confirmation)
        self.confirmation.bind('<Leave>', self.on_leave_confirmation)
        self.confirmation.bind('<Button-1>', self.on_click_confirmation)
        
        tk.Label(self,bg="white").grid(row=3, column=0)
        
        self.click_seat = 0

        self.seat_left = [
            ['A11', 'A12', 'A13', 'A14', 'A15'],
            ['B11', 'B12', 'B13', 'B14', 'B15'],
            ['C11', 'C12', 'C13', 'C14', 'C15'],
            ['D11', 'D12', 'D13', 'D14', 'D15'],
            ['E11', 'E12', 'E13', 'E14', 'E15'],
        ]
        for rows, seat in enumerate(self.seat_left):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+4, column=0, padx=(50*row, 70*(4-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))
                # if seats in SeatSelection2.selected_seats2:
                if seats in self.selected_seats2 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')
        self.seat_center = [
            ['A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27'],
            ['B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27'],
            ['C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27'],
            ['D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27'],
            ['E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27'],
            ['F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27'],
        ]

        for rows, seat in enumerate(self.seat_center):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+3, column=1, padx=(50*row, 50*(7-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))
                # if seats in SeatSelection2.selected_seats2:
                if seats in self.selected_seats2 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')
        self.seat_right = [
            ['A31', 'A32', 'A33', 'A34', 'A35'],
            ['B31', 'B32', 'B33', 'B34', 'B35'],
            ['C31', 'C32', 'C33', 'C34', 'C35'],
            ['D31', 'D32', 'D33', 'D34', 'D35'],
            ['E31', 'E32', 'E33', 'E34', 'E35'],
        ]
        for rows, seat in enumerate(self.seat_right):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+4, column=2, padx=(50*row, 70*(4-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))
                # if seats in SeatSelection2.selected_seats2:
                if seats in self.selected_seats2 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')
    def on_seat_click(self, label):
        seat = label.cget("text")
        if label.cget("bg") == "#800000":
            label.config(bg="#C0C0C0", fg='#3A3B3C')
            self.click_seat -= 1
            SeatSelection2.selected_seats2.remove(seat)
        else:
            label.config(bg="#800000", fg='white')
            self.click_seat += 1
            SeatSelection2.selected_seats2.add(seat)

    def on_enter_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_movie(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_enter_confirmation(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_leave_confirmation(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_click_movie(self, event):
        yes_no = messagebox.askokcancel("Info", "Are you sure you want to cancel this movie?")
        if yes_no:
            self.parent.change_window('MovieSelection')
        else:
            return
    def on_click_confirmation(self, event):
        seats = self.selected_seats2.copy()
        num_seats = len(seats)
        amount = self.movie_amount
        total = num_seats * amount
        name = self.movie_name
        dates = self.movie_dates
        
        self.parent.change_window('Confirmation2', name, amount, dates, total, seats, num_seats)
        self.final_selected_seats.update(seats)
        self.selected_seats2.clear()
    def on_click_save(self):
        seats = self.selected_seats2.copy()
        num_seats = len(seats)
        amount = self.movie_amount
        total = num_seats * amount
        name = self.movie_name
        dates = self.movie_dates
        
        self.parent.change_window('Confirmation2', name, amount, dates, total, seats, num_seats)
        self.final_selected_seats.update(seats)
        self.selected_seats2.clear()
    def on_click_logout(self):
        self.parent.change_window('LoginPage')

class SeatSelection3(tk.Frame):
    selected_seats3 = set()
    final_selected_seats = set()
    def __init__(self, master, movie_name, movie_amount, dates):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.movie_name = movie_name
        self.movie_amount = movie_amount
        self.movie_dates = dates
        self.configure(bg='white')
        self.show_widgets()
    def show_widgets(self):
        self.movie_selection = tk.Label(self, text="Movie Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.movie_selection.grid(row=0, column=0)
        self.seat_selection = tk.Label(self, text="Seat Selection", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=27, height=2, cursor='hand2')
        self.seat_selection.grid(row=0, column=1)
        self.confirmation = tk.Label(self, text="Confirmation", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.confirmation.grid(row=0, column=2)

        tk.Label(self, text="Available", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=1, column=0, pady=20)
        tk.Label(self, text="Pre-occupied", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white').grid(row=2, column=0)
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2).grid(row=1, column=0, padx=85, pady=20, sticky='e')
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='#800000',width=2).grid(row=2, column=0, padx=85, sticky='e')
        tk.Label(self, text="    ", font=("Montserrat", 19, "bold"), fg='white', bg='white').grid(row=3, column=0)

        self.checkDB_btn = tk.Button(self, text="Next", font=("Montserrat", 15, "bold"), fg='white', bg="#00FF00", command=self.on_click_save)
        self.checkDB_btn.grid(row=3, column=2, ipadx=40)

        self.logout = tk.Button(self, text="Logout", font=("Montserrat", 15, "bold"), fg='white', bg="#3A3B3C", command=self.on_click_logout)
        self.logout.grid(row=1, column=2, ipadx=30)

        self.movie_selection.bind('<Enter>', self.on_enter_movie)
        self.movie_selection.bind('<Leave>', self.on_leave_movie)
        self.movie_selection.bind('<Button-1>', self.on_click_movie)

        self.confirmation.bind('<Enter>', self.on_enter_confirmation)
        self.confirmation.bind('<Leave>', self.on_leave_confirmation)
        self.confirmation.bind('<Button-1>', self.on_click_confirmation)
        
        tk.Label(self,bg="white").grid(row=3, column=0)
        
        self.click_seat = 0

        self.seat_left = [
            ['A11', 'A12', 'A13', 'A14', 'A15'],
            ['B11', 'B12', 'B13', 'B14', 'B15'],
            ['C11', 'C12', 'C13', 'C14', 'C15'],
            ['D11', 'D12', 'D13', 'D14', 'D15'],
            ['E11', 'E12', 'E13', 'E14', 'E15'],
        ]
        for rows, seat in enumerate(self.seat_left):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+4, column=0, padx=(50*row, 70*(4-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))
                # if seats in SeatSelection3.selected_seats3:
                if seats in self.selected_seats3 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')
        self.seat_center = [
            ['A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27'],
            ['B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27'],
            ['C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27'],
            ['D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27'],
            ['E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27'],
            ['F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27'],
        ]

        for rows, seat in enumerate(self.seat_center):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+3, column=1, padx=(50*row, 50*(7-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))
                # if seats in SeatSelection3.selected_seats3:
                if seats in self.selected_seats3 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')
        self.seat_right = [
            ['A31', 'A32', 'A33', 'A34', 'A35'],
            ['B31', 'B32', 'B33', 'B34', 'B35'],
            ['C31', 'C32', 'C33', 'C34', 'C35'],
            ['D31', 'D32', 'D33', 'D34', 'D35'],
            ['E31', 'E32', 'E33', 'E34', 'E35'],
        ]
        for rows, seat in enumerate(self.seat_right):
            for row, seats in enumerate(seat):
                self.seat_label = tk.Label(self, text=seats, font=("Montserrat", 15, "bold"), fg='#3A3B3C', bg='#C0C0C0', width=2, height=1, anchor='center')
                self.seat_label.grid(row=rows+4, column=2, padx=(50*row, 70*(4-row)), pady=20)
                self.seat_label.bind("<Button-1>", lambda event, label=self.seat_label: self.on_seat_click(label))
                # if seats in SeatSelection3.selected_seats3:
                if seats in self.selected_seats3 or seats in self.final_selected_seats:
                    self.seat_label.config(bg="#800000", fg='white')
                else:
                    self.seat_label.config(bg="#C0C0C0", fg='#3A3B3C')
    def on_seat_click(self, label):
        seat = label.cget("text")
        if label.cget("bg") == "#800000":
            label.config(bg="#C0C0C0", fg='#3A3B3C')
            self.click_seat -= 1
            SeatSelection3.selected_seats3.remove(seat)
        else:
            label.config(bg="#800000", fg='white')
            self.click_seat += 1
            SeatSelection3.selected_seats3.add(seat)

    def on_enter_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_movie(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_enter_confirmation(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_leave_confirmation(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_click_movie(self, event):
        yes_no = messagebox.askokcancel("Info", "Are you sure you want to cancel this movie?")
        if yes_no:
            self.parent.change_window('MovieSelection')
        else:
            return
    def on_click_confirmation(self, event):
        seats = self.selected_seats3.copy()
        num_seats = len(seats)
        amount = self.movie_amount
        total = num_seats * amount
        name = self.movie_name
        dates = self.movie_dates
        
        self.parent.change_window('Confirmation3', name, amount, dates, total, seats, num_seats)
        self.final_selected_seats.update(seats)
        self.selected_seats3.clear()
    def on_click_save(self):
        seats = self.selected_seats3.copy()
        num_seats = len(seats)
        amount = self.movie_amount
        total = num_seats * amount
        name = self.movie_name
        dates = self.movie_dates
        
        self.parent.change_window('Confirmation3', name, amount, dates, total, seats, num_seats)
        self.final_selected_seats.update(seats)
        self.selected_seats3.clear()
    def on_click_logout(self):
        self.parent.change_window('LoginPage')

class Confirmation1(tk.Frame):
    def __init__(self, master, name, amount, dates, total, seats, num_seats):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.movie_name = name
        self.movie_total = total
        self.movie_dates = dates
        self.movie_amount = amount
        self.movie_seats = seats
        self.movie_num_seats = num_seats
        self.configure(bg='white')
        self.show_canvas()

    def show_canvas(self):
        self.canvas_width = self.winfo_screenwidth() //1
        self.canvas_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.movie_selection = tk.Label(self, text="Movie Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 5.9, self.canvas_height // 20, window=self.movie_selection)
        self.seat_selection = tk.Label(self, text="Seat Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 1.99, self.canvas_height // 20, window=self.seat_selection)
        self.confirmation = tk.Label(self, text="Confirmation", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 20, window=self.confirmation)
        
        self.mod = tk.Label(self, text="Payment Method", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white')
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 5, window=self.mod)

        self.image = Image.open('gcash.JPG')
        self.image = self.image.resize((120,60))
        self.tk_image = ImageTk.PhotoImage(self.image)

        self.gcash = tk.Label(self, image=self.tk_image, bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 3.8, window=self.gcash)

        self.otc = tk.Label(self, text="OTC", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 4.8, self.canvas_height // 3.81, window=self.otc)

        self.details = tk.Label(self, text="Details:", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 2.7, window=self.details)

        self.name = tk.Label(self, text="Name:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 2.2, window=self.name)

        self.name_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3.7, self.canvas_height // 2.2, window=self.name_ent)

        self.contact = tk.Label(self, text="Contact Number:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2, window=self.contact)

        self.contact_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 2.8, self.canvas_height // 2, window=self.contact_ent)

        self.email = tk.Label(self, text="Email Address:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 6.3, self.canvas_height // 1.85, window=self.email)

        self.email_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3.0009, self.canvas_height // 1.85, window=self.email_ent)

        self.label = tk.Label(self, text="  ", font=("Montserrat", 30, "bold"),fg='white', bg='#DADBDD', height=5, width=17)
        self.canvas.create_window(self.canvas_width // 1.29, self.canvas_height // 2.25, window=self.label)

        self.movie_lb = tk.Label(self, text="Movie Title:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.39, self.canvas_height // 3, window=self.movie_lb)

        self.movie_choose = tk.Label(self, text=self.movie_name, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 3, window=self.movie_choose)

        self.date_lb = tk.Label(self, text="Date:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.35, self.canvas_height // 2.7, window=self.date_lb)

        self.date_choose = tk.Label(self, text=self.movie_dates, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.7, window=self.date_choose)

        self.hm_seats_lb = tk.Label(self, text="Number of seat/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.44, self.canvas_height // 2.47, window=self.hm_seats_lb)

        self.seat_selected = tk.Label(self, text=self.movie_num_seats, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.47, window=self.seat_selected)
        
        self.seats_lb = tk.Label(self, text="Seat number/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.42, self.canvas_height // 2.27, window=self.seats_lb)

        self.number_seats = tk.Label(self, text=self.movie_seats, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.27, window=self.number_seats)

        self.price_lb = tk.Label(self, text="Price per ticket/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.43, self.canvas_height // 2.1, window=self.price_lb)

        self.price = tk.Label(self, text=self.movie_amount, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.1, window=self.price)  

        self.amount_lb = tk.Label(self, text="Total Amount:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 1.9, window=self.amount_lb)

        self.total_amnt = tk.Label(self, text=self.movie_total, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.15, self.canvas_height // 1.9, window=self.total_amnt)

        self.mop2 = tk.Label(self, text='Mode of payment: ', font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.43, self.canvas_height // 1.7, window=self.mop2)

        self.final_mop = tk.Label(self, text='OTC', font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 1.7, window=self.final_mop)

        self.overview = tk.Label(self, text="Overview:", font=("Montserrat", 19, 'bold'),fg='black', bg='white')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 4.4, window=self.overview)

        self.btn_book_ticket = tk.Button(self, text="Book Ticket", font=('Montserrat', 19, 'bold'), fg='white', bg="#00FF00", width=15, height=1, command=self.on_click_save)
        self.canvas.create_window(self.canvas_width // 2, self.canvas_height // 1.4, window=self.btn_book_ticket)

        self.logout = tk.Button(self, text="Logout", font=('Montserrat', 15, 'bold'), fg='white', bg="#3A3B3C", width=12, height=1, command=self.on_click_logout)
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 7, window=self.logout)

        self.movie_selection.bind('<Enter>', self.on_enter_movie)
        self.movie_selection.bind('<Leave>', self.on_leave_movie)
        self.movie_selection.bind('<Button-1>', self.on_click_movie)

        self.seat_selection.bind('<Enter>', self.on_enter_seats)
        self.seat_selection.bind('<Leave>', self.on_leave_seats)
        self.seat_selection.bind('<Button-1>', self.on_click_seat)
        self.gcash.bind('<Button-1>', self.on_click_gcash)
        self.otc.bind('<Button-1>', self.on_click_otc)
    def on_click_gcash(self, event):
        self.final_mop.config(text='GCASH')
    def on_click_otc(self, event):
        self.final_mop.config(text='OTC')
    def on_click_save(self):
        mop = self.final_mop.cget("text")

        if len(self.contact_ent.get()) > 11 or len(self.contact_ent.get()) < 11:
            messagebox.showerror("Error", "Contact number must have 11 digits")
            return
        if len(self.contact_ent.get()) == 0:
            messagebox.showerror("Invalid Input", "Contact number is empty")
            return
        for char in self.name_ent.get():
            if char.isdigit():
                messagebox.showerror("Invalid Input", "Only letters are allowed in name field")
                return
        for char in self.contact_ent.get():
                if not char.isdigit():
                    messagebox.showerror("Invalid Input", "Invalid Contact number")
                    return
        special_chars = string.punctuation + '"'
        if any(char in special_chars for char in self.name_ent.get()):
            messagebox.showerror("Invalid Input", "Input contains special characters in name field!")
            return
        if self.email_ent.get() == '':
            messagebox.showerror("Error", "Email field is empty")
            return
        try: 
            movies = models.Booked()
            movies.cus_name = self.name_ent.get()
            movies.cus_contact = int(self.contact_ent.get())
            movies.cus_email = self.email_ent.get()
            movies.time = datetime.now().strftime('%H:%M:%S')
            movies.movie_title = self.movie_name
            movies.movie_date = self.movie_dates
            movies.num_of_seats = self.movie_num_seats
            movies.seat_num = self.movie_seats
            movies.amount = float(self.movie_amount)
            movies.total = float(self.movie_total)
            movies.mop = mop

            db_conn = db_handler.DBHandler()
            db_conn.book_movie(movies)
            db_conn.close()
            self.name_ent.delete(0, tk.END)
            self.email_ent.delete(0, tk.END)
            self.contact_ent.delete(0, tk.END)
            messagebox.showinfo("Successful", "Movie Ticket Successfully Booked")
            self.parent.change_window('MovieSelection')
        except ValueError:
            messagebox.showerror("Error", "Please check all the fields")
            return
    def on_enter_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_enter_seats(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_seats(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_click_movie(self, event):
        self.parent.change_window('MovieSelection')
    def on_click_seat(self, event):
        name = self.movie_name
        amount = self.movie_amount
        dates = self.movie_dates
        self.parent.change_window('SeatSelection1', name, amount, dates)

    def on_click_logout(self):
        self.parent.change_window('LoginPage')

class Confirmation2(tk.Frame):
    def __init__(self, master, name, amount, dates, total, seats, num_seats):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.movie_name = name
        self.movie_total = total
        self.movie_dates = dates
        self.movie_amount = amount
        self.movie_seats = seats
        self.movie_num_seats = num_seats
        
        self.configure(bg='white')
        self.show_canvas()
    def show_canvas(self):
        self.canvas_width = self.winfo_screenwidth() //1
        self.canvas_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.movie_selection = tk.Label(self, text="Movie Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 5.9, self.canvas_height // 20, window=self.movie_selection)
        self.seat_selection = tk.Label(self, text="Seat Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 1.99, self.canvas_height // 20, window=self.seat_selection)
        self.confirmation = tk.Label(self, text="Confirmation", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 20, window=self.confirmation)
        
        self.mod = tk.Label(self, text="Payment Method", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white')
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 5, window=self.mod)

        self.image = Image.open('gcash.JPG')
        self.image = self.image.resize((120,60))
        self.tk_image = ImageTk.PhotoImage(self.image)

        self.gcash = tk.Label(self, image=self.tk_image, bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 3.8, window=self.gcash)

        self.otc = tk.Label(self, text="OTC", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 4.8, self.canvas_height // 3.81, window=self.otc)

        self.details = tk.Label(self, text="Details:", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 2.7, window=self.details)

        self.name = tk.Label(self, text="Name:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 2.2, window=self.name)

        self.name_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3.7, self.canvas_height // 2.2, window=self.name_ent)

        self.contact = tk.Label(self, text="Contact Number:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2, window=self.contact)

        self.contact_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 2.8, self.canvas_height // 2, window=self.contact_ent)

        self.email = tk.Label(self, text="Email Address:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 6.3, self.canvas_height // 1.85, window=self.email)

        self.email_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3.0009, self.canvas_height // 1.85, window=self.email_ent)

        self.label = tk.Label(self, text="  ", font=("Montserrat", 30, "bold"),fg='white', bg='#DADBDD', height=5, width=17)
        self.canvas.create_window(self.canvas_width // 1.29, self.canvas_height // 2.25, window=self.label)

        self.movie_lb = tk.Label(self, text="Movie Title:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.39, self.canvas_height // 3, window=self.movie_lb)

        self.movie_choose = tk.Label(self, text=self.movie_name, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 3, window=self.movie_choose)

        self.date_lb = tk.Label(self, text="Date:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.35, self.canvas_height // 2.7, window=self.date_lb)

        self.date_choose = tk.Label(self, text=self.movie_dates, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.7, window=self.date_choose)

        self.hm_seats_lb = tk.Label(self, text="Number of seat/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.44, self.canvas_height // 2.47, window=self.hm_seats_lb)

        self.seat_selected = tk.Label(self, text=self.movie_num_seats, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.47, window=self.seat_selected)
        
        self.seats_lb = tk.Label(self, text="Seat number/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.42, self.canvas_height // 2.27, window=self.seats_lb)

        self.number_seats = tk.Label(self, text=self.movie_seats, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.27, window=self.number_seats)

        self.price_lb = tk.Label(self, text="Price per ticket/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.43, self.canvas_height // 2.1, window=self.price_lb)

        self.price = tk.Label(self, text=self.movie_amount, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.1, window=self.price)  

        self.amount_lb = tk.Label(self, text="Total Amount:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 1.9, window=self.amount_lb)

        self.total_amnt = tk.Label(self, text=self.movie_total, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.15, self.canvas_height // 1.9, window=self.total_amnt)

        self.overview = tk.Label(self, text="Overview:", font=("Montserrat", 19, 'bold'),fg='black', bg='white')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 4.4, window=self.overview)

        self.btn_book_ticket = tk.Button(self, text="Book Ticket", font=('Montserrat', 19, 'bold'), fg='white', bg="#00FF00", width=15, height=1, command=self.on_click_save)
        self.canvas.create_window(self.canvas_width // 2, self.canvas_height // 1.4, window=self.btn_book_ticket)

        self.logout = tk.Button(self, text="Logout", font=('Montserrat', 15, 'bold'), fg='white', bg="#3A3B3C", width=12, height=1, command=self.on_click_logout)
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 7, window=self.logout)

        self.mop2 = tk.Label(self, text='Mode of payment: ', font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.43, self.canvas_height // 1.7, window=self.mop2)

        self.final_mop = tk.Label(self, text='OTC', font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 1.7, window=self.final_mop)

        self.movie_selection.bind('<Enter>', self.on_enter_movie)
        self.movie_selection.bind('<Leave>', self.on_leave_movie)
        self.movie_selection.bind('<Button-1>', self.on_click_movie)

        self.seat_selection.bind('<Enter>', self.on_enter_seats)
        self.seat_selection.bind('<Leave>', self.on_leave_seats)
        self.seat_selection.bind('<Button-1>', self.on_click_seat)
        self.gcash.bind('<Button-1>', self.on_click_gcash)
        self.otc.bind('<Button-1>', self.on_click_otc)
    def on_click_gcash(self, event):
        self.final_mop.config(text='GCASH')
    def on_click_otc(self, event):
        self.final_mop.config(text='OTC')
    def on_click_save(self):
        mop = self.final_mop.cget("text")
        try: 
            movies = models.Booked()
            movies.cus_name = self.name_ent.get()
            movies.cus_contact = int(self.contact_ent.get())
            movies.cus_email = self.email_ent.get()
            movies.time = datetime.now().strftime('%H:%M:%S')
            movies.movie_title = self.movie_name
            movies.movie_date = self.movie_dates
            movies.num_of_seats = self.movie_num_seats
            movies.seat_num = self.movie_seats
            movies.amount = float(self.movie_amount)
            movies.total = float(self.movie_total)
            movies.mop = mop

            db_conn = db_handler.DBHandler()
            db_conn.book_movie(movies)
            db_conn.close()
            messagebox.showinfo("Successful", "Movie Ticket Successfully Booked")
            self.name_ent.delete(0, tk.END)
            self.email_ent.delete(0, tk.END)
            self.contact_ent.delete(0, tk.END)
            self.parent.change_window('MovieSelection')
        except ValueError:
            messagebox.showerror("Error", "Please check all the fields")
            return
    def on_enter_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_enter_seats(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_seats(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_click_movie(self, event):
        self.parent.change_window('MovieSelection')
    def on_click_seat(self, event):
        name = self.movie_name
        amount = self.movie_amount
        dates = self.movie_dates
        self.parent.change_window('SeatSelection2', name, amount, dates)
    def on_click_logout(self):
        self.parent.change_window('LoginPage')

class Confirmation3(tk.Frame):
    def __init__(self, master, name, amount, dates, total, seats, num_seats):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.movie_name = name
        self.movie_total = total
        self.movie_dates = dates
        self.movie_amount = amount
        self.movie_seats = seats
        self.movie_num_seats = num_seats
        
        self.configure(bg='white')
        self.show_canvas()
    def show_canvas(self):
        self.canvas_width = self.winfo_screenwidth() //1
        self.canvas_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.movie_selection = tk.Label(self, text="Movie Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 5.9, self.canvas_height // 20, window=self.movie_selection)
        self.seat_selection = tk.Label(self, text="Seat Selection", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 1.99, self.canvas_height // 20, window=self.seat_selection)
        self.confirmation = tk.Label(self, text="Confirmation", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=27, height=2, cursor='hand2')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 20, window=self.confirmation)
        
        self.mod = tk.Label(self, text="Payment Method", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white')
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 5, window=self.mod)

        self.image = Image.open('gcash.JPG')
        self.image = self.image.resize((120,60))
        self.tk_image = ImageTk.PhotoImage(self.image)

        self.gcash = tk.Label(self, image=self.tk_image, bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 3.8, window=self.gcash)

        self.otc = tk.Label(self, text="OTC", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 4.8, self.canvas_height // 3.81, window=self.otc)

        self.details = tk.Label(self, text="Details:", font=("Montserrat", 19, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 2.7, window=self.details)

        self.name = tk.Label(self, text="Name:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 8.1, self.canvas_height // 2.2, window=self.name)

        self.name_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3.7, self.canvas_height // 2.2, window=self.name_ent)

        self.contact = tk.Label(self, text="Contact Number:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2, window=self.contact)

        self.contact_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 2.8, self.canvas_height // 2, window=self.contact_ent)

        self.email = tk.Label(self, text="Email Address:", font=("Montserrat", 15, 'bold'), fg='#3A3B3C', bg='white', cursor='hand2')
        self.canvas.create_window(self.canvas_width // 6.3, self.canvas_height // 1.85, window=self.email)

        self.email_ent = tk.Entry(self, width= 50, bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3.0009, self.canvas_height // 1.85, window=self.email_ent)

        self.label = tk.Label(self, text="  ", font=("Montserrat", 30, "bold"),fg='white', bg='#DADBDD', height=5, width=17)
        self.canvas.create_window(self.canvas_width // 1.29, self.canvas_height // 2.25, window=self.label)

        self.movie_lb = tk.Label(self, text="Movie Title:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.39, self.canvas_height // 3, window=self.movie_lb)

        self.movie_choose = tk.Label(self, text=self.movie_name, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 3, window=self.movie_choose)

        self.date_lb = tk.Label(self, text="Date:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.35, self.canvas_height // 2.7, window=self.date_lb)

        self.date_choose = tk.Label(self, text=self.movie_dates, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.7, window=self.date_choose)

        self.hm_seats_lb = tk.Label(self, text="Number of seat/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.44, self.canvas_height // 2.47, window=self.hm_seats_lb)

        self.seat_selected = tk.Label(self, text=self.movie_num_seats, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.47, window=self.seat_selected)
        
        self.seats_lb = tk.Label(self, text="Seat number/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.42, self.canvas_height // 2.27, window=self.seats_lb)

        self.number_seats = tk.Label(self, text=self.movie_seats, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.27, window=self.number_seats)

        self.price_lb = tk.Label(self, text="Price per ticket/s:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.43, self.canvas_height // 2.1, window=self.price_lb)

        self.price = tk.Label(self, text=self.movie_amount, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 2.1, window=self.price)  

        self.amount_lb = tk.Label(self, text="Total Amount:", font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 1.9, window=self.amount_lb)

        self.total_amnt = tk.Label(self, text=self.movie_total, font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.15, self.canvas_height // 1.9, window=self.total_amnt)

        self.overview = tk.Label(self, text="Overview:", font=("Montserrat", 19, 'bold'),fg='black', bg='white')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 4.4, window=self.overview)

        self.btn_book_ticket = tk.Button(self, text="Book Ticket", font=('Montserrat', 19, 'bold'), fg='white', bg="#00FF00", width=15, height=1, command=self.on_click_save)
        self.canvas.create_window(self.canvas_width // 2, self.canvas_height // 1.4, window=self.btn_book_ticket)

        self.logout = tk.Button(self, text="Logout", font=('Montserrat', 15, 'bold'), fg='white', bg="#3A3B3C", width=12, height=1, command=self.on_click_logout)
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 7, window=self.logout)

        self.mop2 = tk.Label(self, text='Mode of payment: ', font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.43, self.canvas_height // 1.7, window=self.mop2)

        self.final_mop = tk.Label(self, text='OTC', font=("Montserrat", 15),fg='black', bg='#DADBDD')
        self.canvas.create_window(self.canvas_width // 1.2, self.canvas_height // 1.7, window=self.final_mop)

        self.movie_selection.bind('<Enter>', self.on_enter_movie)
        self.movie_selection.bind('<Leave>', self.on_leave_movie)
        self.movie_selection.bind('<Button-1>', self.on_click_movie)

        self.seat_selection.bind('<Enter>', self.on_enter_seats)
        self.seat_selection.bind('<Leave>', self.on_leave_seats)
        self.seat_selection.bind('<Button-1>', self.on_click_seat)
        self.gcash.bind('<Button-1>', self.on_click_gcash)
        self.otc.bind('<Button-1>', self.on_click_otc)
    def on_click_gcash(self, event):
        self.final_mop.config(text='GCASH')
    def on_click_otc(self, event):
        self.final_mop.config(text='OTC')
    def on_click_save(self):
        mop = self.final_mop.cget("text")
        try: 
            movies = models.Booked()
            movies.cus_name = self.name_ent.get()
            movies.cus_contact = int(self.contact_ent.get())
            movies.cus_email = self.email_ent.get()
            movies.time = datetime.now().strftime('%H:%M:%S')
            movies.movie_title = self.movie_name
            movies.movie_date = self.movie_dates
            movies.num_of_seats = self.movie_num_seats
            movies.seat_num = self.movie_seats
            movies.amount = float(self.movie_amount)
            movies.total = float(self.movie_total)
            movies.mop = mop

            db_conn = db_handler.DBHandler()
            db_conn.book_movie(movies)
            db_conn.close()
            self.name_ent.delete(0, tk.END)
            self.email_ent.delete(0, tk.END)
            self.contact_ent.delete(0, tk.END)
            messagebox.showinfo("Successful", "Movie Ticket Successfully Booked")
            self.parent.change_window('MovieSelection')
        except ValueError:
            messagebox.showerror("Error", "Please check all the fields")
            return
    def on_enter_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_movie(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_enter_seats(self, event):
        self.seat_selection.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_seats(self, event):
        self.seat_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.movie_selection.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.confirmation.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_click_movie(self, event):
        self.parent.change_window('MovieSelection')
    def on_click_seat(self, event):
        name = self.movie_name
        amount = self.movie_amount
        dates = self.movie_dates
        self.parent.change_window('SeatSelection3', name, amount, dates)
    def on_click_logout(self):
        self.parent.change_window('LoginPage')

class ViewDatabase(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.cal_get = None
        self.slct_file = None
        self.poster_img = None
        self.frame = None

        self.search_lb = tk.Label(self, text="Search:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.search_lb.grid(row=1, column=0, columnspan=1, sticky='e')
        self.search_ent = tk.Entry(self, width=40, font=(15), bg='#F5F5F5')
        self.search_ent.grid(row=1, column=1, padx=5, sticky='w')
        self.logout = tk.Button(self, text="Logout", font=('Montserrat', 15, 'bold'), fg='white', bg="#3A3B3C", width=10 , command=self.on_click_logout)
        self.logout.grid(row=1, column=1, sticky='e', padx=40, pady=20)

        self.configure(bg='white')
        self.edit = tk.Label(self, text="Edit Movies", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=40, height=2, cursor='hand2')
        self.edit.grid(row=0, column=0)
        self.history = tk.Label(self, text="View History", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=40, height=2, cursor='hand2')
        self.history.grid(row=0, column=1)

        self.history.bind('<Enter>', self.on_enter_history)
        self.history.bind('<Leave>', self.on_leave_history)
        self.history.bind("<Button-1>", self.on_click_history)
        self.canvas_width = self.winfo_screenwidth() //1
        self.canvas_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white', highlightbackground='white')
        self.canvas.grid(row=2, column=0, columnspan=2)

        columns = ('poster', 'name', 'amount', 'sched')
        
        self.table = ttk.Treeview(self.canvas, columns=columns, show='headings')

        self.table.heading('poster', text='Poster')
        self.table.heading('name', text='Movie Name')
        self.table.heading('amount', text='Amount')
        self.table.heading('sched', text='Schedule')

        self.update_movie_table()
        self.table.bind("<<TreeviewSelect>>", self.on_movie_select)

        self.canvas.create_window(self.canvas_width // 2, self.canvas_height // 6, window=self.table)

        self.poster = tk.Button(self, text="Add Poster", font=('Montserrat', 13, 'bold'), fg='white', bg="#3A3B3C", command=self.select_poster)
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2.4, window=self.poster)

        self.poster_lb = tk.Label(self,bg='#3A3B3C', text='No poster', fg='white', font=('Montserrat', 13, 'bold'))
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 2.4, window=self.poster_lb)

        self.movie_name = tk.Label(self, text="Movie Name:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 1.86, window=self.movie_name)

        self.movie_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 1.86, window=self.movie_ent)

        self.calendar = tk.Button(self, text="Calendar", font=('Montserrat', 13, 'bold'), fg='white', bg="#3A3B3C", command=self.create_baby_frame)
        self.canvas.create_window(self.canvas_width // 1.8, self.canvas_height // 2.4, window=self.calendar)

        self.calendar_ent = tk.Entry(self, state='readonly', width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 1.4, self.canvas_height // 2.4, window=self.calendar_ent)

        self.amount = tk.Label(self, text="Amount:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 1.8, self.canvas_height // 1.86, window=self.amount)

        self.amount_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 1.4, self.canvas_height // 1.86, window=self.amount_ent)

        self.add_movie = tk.Button(self, text="Add Movie", font=('Montserrat', 17, 'bold'), fg='white', bg="#00FF00", width=12, height=1, command=self.add_movie_to_database)
        self.canvas.create_window(self.canvas_width // 1.5, self.canvas_height // 1.6, window=self.add_movie)

        self.clear = tk.Button(self, text="Clear Fields", font=('Montserrat', 14, 'bold'), fg='white', bg="#3A3B3C", width=10, command=self.clear_fields)
        self.canvas.create_window(self.canvas_width // 1.4, self.canvas_height // 2.8, window=self.clear)

        self.remove_movie = tk.Button(self, text="Remove Movie", font=('Montserrat', 17, 'bold'), fg='white', bg="red", width=12, height=1, command=self.delete_movie)
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 1.6, window=self.remove_movie)

        self.search_ent.bind('<KeyRelease>', self.update_movie_table)
        
    def clear_fields(self):
        self.movie_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.calendar_ent.delete(0, tk.END)
        self.selected_file = None
        self.poster_lb.configure(text="No poster")
        self.poster_lb.config(image="")

    def delete_movie(self):
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Delete Movie", "Select a movie to delete.")
            return
        
        proceed = messagebox.askyesno("Delete Movie", "Do you want to delete the selected Movie?")

        if not proceed:
            return

        for item in selected_items:
            selected = self.table.item(item)['values'][1]

            db_conn = db_handler.DBHandler()
            db_conn.delete_movie(selected)
            db_conn.close()

            self.update_movie_table()
        self.movie_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.calendar_ent.delete(0, tk.END)
        self.selected_file = None
        self.poster_lb.configure(text="No poster")
        self.poster_lb.config(image="")
    def update_movie_table(self, event=None):
        self.get_movies()
        self.table.delete(*self.table.get_children())
        for movies in self.movie_list:
            row = (movies.poster, movies.name, movies.amount, movies.sched)
            self.table.insert('', tk.END, values=row)
        self.table.bind("<<TreeviewSelect>>", self.on_movie_select)
    
    def get_movies(self):
        key = self.search_ent.get()
        db_conn = db_handler.DBHandler()
        self.movie_list = db_conn.search_movie(key)
        db_conn.close()
    
    def create_baby_frame(self):
        self.calendar_ent.config(state='normal')
        if self.frame is not None:
            return
        self.frame = tk.Frame(self.canvas, width=300, height=300, bg='white')
        self.canvas.create_window(self.canvas.winfo_width() // 1.12, self.canvas.winfo_height() // 3.7, window=self.frame)

        self.calendar = Calendar(self.frame)
        self.calendar.pack()

        self.button = tk.Button(self.frame, text="Save", command=self.get_schedule, width=15)
        self.button.pack()
        self.back_btn = tk.Button(self.frame, text='Back', command=self.back, width =15)
        self.back_btn.pack()

    def back(self):
        self.calendar_ent.delete(0, tk.END)
        self.calendar_ent.config(state='readonly')
        self.frame.destroy()
        self.frame = None

    def get_schedule(self):
        self.cal_get = self.calendar.selection_get()
        selected_day_month_year = self.cal_get.strftime("%m/%d/%Y")
        self.calendar_ent.delete(0, tk.END)
        self.calendar_ent.insert(tk.END, selected_day_month_year)
        self.calendar_ent.config(state='readonly')
        self.frame.destroy()
        self.frame = None

    def on_click_logout(self):
        self.parent.change_window('LoginPage')
    
    def select_poster(self):
        file_types = (("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*"))
        self.selected_file = filedialog.askopenfilename(filetypes=file_types)
        if self.selected_file:
            self.display_poster()

    def display_poster(self):
        image = Image.open(self.selected_file)
        image = image.resize((150, 150), Image.ANTIALIAS)
        self.poster_image = ImageTk.PhotoImage(image)
        self.poster_lb.configure(text="", image=self.poster_image)
        self.poster_lb.image = self.poster_image
    
    def add_movie_to_database(self):
        
        self.calendar_ent.config(state='normal')
        name = self.movie_ent.get()
        amount = self.amount_ent.get()
        sched = self.cal_get.strftime("%m/%d/%Y")

        for char in amount:
                if not char.isdigit():
                    messagebox.showerror("Invalid Input", "Invalid amount")
                    return
        special_chars = string.punctuation + '"'
        
        if name == "":
            messagebox.showerror("Error", "Name field is empty")
            return
        elif len(amount) == 0:
            messagebox.showerror("Error", "Amount is empty")
            return
        elif any(char in special_chars for char in name):
            messagebox.showerror("Invalid Input", "Input contains special characters in name field!")
            return
        elif any(char in special_chars for char in amount):
            messagebox.showerror("Invalid Input", "Input contains special characters in amount field!")
            return

        folder_name = self.cal_get.strftime("%m_%d_%Y")
                
        if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                    
        with open(self.selected_file, "rb") as file:
            blob_data = file.read()
                    
        file_path = os.path.join(folder_name, f"{str(name)}.jpg")
                    
        with open(file_path, "wb") as file:
            file.write(blob_data)
                    
        movie = models.Movies(blob_data)
        movie.name = name
        movie.amount = amount
        movie.sched = sched
        self.parent.db_handler.insert_movie(movie)
                
        self.movie_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.calendar_ent.delete(0, tk.END)
        self.selected_file = None
        self.poster_lb.configure(text="No poster")
        self.poster_lb.config(image="")

        messagebox.showinfo("Success", "Movie added to the database.")
        self.calendar_ent.config(state='readonly')
        self.update_movie_table()
        
    def on_movie_select(self, event):
        self.calendar_ent.config(state='normal')
        selected_item = self.table.selection()
        if selected_item:
            values = self.table.item(selected_item)['values']
            poster_data, name, amount, sched = values
            self.movie_ent.delete(0, tk.END)
            self.movie_ent.insert(tk.END, name)
            self.amount_ent.delete(0, tk.END)
            self.amount_ent.insert(tk.END, amount)
            self.calendar_ent.delete(0, tk.END)
            self.calendar_ent.insert(tk.END, sched)
            folder_name = str(sched).replace("/", "_") 
            file_path = os.path.join(folder_name, f"{name}.jpg")  
            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    file.read()
                image = Image.open(file_path)
                image = image.resize((150, 150))
                photo = ImageTk.PhotoImage(image)

                self.poster_lb.configure(image=photo)
                self.poster_lb.image = photo
            else:
                print(f"File not found: {file_path}")
    
    def on_enter_history(self, event):
        self.history.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.edit.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_history(self, event):
        self.history.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.edit.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_click_history(self, event):
        self.movie_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.calendar_ent.delete(0, tk.END)
        self.selected_file = None
        self.poster_lb.configure(text="No poster")
        self.poster_lb.config(image="")
        self.parent.change_window('ViewHistory')

class ViewHistory(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master

        self.search_lb = tk.Label(self, text="Search:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.search_lb.grid(row=1, column=0, columnspan=1, sticky='e')
        self.search_ent = tk.Entry(self, width=40, font=(15), bg='#F5F5F5')
        self.search_ent.grid(row=1, column=1, padx=5, sticky='w')
        self.logout = tk.Button(self, text="Logout", font=('Montserrat', 15, 'bold'), fg='white', bg="#3A3B3C", width=10 , command=self.on_click_logout)
        self.logout.grid(row=1, column=1, sticky='e', padx=40, pady=20)

        self.configure(bg='white')
        self.edit = tk.Label(self, text="Edit Movies", font=("Montserrat", 19, "bold"), fg='#3A3B3C', bg='white', width=40, height=2, cursor='hand2')
        self.edit.grid(row=0, column=0)
        self.history = tk.Label(self, text="View History", font=("Montserrat", 19, "bold"), fg='white', bg='#3A3B3C', width=40, height=2, cursor='hand2')
        self.history.grid(row=0, column=1)

        self.search_ent.bind('<KeyRelease>', self.update_movie_table)
        self.canvas_width = self.winfo_screenwidth() //1
        self.canvas_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white', highlightbackground='white')
        self.canvas.grid(row=2, column=0, columnspan=2)
        
    
        columns = ('name', 'contact', 'email', 'time', 'title', 'date', 'numseats', 'seatnum', 'amount', 'total', 'mop')
        
        self.table = ttk.Treeview(self.canvas, columns=columns, show='headings')

        self.table.heading('name', text='Name')
        self.table.heading('contact', text='Contact')
        self.table.heading('email', text='Email')
        self.table.heading('time', text='Time')
        self.table.heading('title', text='Movie')
        self.table.heading('date', text='Date')
        self.table.heading('numseats', text='Number seat/s')
        self.table.heading('seatnum', text='Seat Number')
        self.table.heading('amount', text='Amount')
        self.table.heading('total', text='Total')
        self.table.heading('mop', text='MOP')

        self.table.column('name', width=120)
        self.table.column('contact', width=120)
        self.table.column('email', width=120)
        self.table.column('time', width=120)
        self.table.column('title', width=120)
        self.table.column('date', width=120)
        self.table.column('numseats', width=120)
        self.table.column('seatnum', width=120)
        self.table.column('amount', width=120)
        self.table.column('total', width=120)
        self.table.column('mop', width=120)
        
        
        self.table.bind("<<TreeviewSelect>>", self.on_movie_select)
        self.update_movie_table()
        self.canvas.create_window(self.canvas_width // 2, self.canvas_height // 6, window=self.table)


        self.name = tk.Label(self, text="Name:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2.9, window=self.name)

        self.name_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 2.9, window=self.name_ent)

        self.contact = tk.Label(self, text="Contact:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2.57, window=self.contact)

        self.contact_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 2.57, window=self.contact_ent)

        self.time = tk.Label(self, text="Time:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2.3, window=self.time)

        self.time_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 2.3, window=self.time_ent)

        self.title = tk.Label(self, text="Movie Title:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 2.1, window=self.title)

        self.title_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 2.1, window=self.title_ent)

        self.date = tk.Label(self, text="Date:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 6, self.canvas_height // 1.9, window=self.date)

        self.date_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 1.9, window=self.date_ent)


        self.numseats = tk.Label(self, text="Number of Seat/s:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 1.7, self.canvas_height // 2.9, window=self.numseats)

        self.numseat_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 2.9, window=self.numseat_ent)

        self.seatnum = tk.Label(self, text="Seat Number/s:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 1.7, self.canvas_height // 2.57, window=self.seatnum)

        self.seatnum_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 2.57, window=self.seatnum_ent)

        self.amount = tk.Label(self, text="Amount:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 1.7, self.canvas_height // 2.3, window=self.amount)

        self.amount_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 2.3, window=self.amount_ent)

        self.total = tk.Label(self, text="Total:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 1.7, self.canvas_height // 2.1, window=self.total)

        self.total_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 2.1, window=self.total_ent)

        self.mop = tk.Label(self, text="Mode of Payment:", font=('Montserrat', 13, 'bold'), fg='#3A3B3C', bg="white")
        self.canvas.create_window(self.canvas_width // 1.7, self.canvas_height // 1.9, window=self.mop)

        self.mop_ent = tk.Entry(self, width=30, font=(15), bg='#F5F5F5')
        self.canvas.create_window(self.canvas_width // 1.3, self.canvas_height // 1.9, window=self.mop_ent)

        self.remove_movie = tk.Button(self, text="Remove Movie", font=('Montserrat', 17, 'bold'), fg='white', bg="red", width=12, height=1, command=self.delete_ticket)
        self.canvas.create_window(self.canvas_width // 1.4, self.canvas_height // 1.6, window=self.remove_movie)

        self.clear = tk.Button(self, text="Clear Fields", font=('Montserrat', 17, 'bold'), fg='white', bg="#3A3B3C", width=12, height=1, command=self.clear_fields)
        self.canvas.create_window(self.canvas_width // 3, self.canvas_height // 1.6, window=self.clear)
        self.edit.bind('<Enter>', self.on_enter_edit)
        self.edit.bind('<Leave>', self.on_leave_edit)
        self.edit.bind("<Button-1>", self.on_click_edit)
    def clear_fields(self):
        self.name_ent.delete(0, tk.END)
        self.contact_ent.delete(0, tk.END)
        self.time_ent.delete(0, tk.END)
        self.title_ent.delete(0, tk.END)
        self.date_ent.delete(0, tk.END)
        self.numseat_ent.delete(0, tk.END)
        self.seatnum_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.total_ent.delete(0, tk.END)
        self.mop_ent.delete(0, tk.END)
    def on_click_logout(self):
        self.name_ent.delete(0, tk.END)
        self.contact_ent.delete(0, tk.END)
        self.time_ent.delete(0, tk.END)
        self.title_ent.delete(0, tk.END)
        self.date_ent.delete(0, tk.END)
        self.numseat_ent.delete(0, tk.END)
        self.seatnum_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.total_ent.delete(0, tk.END)
        self.mop_ent.delete(0, tk.END)
        self.parent.change_window('LoginPage')
        
    def update_movie_table(self, event=None):
        self.get_movies()
        self.table.delete(*self.table.get_children())
        for movies in self.movie_list:
            row = (
                movies.cus_name,
                movies.cus_contact,
                movies.cus_email,
                movies.time,
                movies.movie_title,
                movies.movie_date,
                movies.num_of_seats,
                movies.seat_num,
                movies.amount,
                movies.total,
                movies.mop,
            )
            self.table.insert('', tk.END, values=row)
        self.table.bind("<<TreeviewSelect>>", self.on_movie_select)
    def get_movies(self):
        key = self.search_ent.get()
        db_conn = db_handler.DBHandler()
        self.movie_list = db_conn.search_ticket(key)
        
        db_conn.close()
        # self.update_movie_table()

    def on_movie_select(self, event):
        selected_item = self.table.selection()
        if selected_item:
            values = self.table.item(selected_item)['values']
            cus_name, cus_contact, cus_email, time, movie_title, movie_date, num_of_seats, seat_num, amount, total, mop = values
            self.name_ent.delete(0, tk.END)
            self.name_ent.insert(tk.END, cus_name)
            self.contact_ent.delete(0, tk.END)
            self.contact_ent.insert(tk.END, cus_contact)
            self.time_ent.delete(0, tk.END)
            self.time_ent.insert(tk.END, time)
            self.title_ent.delete(0, tk.END)
            self.title_ent.insert(tk.END, movie_title)
            self.date_ent.delete(0, tk.END)
            self.date_ent.insert(tk.END, movie_date)
            self.numseat_ent.delete(0, tk.END)
            self.numseat_ent.insert(tk.END, num_of_seats)
            self.seatnum_ent.delete(0, tk.END)
            self.seatnum_ent.insert(tk.END, seat_num)
            self.amount_ent.delete(0, tk.END)
            self.amount_ent.insert(tk.END, amount)
            self.total_ent.delete(0, tk.END)
            self.total_ent.insert(tk.END, total)
            self.mop_ent.delete(0, tk.END)
            self.mop_ent.insert(tk.END, mop)

    def delete_ticket(self):
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Delete Movie", "Select a movie to delete.")
            return
        
        proceed = messagebox.askyesno("Delete Movie", "Do you want to delete the selected Movie?")

        if not proceed:
            return

        for item in selected_items:
            selected = self.table.item(item)['values'][0]

            db_conn = db_handler.DBHandler()
            db_conn.delete_ticket(selected)
            db_conn.close()

            self.update_movie_table()
        self.name_ent.delete(0, tk.END)
        self.contact_ent.delete(0, tk.END)
        self.time_ent.delete(0, tk.END)
        self.title_ent.delete(0, tk.END)
        self.date_ent.delete(0, tk.END)
        self.numseat_ent.delete(0, tk.END)
        self.seatnum_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.total_ent.delete(0, tk.END)
        self.mop_ent.delete(0, tk.END)

    def on_enter_edit(self, event):
        self.edit.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
        self.history.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
    def on_leave_edit(self, event):
        self.edit.configure(fg='white', bg='#3A3B3C', font=("Montserrat", 19, "bold"))
        self.history.configure(fg='#3A3B3C', bg='white', font=("Montserrat", 19, "bold"))
    def on_click_edit(self, event):
        self.name_ent.delete(0, tk.END)
        self.contact_ent.delete(0, tk.END)
        self.time_ent.delete(0, tk.END)
        self.title_ent.delete(0, tk.END)
        self.date_ent.delete(0, tk.END)
        self.numseat_ent.delete(0, tk.END)
        self.seatnum_ent.delete(0, tk.END)
        self.amount_ent.delete(0, tk.END)
        self.total_ent.delete(0, tk.END)
        self.mop_ent.delete(0, tk.END)
        self.parent.change_window('ViewDatabase')

import tkinter as tk
import pages
import db_handler

    
class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Movie Ticket Booking System")
        self.db_handler = db_handler.DBHandler()
        self.frames = dict()
        self.frames['LoginPage'] = pages.LoginPage(self)
        self.frames['Sign-upPage'] = pages.SignUpPage(self)
        self.frames['MovieSelection'] = pages.MovieSelection(self)
        self.frames['SeatSelection1'] = pages.SeatSelection1(self, movie_name = "", movie_amount= 0, dates= '')
        self.frames['SeatSelection2'] = pages.SeatSelection2(self, movie_name = "", movie_amount= 0, dates= '')
        self.frames['SeatSelection3'] = pages.SeatSelection3(self, movie_name = "", movie_amount= 0, dates= '')
        self.frames['Confirmation1'] = pages.Confirmation1(self, name = '', amount= 0.0, dates='', total= 0.0, seats= '', num_seats='')
        self.frames['Confirmation2'] = pages.Confirmation2(self, name = '', amount= 0.0, dates='', total= 0.0, seats= '', num_seats='')
        self.frames['Confirmation3'] = pages.Confirmation3(self, name = '', amount= 0.0, dates='', total= 0.0, seats= '', num_seats='')
        self.frames['ViewDatabase'] = pages.ViewDatabase(self)
        self.frames['ViewHistory'] = pages.ViewHistory(self)
        
        self.change_window('LoginPage')
   

    def change_window(self, name, *args):
        for frame in self.frames.values():
            frame.grid_forget()
        
        if name == 'SeatSelection1':
            movie_name, movie_amount, dates = args
            self.frames[name] = pages.SeatSelection1(self, movie_name, movie_amount, dates)
        elif name == 'SeatSelection2':
            movie_name, movie_amount, dates = args
            self.frames[name] = pages.SeatSelection2(self, movie_name, movie_amount, dates)
        elif name == 'SeatSelection3':
            movie_name, movie_amount, dates = args
            self.frames[name] = pages.SeatSelection3(self, movie_name, movie_amount, dates)
        elif name == 'Confirmation1':
            name, amount, dates, total, seats, num_seats = args
            self.frames[name] = pages.Confirmation1(self, name, amount, dates, total, seats, num_seats)
        elif name == 'Confirmation2':
            name, amount, dates, total, seats, num_seats = args
            self.frames[name] = pages.Confirmation2(self, name, amount, dates, total, seats, num_seats)
        elif name == 'Confirmation3':
            name, amount, dates, total, seats, num_seats = args
            self.frames[name] = pages.Confirmation3(self, name, amount, dates, total, seats, num_seats)
        self.frames[name].grid(row=0, column=0)

#                        username  password
# ADMIN ACCOUNT:          admin    admin123
# EMPLOYEE ACCOUNT:       mhyk      makmak

# RENAME FIRST THE FOLDERS TO CURRENT DATE, FORMAT IS MM_DD_YYYY. TO RUN THE PROGRAM 

root = MainWindow()
root.state('zoomed')
root.mainloop()
        
import sqlite3
from datetime import datetime
import models
import base64

class DBHandler:
    def __init__(self):
        self.acc_db = 'database.db'
        self.admin_table = 'admin_account'
        self.emp_table = 'employee_account'
        self.movie_table = 'movies'
        self.booked_movie_table = 'booked_movies'

        self.conn = sqlite3.connect(self.acc_db)
        self.cursor = self.conn.cursor()

    def book_movie(self, movies):
        query = "INSERT INTO booked_movies (cus_name, cus_contact, cus_email, time_of_book, movie_title, movie_date, number_of_seats, seat_num, amount, total, mop) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        seat_num_str = ', '.join(str(num) for num in movies.seat_num)
        values = (
            movies.cus_name,
            movies.cus_contact,
            movies.cus_email,
            movies.time,
            movies.movie_title,
            movies.movie_date,
            movies.num_of_seats,
            seat_num_str,
            movies.amount,
            movies.total,
            movies.mop
        )
        self.cursor.execute(query, values)
        self.conn.commit()

    def search_movie(self, key):
        key = '%' + key + '%'
        query = f'SELECT * FROM {self.movie_table} WHERE name LIKE? OR schedule LIKE? ORDER BY schedule'
        values = (key,key)
        self.cursor.execute(query, values)
        
        movies = []
        for row in self.cursor:
            movie = models.Movies()
            movie.poster = base64.b64decode(row[0])
            movie.name = row[1]
            movie.amount = row[2]
            movie.sched = row[3]
            movies.append(movie)
        
        return movies
    def search_ticket(self, key):
        key = '%' + key + '%'
        query = f'SELECT * FROM {self.booked_movie_table} WHERE cus_name LIKE? OR time_of_book LIKE? OR movie_title LIKE? OR movie_date LIKE? ORDER BY cus_name'
        values = (key,key,key,key)
        self.cursor.execute(query, values)
        
        movies = []
        for row in self.cursor:
            ticket = models.Booked()
            ticket.cus_name = row[0]
            ticket.cus_contact = row[1]
            ticket.cus_email = row[2]
            ticket.time = row[3]
            ticket.movie_title = row[4]
            ticket.movie_date = row[5]
            ticket.num_of_seats = row[6]
            ticket.seat_num = row[7]
            ticket.amount = row[8]
            ticket.total = row[9]
            ticket.mop = row[10]
            movies.append(ticket)
        
        return movies
    
    def search_movie_selection(self, key):
        key = '%' + key + '%'
        query = f'SELECT * FROM {self.movie_table} WHERE schedule LIKE? ORDER BY schedule'
        values = (key,)
        self.cursor.execute(query, values)

        rows = self.cursor.fetchall()

        movies = []
        for row in rows:
            movie = models.Movies()
            movie.poster = base64.b64decode(row[0])
            movie.name = row[1]
            movie.amount = row[2]
            movie.sched = row[3]
            movies.append(movie)
        
        return movies
    
    def read_movies(self):
        query = f'SELECT * FROM {self.movie_table}'
        self.cursor.execute(query)

        movies = []
        for row in self.cursor:
            movie = models.Movies()
            movie.poster = base64.b64decode(row[0])
            movie.name = row[1]
            movie.amount = row[2]
            movie.sched = row[3]
            movies.append(movie)
        
        return movies

    def admin_login(self, username, password):
        query = f'SELECT * FROM {self.admin_table} WHERE username=? AND password=?'
        values = (username, password)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False

    def emp_login(self, username, password):
        query = f'SELECT * FROM {self.emp_table} WHERE username=? AND password=?'
        values = (username, password)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def insert_employee(self, employee):
        query = f'INSERT INTO {self.emp_table} (name, birthdate, contact_num, email, employee_num, username, password) VALUES (?, ?, ?, ?, ?, ?, ?)'
        values = (employee.name, employee.birthdate, employee.contact, employee.email, employee.emp_num, employee.user, employee.password)
        self.cursor.execute(query,values)
        self.conn.commit()
    
    def insert_movie(self, movie):
        query = f'INSERT INTO {self.movie_table} (poster, name, amount, schedule) VALUES (?, ?, ?, ?)'
        values = (movie.poster, movie.name, movie.amount, movie.sched)
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def delete_movie(self, selected):
        query = f"DELETE FROM {self.movie_table} WHERE name = ?"
        values = (selected,)
        self.cursor.execute(query, values)
        self.conn.commit()
    def delete_ticket(self, selected):
        query = f"DELETE FROM {self.booked_movie_table} WHERE cus_name = ?"
        values = (selected,)
        self.cursor.execute(query, values)
        self.conn.commit()
    

    def close(self):
        self.conn.close()

DBHandler().read_movies()
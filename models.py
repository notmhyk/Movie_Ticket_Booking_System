class Account_admin:
    def __init__(self):
        self.username = ''
        self.password = ''

class Account_emp:
    def __init__(self):
        self.name = ''
        self.birthdate = ''
        self.contact_num = 0
        self.email = ''
        self.emp_id = ''
        self.username = ''
        self.password = ''

class Movies:
    def __init__(self, blob_data= None):
        self.poster = blob_data
        self.name = ''
        self.amount = 0.0
        self.sched = ''

class Booked:
    def __init__(self):
        self.cus_name = ''
        self.cus_contact = 0
        self.cus_email = ''
        self.time = ''
        self.movie_title = ''
        self.movie_date = ''
        self.num_of_seats = ''
        self.seat_num = ''
        self.amount = 0.0
        self.total = 0.0
        self.mop = ''
        

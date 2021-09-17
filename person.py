rom datetime import datetime


class person:
    def __int__(self):
        self = self

    def __init__(self, id, name, pnumber, email):
        self.id = id
        self.name = name
        self.pnumber = pnumber
        self.email = email
        self.createdate = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
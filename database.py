import sqlite3

class Database:
    def __init__(self, db_name="fitness.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor
        self.create_table()

    def create_table(self):
        self.cursor.execute(''' CREATE TABLE IF NOT EXIST members
                            (id INTEGER PRIMARY KEY,
                            name TEXT,
                            last_name TEXT,
                            age INTEGER,
                            city TEXT,
                            price REAL,
                            membership_duration INTEGER''')

        self.conn.commit()

    def add_member(self):
        # Method to add a new member.
        pass


    def get_members(self):
        # Method to existing members.
        pass


    def update_member(self):
        # Method to update a member's information.
        pass


    def delete_member(self):
        # Method to delete a member.
        pass


    def __del__(self):
        # destructor
        self.conn.close()
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
                            membership_duration INTEGER''') # Adding columns to members.
        self.conn.commit()


    def add_member(self, name, last_name, age, city, price, membership_duration):
        """
        Method to adds a member.
        :param name:
        :param last_name:
        :param age:
        :param city:
        :param price:
        :param membership_duration:
        :return:
        """
        self.cursor.execute(
            "INSERT INTO members (name, last_name, age, city, price, membership_duration"
            "VALUES (?, ?, ?, ?, ?, ?)",
            name, last_name, age, city, price, membership_duration)
        self.conn.commit()


    def get_members(self):
        """
        Method to show members.
        """
        self.cursor.execute("SELECT * FROM members")
        return self.cursor.fetchall()


    def update_member(self, name, last_name, age, city, price, membership_duration):
        """
        Method to update a member's information.
        :param name:
        :param last_name:
        :param age:
        :param city:
        :param price:
        :param membership_duration:
        :return:
        """
        self.cursor.execute(
            "UPDATE members SET name=?, last_name=?, age=?, city=?, price=?, membership_duration=?"
            "WHERE id=?",
            name, last_name, age, city, price, membership_duration)
        self.conn.commit()


    def delete_member(self, member_id):
        """
        Method to delete a member
        :param member_id:
        :return:
        """
        self.cursor.execute("DELETE FROM members"
                            "WHERE id=?",
                            (member_id,))
        self.conn.commit()

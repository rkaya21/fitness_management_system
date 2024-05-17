import sqlite3


class Database:
    def __init__(self, db_name="fitness.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS members
                            (id INTEGER PRIMARY KEY,
                            name TEXT,
                            last_name TEXT,
                            age INTEGER,
                            city TEXT,
                            price REAL,
                            membership_duration INTEGER)''')
        self.conn.commit()


    def add_member(self, name, last_name, age, city, price, membership_duration):
        """
        Add a new member to the database.
        :param name: Member's first name
        :param last_name: Member's last name
        :param age: Member's age
        :param city: Member's city
        :param price: Membership price
        :param membership_duration: Duration of membership in MONTHS
        """
        self.cursor.execute(
            "INSERT INTO members (name, last_name, age, city, price, membership_duration) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (name, last_name, age, city, price, membership_duration))
        self.conn.commit()


    def get_members(self):
        """
        Show all members from the database.
        :return: List of members
        """
        self.cursor.execute("SELECT * FROM members")
        return self.cursor.fetchall


    def update_member(self, member_id, name, last_name, age, city, price, membership_duration):
        """
        Update member's information in the database.
        :param member_id: Member's ID
        :param name: Member's new first name
        :param last_name: Member's new last name
        :param age: Member's new age
        :param city: Member's new city
        :param price: New membership price
        :param membership_duration: New membership duration in MONTHS
        """
        self.cursor.execute(
            "UPDATE members SET name=?, last_name=?, age=?, city=?, price=?, membership_duration=? "
            "WHERE id=?",
            (name, last_name, age, city, price, membership_duration, member_id))
        self.conn.commit()


    def delete_member(self, member_id):
        """
        Delete a member from the database.
        :param member_id: ID of the member to be deleted
        """
        self.cursor.execute("DELETE FROM members WHERE id=?", (member_id,))
        self.conn.commit()

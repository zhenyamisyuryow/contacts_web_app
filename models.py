import sqlite3
import re

class ContactModel:
    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL
            )
        '''
        try:
            self.conn.execute(query)
            self.conn.commit()
        except:
            return "Error. Unable to create table"
        return "Success."
    

    def get_all_contacts(self):
        query = 'SELECT * FROM contacts ORDER BY name ASC'
        cursor = self.conn.execute(query)
        contacts = cursor.fetchall()
        return contacts
    

    def get_contact(self, contact_id):
        query = 'SELECT * FROM contacts WHERE id = ?'
        cursor = self.conn.execute(query, (contact_id,))
        contact = cursor.fetchone()
        return contact
    
    
    def is_valid_email(self, email):
        return re.match(r'^[a-z0-9]+[._\-+]*[a-z0-9]*@\w+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', email)


    def is_valid_phone(self, phone):
        return re.match(r"\+380{1}[(]{1}\d{2}[)]\d{3}[-]{1}\d{2}[-]{1}\d{2}$", phone)


    def add_contact(self, name, phone, email):
        if not name:
            raise ValueError("Name can not be empty.")
        if not self.is_valid_phone(phone):
            raise ValueError("Invalid phone format. Provide phone in following format: +380(XX)XXX-XX-XX")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format.")
        query = 'INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)'
        self.conn.executemany(query, [(name, phone, email)])
        self.conn.commit()
    

    def update_contact(self, contact_id, name, phone, email):
        if not name:
            raise ValueError("Name can not be empty.")
        if not self.is_valid_phone(phone):
            raise ValueError("Invalid phone format. Provide phone in following format: +380(XX)XXX-XX-XX")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format.")
        query = 'UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?'
        self.conn.execute(query, (name, phone, email, contact_id))
        self.conn.commit()


    def delete_contact(self, contact_id):
        query = 'DELETE FROM contacts WHERE id = ?'
        self.conn.execute(query, (contact_id,))
        self.conn.commit()


    def close_conn(self):
        self.conn.close()
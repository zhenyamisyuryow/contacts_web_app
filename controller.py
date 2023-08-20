from models import ContactModel
from views import ContactView

class ContactController:
    def __init__(self):
        self.model = ContactModel()
        self.view = ContactView()


    def get_contacts(self):
        contacts = self.model.get_all_contacts()
        page = self.view.render_template('home.html', contacts = contacts)
        self.model.close_conn()
        return page
    

    def add_contact(self, params:dict):
        try:
            name = params["name"][0].capitalize()
            phone = params["phone"][0]
            email = params["email"][0]
            self.model.add_contact(name, phone, email)
            self.model.close_conn()
            return self.view.success_message()
        except (KeyError, ValueError) as e:
            if isinstance(e, KeyError):
                return self.view.warning_message(f"{e.args[0].capitalize()} can not be empty", "/")
            return self.view.warning_message(f"{e.args[0]}", "/")

    

    def edit_contact(self, contact_id):
        contact = self.model.get_contact(contact_id)
        self.model.close_conn()
        page = self.view.render_template('update.html', contact = contact)
        return page
    
    
    def update_contact(self, contact_id, params:dict):
        try:
            self.model.update_contact(contact_id, params["name"][0], params["phone"][0], params["email"][0])
            self.model.close_conn()
            return self.view.success_message()
        except (KeyError, ValueError) as e:
            if isinstance(e, KeyError):
                return self.view.warning_message(f"{e.args[0].capitalize()} can not be empty", "/")
            return self.view.warning_message(f"{e.args[0]}", "/")


    def delete_contact(self, contact_id):
        try:
            self.model.delete_contact(contact_id)
            self.model.close_conn()
            return self.view.success_message()
        except AttributeError as e:
            return self.view.warning_message(f"{e.args[0].capitalize()} is required.", "?")
        
    
from models import contact_list, Contact
from views import contact_list_template, contact_template, edit_contact_template, error_page

def list_contacts():
    contacts = ""
    for index, contact in enumerate(contact_list):
        contacts += contact_template.format(name=contact.name, email=contact.email, phone=contact.phone, index=index)
    return contact_list_template.format(contacts=contacts)

def create_contact(params):
    try:
        name = params['name'][0]
        email = params['email'][0]
        phone = params['phone'][0]
    except KeyError as e:
        return f"Please fill out {e.args[0].capitalize()} field."
    
    contact = Contact(name, email, phone)
    contact_list.append(contact)

def edit_contact(index):
    contact = contact_list[index]
    return edit_contact_template.format(name=contact.name, email=contact.email, phone=contact.phone, index=index)

def update_contact(index, params):
    contact = contact_list[index]
    try:
        contact.name = params['name'][0]
        contact.email = params['email'][0]
        contact.phone = params['phone'][0]
    except KeyError as e:
        return f"Please fill out {e.args[0].capitalize()} field."

def delete_contact(index):
    try:
        del contact_list[index]
    except IndexError:
        return "Invalid contact index."
    
def generate_error_page(error_message):
    return error_page.format(error_message=error_message)
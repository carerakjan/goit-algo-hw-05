from decorators import input_error, parse_error


@parse_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated.'

@input_error
def show_phone(args, contacts):
    return contacts[args[0]]


def show_all(contacts):
    return '\n'.join([f'{name}, {num}' for name, num in contacts.items()])
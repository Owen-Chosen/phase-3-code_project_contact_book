import click
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@click.group('mycommands')
def mycommands():
    pass


@click.command()
@click.option('--firstname', required=True, prompt='First name', help='Enter contacts firstname')
@click.option('--lastname', prompt='Lastname', help='Enter contacts lastname')
@click.option('--phone', prompt='Phone number', type=int, help='Enter contacts phone numer')
@click.option('--email', prompt='Email', type=str, help='Enter contacts email')
def register_contact(firstname, lastname, phone, email):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'phone': int(phone),
        'email': email
    }

@click.command()
def show_contacts():
    print("One")

@click.command()
def delete_contact():
    pass

@click.command()
def update_contact():
    pass

Base = declarative_base()
contact = {}

mycommands.add_command(register_contact)
mycommands.add_command(show_contacts)
mycommands.add_command(delete_contact)
mycommands.add_command(update_contact)


if __name__ == '__main__':
    mycommands()
    engine = create_engine('sqlite:///phone_book.db')
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()

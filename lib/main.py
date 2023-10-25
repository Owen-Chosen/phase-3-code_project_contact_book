import click
from models import Contact, session


@click.group('mycommands')
def mycommands():
    pass


@click.command()
@click.option('--firstname', required=True, prompt='First name', help='Enter contacts firstname')
@click.option('--lastname', prompt='Lastname', help='Enter contacts lastname')
@click.option('--phone', prompt='Phone number', type=int, help='Enter contacts phone numer')
@click.option('--email', prompt='Email', type=str, help='Enter contacts email')
def register_contact(firstname, lastname, phone, email):
    new_contact = Contact(
        firstname = firstname,
        lastname = lastname,
        phone = int(phone),
        email = email
    )
    session.add(new_contact)
    session.commit()
    click.echo("SAVED IN DATABASE...")


@click.command()
def show_contacts():
    for contact in session.query(Contact).all():
        click.echo(contact)


@click.command()
@click.option('--id', prompt='Enter contact id', type=int, help='Enter contacts id to be deleted')
def delete_contact(id):
    session.query(Contact).filter(Contact.id==id).delete()
    for contact in session.query(Contact).all():
        click.echo(contact)
    session.commit()


mycommands.add_command(register_contact)
mycommands.add_command(show_contacts)
mycommands.add_command(delete_contact)


if __name__ == '__main__':
    mycommands()
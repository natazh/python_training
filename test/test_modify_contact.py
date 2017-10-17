from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact( firstname="T"))
    app.contact.modify(Contact( firstname="Петр",lastname= "Петров"))


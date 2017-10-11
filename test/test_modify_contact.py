from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact( firstname="Петр",middlename="None",lastname= "Петров", nickname="None",title= "None",company= "None",address= "None",home= "None",mobile= "None",work= "None",fax= "None",email= "None", email_2="None",email_3="None", homepage="None",address2= "None",phone2= "None",
                             notes="None"))
    app.session.logout()

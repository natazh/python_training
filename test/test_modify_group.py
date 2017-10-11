# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
        app.session.login( username="admin", password="secret")
        app.group.modify(Group(name="old", header="None", footer="None"))
        app.session.logout()
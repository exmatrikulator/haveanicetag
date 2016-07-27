#!/usr/bin/env python
# coding: utf8
import os
from flask_script import Manager, Server
from flask_assets import ManageAssets
from webapp.models import Tag
from webapp import app

manager = Manager(app)
manager.add_command("runserver", Server())


@manager.command
def createdb():
    "Inititalise the database"
    from webapp.models import db
    var = input("Drop database [N/y]: ")
    if var.lower() == "y":
        db.drop_all()
    db.create_all()
    db.session.commit()
    #
    # try:
    #     db.session.add( Region( name = "Wuppertal" ) )
    #     db.session.commit()
    # except:
    #     db.session.rollback()
    #


if __name__ == "__main__":
    app.debug = True
    manager.run()

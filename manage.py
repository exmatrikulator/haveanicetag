#!/usr/bin/env python
# coding: utf8
## @file manager

import os
from flask_script import Manager, Server
from flask_assets import ManageAssets
from webapp.models import Tag
from webapp import app,assets_env


manager = Manager(app)
manager.add_command("assets", ManageAssets(assets_env))
manager.add_command("runserver", Server())

## start the tests
@manager.command
def runtest():
    import unittest
    from test import TestUtilMethods
    #unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestUtilMethods)
    unittest.TextTestRunner().run(suite)


@manager.command
def createdb():
    "Inititalise the database"
    from webapp.models import db
    var = input("Drop database [N/y]: ")
    if var.lower() == "y":
        db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    app.debug = True
    manager.run()

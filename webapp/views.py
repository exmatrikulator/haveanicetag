import os
from flask import request, redirect, render_template
from sqlalchemy.orm import joinedload
from webapp import app, db
from webapp.util import *
from webapp.models import *



@app.route("/")
def index():
    print( request.args.getlist('tag'))
    records = db.session.query(Data)
    records = records.options(joinedload(Data.tags))

    for tag in request.args.getlist('tag'):
          records = records.filter( Data.tags.any(Tag.name == tag) )
    records = records.limit(50)
    return render_template('index.html', records = records)


@app.route("/save")
def save():
    print( request.args.getlist('tag'))
    entry = db.session.query(Data)
    for tag in request.args.getlist('tag'):
          entry = entry.filter( Data.tags.any(Tag.name == tag) )
    entry = entry.first()
    print(entry)
    if entry is None:
        entry = Data( tags=get_tag_list(request.args.getlist('tag')), value = request.args.get('value'))
        db.session.add(entry)
        db.session.commit()

    return "ok"

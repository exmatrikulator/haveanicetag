## @package webapp.views
# The Flask Views

import os
import re
from flask import request, redirect, render_template, jsonify, send_from_directory
from sqlalchemy.orm import joinedload, load_only
from webapp import app, db
from webapp.util import *
from webapp.models import *


## Route /
# displays the main content
@app.route("/")
def index():
    #print( request.args.getlist('tag'))
    records = db.session.query(Data)
    records = records.options(joinedload(Data.tags))

    for tag in request.args.getlist('tag'):
          records = records.filter( Data.tags.any(Tag.name == tag) )
    records = records.limit(50)
    possible_tags = get_tagList_by_tags( request.args.getlist('tag') )
    current_data = get_data(request.args.getlist('tag'))
    #print(possible_tags)
    return render_template('index.html', records = records, tags = request.args.getlist('tag'), possible_tags = possible_tags, current_data=current_data )

## Route /save
# saves the posted Data and redirects
@app.route("/save")
def save():
    tags = [x for x in request.args.getlist('tag') if x]
    dataEntry = get_data( tags )
    if not dataEntry:   #already exists?
        entry = Data( tags=get_tagList(tags), value = request.args.get('value'))
        db.session.add(entry)
        db.session.commit()
    else:
        Data.query.get(dataEntry.id).value = request.args.get('value')
        db.session.commit()
    url = "/?"
    for tag in tags:
        url = url + "tag=" + tag + "&"
    return redirect( url )

## Route /delete
# delete a record and redirect
@app.route("/delete")
def delete():
    return ""

## Route /api/0.1/get_tags
# return a json with possible Tags
@app.route("/api/0.1/get_tags")
def get_tags():
    if len(request.args.getlist('tags')) > 0:
        output = get_tagList_from_tags_by_search( request.args.getlist('tags'), request.args.get('tag') )
    else:
        output = get_tagList_by_search( request.args.get('tag') )
    #print( output  )
    return jsonify(tags=output)


## Route /doc
# shows the documentation, if available
@app.route('/doc/<path:path>')
def show_doc(path):
    return send_from_directory('../docs/html/', path)

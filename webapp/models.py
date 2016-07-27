from flask import abort
from flask_sqlalchemy import SQLAlchemy

from webapp import db
#db = SQLAlchemy()

TagRelation = db.Table('TagRelation', db.metadata,
    db.Column('data_id', db.Integer, db.ForeignKey('data.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

## Stores all Tag Names
class Tag(db.Model):
    __tablename__ = "tag"
    ## The primary Key
    id = db.Column(db.Integer, primary_key=True)
    ## The displayed Name
    name = db.Column(db.String(32), unique=True)
    #tags = db.relationship(Data, secondary=TagRelation,  backref="tags")

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name


## Stores all (Meta) Data
class Data(db.Model):
    __tablename__ = "data"
    ## The primary Key
    id = db.Column(db.Integer, primary_key=True)
    ##relationship to Tags
    tags = db.relationship(Tag, secondary=TagRelation, backref=db.backref('dates'))
    ## The Value of the Data
    value = db.Column(db.String)
    ## Just a free Comment
    comment = db.Column(db.String)
    ## A Hyperlink to the Source of the Vlaue
    source = db.Column(db.String)
    ## last edit date
    lastchange = db.Column(db.Date)
    db.UniqueConstraint('tags', 'value')

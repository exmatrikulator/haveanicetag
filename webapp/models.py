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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name


## Stores all User Accounts / logins
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship("Tag", secondary=TagRelation,  backref=db.backref('datas', lazy='dynamic'))
    value = db.Column(db.String)
    db.UniqueConstraint('tags', 'value')

## @package webapp.util
# Some helper Functions

import re
from sqlalchemy.orm import joinedload
from webapp.models import *
from webapp import db

## escape String for use SQL
# @param text a string, which should be escaped
# @return a string, which is SQL safe
def escape_sql(text):
    return re.sub('[^A-z0-9 ]+','',text)

## get a tag object
# @param tag the displayed name of a Tag
# @return the sqlalchemy object of a Tag
def get_tag_object(tag):
    return db.session.query(Tag).filter_by(name=tag).first()

## get a list of matching tags
# @param tag a search string
# @return a list of sqlalchemy objects of Tags
def get_tagList_like(tag):
    return db.session.query(Tag.id).filter(Tag.name.contains(tag)).all()

## get a sqlalchemy list of tags
# gets the object of existing Tags or create new object for non existing Tags
# @param tags a list of the displayed name of Tags
# @return a sqlalchemy list of Tags
def get_tagList(tags):
    result = []
    # tags = tags.lower()
    # tags = tags.replace(";",",").replace("/",",")
    # tags = tags.split(",")
    # tags = set(tags)        # no duplicates!

    for tag in tags:
        tag = tag.strip()
        if tag:
            tagobj = db.session.query(Tag).filter_by(name=tag).first()
            if tagobj is None:
                tagobj = Tag(name=tag)
            result.append(tagobj)
    return list(set(result)) #delete duplicate

## get a list of matching Tags
# if you haven't selected any Tag, you will get a list of mactching Tags
# @param search a (sub)string of a Tag
# @return a list of possible Tags
def get_tagList_by_search(search):
    entries = db.engine.execute( "SELECT name FROM tag WHERE name like '%" + escape_sql(search) + "%' ORDER BY name" )
    return [str(i.name) for i in entries]

## get a list of possible Tags
# if you have already have selected Tags, you will get a list of all possible other
# @param tags a list of Tags
# @return a list of possible Tags
def get_tagList_by_tags(tags):
    if len(tags) <1:
        return get_tagList_by_search("")
    sql1 = "name LIKE '" + escape_sql(tags[0]) + "'"
    sql2 = "tag.name NOT LIKE '" + escape_sql(tags[0]) + "'"
    tags_count = 0
    for tag in tags:
        tags_count += 1
        if tags_count > 1:
            sql1 += "OR name LIKE '" + escape_sql(tag) + "' "
            sql2 += "AND tag.name NOT LIKE '" + escape_sql(tag) + "' "
    sql = "SELECT distinct(tag.name) FROM \
    (SELECT TagRelation.data_id FROM tag\
        JOIN TagRelation ON tag.id=TagRelation.tag_id \
        WHERE " + sql1 + " \
        GROUP BY TagRelation.data_id HAVING count(tag.id)=" + str(tags_count) + ") a\
    JOIN TagRelation ON a.data_id=TagRelation.data_id \
    JOIN tag ON tag.id=TagRelation.tag_id\
    WHERE " + sql2 + ";"
    sql = re.sub('\s+',' ',sql)
    #print(sql)
    entries = db.engine.execute( sql )
    return [str(i.name) for i in entries]

## get a list a of matching Tags
# if you have already selected Tags and want to search in the remaining possible Tags
# @param tags a list of selected tags
# @param search a search string over the remaining Tags
# @return a list of matching Tags
def get_tagList_from_tags_by_search(tags,search):
    if len(tags) <1:
        return False
    possible_tags = get_tagList_by_tags(tags)
    #print(possible_tags)
    output = [tag for tag in possible_tags if search in tag]
    #print(output)
    return output

##
# Is there already an entry with those Tags?
# @param tags a list of Tags
# @return True  if there is an entry
# @return False if there isn't an entry yet
def exist(tags):
    tags = [x for x in tags if x]
    if len(tags) <1:
        return True

    records = db.session.query(Data)
    records = records.options(joinedload(Data.tags))
    for tag in tags:
          records = records.filter( Data.tags.any(Tag.name == tag) )
    records = records.first()
    #print(records)

    if records:
        return True
    else:
        return False

## get a Data record
# select a Data record with those Tags
# @param tags a list of tags
# @return the Data record
def get_data(tags):
    tags = [x for x in tags if x]
    if len(tags) <1:
        return ""

    records = db.session.query(Data)
    records = records.options(joinedload(Data.tags))
    for tag in tags:
          records = records.filter( Data.tags.any(Tag.name == tag) )
    records = records.first()
    #print(records)

    if records:
        return records
    else:
        return ""

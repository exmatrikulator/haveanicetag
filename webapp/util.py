from webapp.models import Tag
from webapp import db


def get_tag_list(tags):
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

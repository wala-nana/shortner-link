from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import link_model
import pyshorteners


def show_all(db : Session):
    all_links= db.query(link_model.Link).all()
    return all_links


def encode_link(link, db : Session):

    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(link.link_url)

    new_link = link_model.Link(
        link_name = link.link_name,
        link_url = link.link_url,
        link_shortcut = short_url
        )

    db.add(new_link)
    db.commit()

    return {"The Shortened URL is: " : short_url}


def get_long_link(short_link, db : Session):

    try:

        # By decode the url:
        type_tiny = pyshorteners.Shortener()
        original_url = type_tiny.tinyurl.expand(short_link.link_url)
        # print(original_url,"original_url original_url")
        return {"The original url is: ": original_url}

        # By get from Database:
        # original_url = db.query(link_model.Link).filter(link_model.Link.link_shortcut==short_link.link_url).first()
        # if not original_url:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Item with url {short_link} is not Available")
        # return {"The original url is: ": original_url.link_url}
    except:
        return {"ERROR MESSAGE: ":"Please enter right url."}

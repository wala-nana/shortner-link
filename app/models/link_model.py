from ..database import Base
from sqlalchemy import Column, Integer,String


class Link(Base):
    __tablename__ = "link"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    link_name = Column(String, index=True)
    link_url = Column(String, index=True)
    link_shortcut = Column(String, index=True)

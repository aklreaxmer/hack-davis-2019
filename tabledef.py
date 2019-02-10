from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from passlib.hash import bcrypt
from sqlalchemy.orm import sessionmaker
import datetime
engine = create_engine('sqlite:///researchportal.db', echo=True)
Base = declarative_base()

#This file defines our database structure

def get_date():
    return datetime.datetime.now()

class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    professor = Column(Boolean)

    def __init__(self, username, password, professor):
        """"""

        self.username = username
        self.password = bcrypt.encrypt(password)
        self.professor = professor

            # create tables
        Base.metadata.create_all(engine)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

class Lab(Base):
    """"""
    __tablename__ = "labs"

    id = Column(Integer, primary_key=True)
    PI = Column(String)
    link = Column(String)
    desc = Column(String)
    category = Column(String)


    def __init__(self, PI, link, desc, category):
        """"""
        self.PI = PI
        self.link = link
        self.desc = desc
        self.category = category
        # create tables
        Base.metadata.create_all(engine)

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    text = Column(String)
    date = Column(Date, default=get_date)
    lab_id =  Column('lab_id',Integer,
        ForeignKey("labs.id"), nullable=False)
    def __init__(self, text, name, date, lab_id):
        """"""
        self.text = text
        self.name = name
        self.date = date
        self.lab_id = lab_id
            # create tables
        Base.metadata.create_all(engine)

class Posting(Base):
    __tablename__ = "postings"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    text = Column(String)
    date = Column(Date, default=get_date)
    lab_id =  Column('lab_id',Integer,
        ForeignKey("labs.id"), nullable=False)
    def __init__(self, text, name, date, lab_id):
        """"""
        self.text = text
        self.name = name
        self.date = date
        self.lab_id = lab_id
            # create tables
        Base.metadata.create_all(engine)

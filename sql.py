import os
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, String, BigInteger, DateTime, BINARY, func
import sys

# sys.path.append(r"C:\LABS\PP\lab_6\PP_lab")

engine = create_engine("mysql+pymysql://root:45627349350923@127.0.0.1/lab-7")

engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()
BaseModel.query = Session.query_property()


# db = SQLAlchemy(app)
#

class user(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(50))
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(45))
    phone = Column(VARCHAR(20))
    user_status = Column(Integer)

    # def __str__(self):
    #     return f"User ID : {self.id}\n" \
    #            f"First name : {self.first_name}" \
    #            f"Last name : {self.last_name}" \
    #            f"Username : {self.username}\n" \
    #            f"Email : {self.email}\n" \
    #            f"Phone : {self.phone}\n"

    def __init__(self, first_name):
        self.first_name = first_name

    # def __repr__(self):
    #     return "<User(name={self.first_name!r})>".format(self=self)


class note(BaseModel):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.id))
    name = Column(VARCHAR(255))


class connected_user(BaseModel):
    __tablename__ = "connected_user"
    user_id = Column(Integer, ForeignKey(user.id), primary_key=True)
    note_id = Column(Integer, ForeignKey(note.id), primary_key=True)


class action(BaseModel):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))


class note_log(BaseModel):
    __tablename__ = "note_log"
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey(note.id))
    user_id = Column(Integer, ForeignKey(user.id))
    action_id = Column(Integer, ForeignKey(action.id))

print(user.query.all())
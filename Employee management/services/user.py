import sqlalchemy
from services.relation import user
from flask import *
from models.model import *
from database import *
import json


class User_services:
    def get_all_users():
        return [User.json(users) for users in User.query.all()]

    def add_user(_username, _email, _desid):
        new_user = User(username=_username, email=_email, desid=_desid)
        db.session.add(new_user)
        db.session.commit()

    def get_user(_id):
        '''function to get user using the id of the movie as parameter'''
        return [User.json(User.query.filter_by(id=_id).first())]

    def update_user(_id, _username, _email, _desid):
        '''function to update the details of a user using the id, title,
        year and genre as parameters'''
        u = (User.query.filter_by(id=_id).first())
        u.username = _username
        u.email = _email
        u.desid =_desid
        db.session.commit()
    def delete_user(_id):
        '''function to delete a user from our database using the id of the user as a parameter'''
        ud = User.query.filter_by(id=_id).first()
        print(ud)
        db.session.delete(ud)
        db.session.commit()

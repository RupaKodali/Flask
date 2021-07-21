from models.model import *

def user(_username):
    u=(User.query.filter_by(username=_username).first())
    res= Designation.query.filter_by(id = u.desid).first()
    return Designation.json(res)
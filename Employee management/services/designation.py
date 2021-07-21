from flask import *
from models.model import *
from database import *
import json

class Designation_services:
    def add_designation(_job):
        new_designation=Designation(job=_job)
        db.session.add(new_designation)
        db.session.commit()
    def get_all_designations():
        return [Designation.json(users) for users in Designation.query.all()]
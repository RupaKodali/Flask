from flask_json_schema import *
from database import *
from models.model import *
db = SQLAlchemy(app)
schema = JsonSchema(app)
todo_schema = {
    'properties': {
        'id': { 'type': 'number' },
        'username': { 'type': 'string' },
        'email':{'type': 'string'},
        'desid':{'type':'number'}
    }
}
todo_schema1 ={
    'properties':{
        'id':{'type':'number'},
        'job':{'type':'string'}
    }
}

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    desid =db.Column(db.Integer, db.ForeignKey('designation.id'),nullable=False)
    def json(self):
        return {'id': self.id, 'username': self.username,
                'email': self.email, 'desid': self.desid}
class Designation(db.Model):
    __tablename__ = 'designation'
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(80),nullable=False)
    userid =   db.relationship('User', backref='designation', lazy=True)
    def json(self):
        return {'id': self.id, 'job':self.job}


db.create_all()
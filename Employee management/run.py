from flask import *
app = Flask(__name__)
from routes.user import *
from routes.designation import *
from routes.relation import *

if __name__ == '__main__':
    app.run(host='localhost', port=3000,debug=True)
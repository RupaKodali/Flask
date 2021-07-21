from services.designation import *
from models.model import *

@app.before_request
def before_request():
    app.logger.info("before_request")

@app.after_request
def after_request(response):
    app.logger.info("after_Request")
    return response
 

@app.route('/designation', methods=['GET'])
@schema.validate(todo_schema1)
def get_designation():
    app.logger.info("request_processing")
    return jsonify({'Users': Designation_services.get_all_designations()})

@app.route('/designation', methods=['POST'])
@schema.validate(todo_schema1)
def add_designation():
    app.logger.info("request_processing")
    request_data = request.get_json()  # getting data from client
    Designation_services.add_designation(request_data["job"])
    response = Response("Designation added", 201, mimetype='application/json')
    return response

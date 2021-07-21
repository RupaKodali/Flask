from services.user import *
from models.model import *

@app.before_request
def before_request():
    app.logger.info("before_request")

@app.after_request
def after_request(response):
    app.logger.info("after_Request")
    return response
 

@app.route('/users', methods=['GET'])
def get():
    return jsonify({'Users': User_services.get_all_users()})

@app.route('/getusers', methods=['GET'])
@schema.validate(todo_schema)
def get_user_by_id():
    request_data = request.get_json()
    return_value = User_services.get_user(request_data["id"])
    return jsonify(return_value)

@app.route('/users', methods=['POST'])
@schema.validate(todo_schema)
def add():
    request_data = request.get_json()  # getting data from client
    User_services.add_user(request_data["username"],request_data["email"],request_data["desid"])
    response = Response("User added", 201, mimetype='application/json')
    return response

@app.route('/users',methods=['PUT'])
@schema.validate(todo_schema)
def update():
    request_data=request.get_json()
    User_services.update_user(request_data["id"], request_data["username"],request_data["email"],request_data["desid"])
    response = Response("User Updated", status=200, mimetype='application/json')
    return response
@app.route('/users',methods=['DELETE'])
@schema.validate(todo_schema)
def delete():
    request_data=request.get_json()
    User_services.delete_user({request_data["id"]})
    response = Response("User deleted", status=200, mimetype='application/json')
    return response

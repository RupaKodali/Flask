from services.relation import *
@app.route('/getu', methods=['GET'])
def get_user_by_username():
    request_data = request.get_json()
    return_value = user(request_data["username"])
    return jsonify(return_value)

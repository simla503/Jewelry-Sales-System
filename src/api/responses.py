from flask import jsonify

def success_response(data=None, message="Success"):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    })

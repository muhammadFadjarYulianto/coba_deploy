from flask import jsonify, make_response

def success(values):
    res = {
        'status': 'success',
        'data': values,
    }
    return make_response(jsonify(res)), 200  

def created(values, message):
    res = {
        'status': 'success',
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 201  

def noContent():
    res = {
        'status': 'success',
        'data': None,
        'message': None
    }
    return make_response(jsonify(res)), 204  

def badRequest(values, message):
    res = {
        'status': 'fail',
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 400  

def unauthorized(values, message):
    res = {
        'status': 'fail',
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 401 

def forbidden(values, message):
    res = {
        'status': 'fail',
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 403  

def notFound(values, message):
    res = {
        'status': 'fail',
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 404  

def unprocessableEntity(values, message):
    res = {
        'status': 'fail',
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 422 

def serverError(values, message):
    res = {
        'status': 'error',
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 500  

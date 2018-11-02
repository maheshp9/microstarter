# services/apiservice/core/api/entity.py

from flask import Blueprint, jsonify, request

entity_blueprint = Blueprint('entity', __name__)

@entity_blueprint.route('/api/entities/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'PING Response!'
    })

@entity_blueprint.route('/api/entities', methods=['POST'])
def add_entity(resp):
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    try:
        if not post_data:
            return jsonify(response_object), 400
        response_object['status'] = 'success'
        response_object['message'] = 'entity created!'
        return jsonify(response_object), 201
    except Exception:
        return jsonify(response_object), 400

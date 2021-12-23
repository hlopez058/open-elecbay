"""The Endpoints to manage the MARKET_REQUESTS"""
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint
from flask import Flask, render_template
from flask import redirect, url_for
from flask_mqtt import Mqtt
import json

REQUEST_API = Blueprint('request_api', __name__)
mqtt = None


# Example market requests
# Should be managed as a queue by a brokerage thread
##
MARKET_REQUESTS = {}
#    "8c36e86c-13b9-4102-a44f-646015dfd981": {
#        'type': 'INFO',
#        'message': u'Test request',
#        'timestamp': (datetime.today() - timedelta(1)).timestamp()
#    }
# }


def send_mqtt(topic, msg):
    mqtt.publish(topic, json.dumps(msg))


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route("/", methods=['GET'])
def hello():
    username = request.args.get('name')
    return render_template('index.html', name=username)


@REQUEST_API.route('/request', methods=['GET'])
def get_records():
    """Return all market requests
    @return: 200: an array of all known MARKET_REQUESTS as a \
    flask/response object with application/json mimetype.
    """
    return jsonify(MARKET_REQUESTS)


@REQUEST_API.route('/request/<string:_id>', methods=['GET'])
def get_record_by_id(_id):
    """Get request details by it's id
    @param _id: the id
    @return: 200: a MARKET_REQUESTS as a flask/response object \
    with application/json mimetype.
    @raise 404: if  request not found
    """
    if _id not in MARKET_REQUESTS:
        abort(404)
    return jsonify(MARKET_REQUESTS[_id])


@REQUEST_API.route('/submit/<string:_id>', methods=['POST'])
def submit_record_by_id(_id):
    """Submit request by it's id
    @param _id: the id
    @return: 200: a MARKET_REQUESTS as a flask/response object \
    with application/json mimetype.
    @raise 404: if  request not found
    """
    if _id not in MARKET_REQUESTS:
        abort(404)
        return jsonify(MARKET_REQUESTS[_id])
    else:
        record = MARKET_REQUESTS[_id]
        send_mqtt(record['type'], record)
        # clear all market requests
        del MARKET_REQUESTS[_id]
        return record


@REQUEST_API.route('/request', methods=['POST'])
def create_record():
    """Create a market request record
    @param type: post : the request type , BID,OFFER,INFO
    @param message: post : the details of the request
    @return: 201: a new_uuid as a flask/response object \
    with application/json mimetype.
    @raise 400: misunderstood request
    """
    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)
    if not data.get('type'):
        abort(400)
    if not data.get('message'):
        abort(400)
    new_uuid = str(uuid.uuid4())
    market_request = {
        'type': data['type'],
        'message': data['message'],
        'timestamp': datetime.now().timestamp()
    }
    MARKET_REQUESTS[new_uuid] = market_request
    # HTTP 201 Created
    return jsonify({"id": new_uuid}), 201


@REQUEST_API.route('/request/<string:_id>', methods=['PUT'])
def edit_record(_id):
    """Edit a request record
    @param type: post : the request type , BID,OFFER,INFO
    @param message: post : the details of the request
    @return: 200: a request as a flask/response object \
    with application/json mimetype.
    @raise 400: misunderstood request
    """
    if _id not in MARKET_REQUESTS:
        abort(404)
    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)
    if not data.get('type'):
        abort(400)
    if not data.get('message'):
        abort(400)
    market_request = {
        'type': data['type'],
        'message': data['message'],
        'timestamp': datetime.now().timestamp()
    }
    MARKET_REQUESTS[_id] = market_request
    return jsonify(MARKET_REQUESTS[_id]), 200


@REQUEST_API.route('/request/<string:_id>', methods=['DELETE'])
def delete_record(_id):
    """Delete a market request record
    @param id: the id
    @return: 204: an empty payload.
    @raise 404: if request not found
    """
    if _id not in MARKET_REQUESTS:
        abort(404)
    del MARKET_REQUESTS[_id]
    return '', 204

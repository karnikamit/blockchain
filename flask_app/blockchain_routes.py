#! *-* coding: UTF-8 *-*
__author__ = "karnikamit"
from flask_app import app, blockchain, logger
from flask_app.block import Block
from flask import jsonify, request
import json
index = 0


def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, Block):
        return obj.__dict__


@app.route('/chain', methods=['GET'])
def chain():
    return json.dumps(blockchain.chain, default=serialize)


@app.route('/mine', methods=['POST'])
def mine():
    global index
    request_body = request.get_json()
    logger.debug("request_body: %s", request_body)
    index += 1
    block = Block(index, request_body)
    blockchain.add_block(block)
    return jsonify({"response": "success"})


if __name__ == '__main__':
    logger.debug("Running on 127.0.0.1, PORT 9900")
    app.run(host='127.0.0.1', port=9900, debug=True)

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
from flask import Flask, request, abort, render_template, redirect, url_for
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import (
        InvalidSignatureException, 
        InvalidAppIdException,
)

import utils
import json

config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config", "config.json")
with open(config_path) as config_file:
    json_config = json.load(config_file)

config = json_config["wechat_server"]

HOST = config["HOST"]
PORT = config["PORT"]

app = Flask(__name__)

def check_wrap(request):
    try:
        utils.check_signature(request)
    except InvalidSignatureException:
        abort(403)

@app.route('/wechat', methods=['GET'])
def wechat_get():
    check_wrap(request)
    echo_str = request.args.get('echostr', '')
    return echo_str

@app.route('/wechat', methods=['POST'])
def wechat_post():
    check_wrap(request)

    msg = parse_message(request.data)
    print msg.source
    print msg.target
    if msg.type == 'event':
        return utils.event_handler(msg)

    if msg.type == 'text':
        return utils.text_handler(msg)

    reply = create_reply('Sorry, cannot handle this for now', msg)

    return reply.render()

if __name__ == '__main__':
    app.run(HOST, PORT, debug=True)


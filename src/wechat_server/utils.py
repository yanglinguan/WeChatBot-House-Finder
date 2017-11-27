from wechatpy.utils import check_signature
from wechatpy import create_reply
from config import config
from wechatpy.exceptions import (
        InvalidSignatureException, 
        InvalidAppIdException,
)

TOKEN = config['TOKEN']
AES_KEY = config['AESKEY']
APPID = config['APPID']

def check_signature(request):
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    encrypt_type = request.args.get('encrypt_type', 'raw')
    msg_signature = request.args.get('msg_signature', '')
    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)

def event_handler(msg):
    if msg.event == 'subscribe':
        reply = create_reply('Welcome to CozyPlaces, Click http://www.google.com to submit your request', msg)
        return reply.render()
    return ''
    
def text_handler(msg):
    reply = create_reply(msg.content, msg)
    return reply.render()




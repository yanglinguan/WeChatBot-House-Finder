from wechatpy import WeChatClient
from config import config

APPID = config["APPID"]
SECRET = config["SECRET"]

client = WeChatClient(APPID, SECRET)
client.menu.create({
    "button":[
        {
            "type": "view",
            "name": "submit request",
            "url": "http://www.google.com/"
        }
    ]
})

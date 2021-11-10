from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from config import line_config
from coupons import get_coupons_result

app = Flask(__name__)

# LINE 聊天機器人的基本資料

line_bot_api = LineBotApi(line_config.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(line_config.CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return 'OK'


# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    text = event.message.text
    result = get_coupons_result(text)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=result))


@app.route("/test", methods=['GET'])
def test():
    return {"status":200}

if __name__ == "__main__":
    app.run()
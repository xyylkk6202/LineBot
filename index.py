from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('pvdnxLXOCqG9kV14KT10JeHe+aDUe+HNacCWbbNbVr/cPJHdbxsDVsDeAFZNl9bKB2wqpqnZZeVEWCwZ2K8IKnerrmwA+v1OR5LZTF1AgGh41jxuj6fyx25M8lsqG/UhwKA7trbH5FNUQ6tWhQ9vfQdB04t89/1O/w1cDnyilFU=')
handler1 = WebhookHandler('e0761cc5c843292fdc4edef2df344ab7')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

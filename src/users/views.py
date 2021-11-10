from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from utils.coupons import get_coupons_result

from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from users.models import User
from datetime import datetime
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# Create your views here.

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        now = datetime.now()
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            profile = line_bot_api.get_profile(event.source.user_id)
            
            
            
            user_qs = User.objects.filter(line_user_id=event.source.user_id)
            if user_qs.exists():
                user_obj = user_qs.first()
                user_obj.last_login_time = now()
                user_obj.save()
            User.objects.create(
                {
                    "line_user_id" : event.source.user_id,
                    "display_name" : profile.display_name,
                    "picture_url" : profile.picture_url,
                    "status_message" : profile.status_message,
                    "last_login_time" : now,
                }
            )
                
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                input_text = event.message.text
                try:
                    if len(input_text) != 3:
                        raise ValueError
                    int(input_text)
                    result = get_coupons_result(input_text)
                except:
                    result = "請輸入身分證後三位數字"
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=result))
        return HttpResponse()
    else:
        return HttpResponse()


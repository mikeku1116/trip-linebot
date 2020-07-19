from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Location

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件

                # 篩選location資料表中，地區欄位為使用者發送地區的景點資料
                locations = Location.objects.filter(area=event.message.text)

                content = ''  # 回覆使用者的內容
                for location in locations:
                    content += location.name + '\n' + location.address + '\n\n'

                line_bot_api.reply_message(  # 回覆訊息
                    event.reply_token,
                    TextSendMessage(text=content)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

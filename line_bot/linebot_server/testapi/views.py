from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (MessageEvent,
                            TextSendMessage, TextMessage, AudioSendMessage, LocationSendMessage, TemplateSendMessage, VideoSendMessage,
                            ButtonsTemplate,
                            PostbackAction, MessageAction, URIAction)

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '文字':
                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(text="文字測試"))
                    elif mtext == '聲音':
                        message = AudioSendMessage(
                            original_content_url='https://57b33a613b19.ngrok.io/static/linebot_server/hello.m4a', duration=2000)
                        line_bot_api.reply_message(event.reply_token, message)
                    elif mtext == '影片':
                        message = VideoSendMessage(
                            original_content_url='https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_480_1_5MG.mp4',
                            preview_image_url='https://57b33a613b19.ngrok.io/static/linebot_server/video.png')
                        line_bot_api.reply_message(event.reply_token, message)
                    elif mtext == '地圖':
                        message = LocationSendMessage(
                            '公司', '市政路386號', '24.159162090886316', '120.64025491140256', True)
                        line_bot_api.reply_message(
                            event.reply_token, message)
                    elif mtext == '預約':
                        message = TemplateSendMessage(
                            alt_text='是否要預約一日男友?',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://avatars3.githubusercontent.com/u/29451488?s=400&v=4',
                                title='是否要預約一日男友?',
                                text='RayJi',
                                actions=[
                                    PostbackAction(
                                        label='立即預約',
                                        display_text='我要預約',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageAction(
                                        label='傳送訊息',
                                        text='傳送訊息'
                                    ),
                                    URIAction(
                                        label='前往首頁',
                                        uri='https://github.com/RayJi0428/learning/tree/main/line_bot'
                                    )
                                ]
                            )
                        )
                        line_bot_api.reply_message(
                            event.reply_token, message)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

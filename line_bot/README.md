# learning
學習分享


# 大綱
## 用途
## 運作流程
![示意圖](https://swf.com.tw/images/books/IoT/Line/line_bot_messaging_api.png)

# 申請服務
## 登入官網建立Provider
https://developers.line.biz/zh-hant/
![](/line_bot/images/provider_0.png)
![](/line_bot/images/provider_1.png)
![](/line_bot/images/provider_2.png)
## 加入好友
申請完Channel後就可以用QRCode加入好友
![](/line_bot/images/provider_3.png)
## 自動回應訊息設定
點選下方的Edit可以試試修改基本回應訊息
![](/line_bot/images/provider_4.png)
![](/line_bot/images/provider_5.png)
![](/line_bot/images/provider_6.png)
![](/line_bot/images/provider_7.png)

# 建立自己的回應伺服器
## 安裝套件
```bat
pip install line-bot-sdk==1.8.0
pip install django
```

## 建立django專案
在目標資料夾輸入命令
```bat
django-admin startproject linebot_server
```
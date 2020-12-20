# 大綱
##### 運作流程
![示意圖](https://developers.line.biz/assets/img/messaging-api-architecture.f40bffbb.png)

# 申請服務
##### 登入官網建立Provider
https://developers.line.biz/zh-hant/

![](https://i.imgur.com/Saa3yp9.png)

![](https://i.imgur.com/eKQeMbs.png)

![](https://i.imgur.com/Rv9533C.png)

##### 在Basic settings頁面紀錄Channel secret(之後要用)

![](https://i.imgur.com/RWDloEe.png)

##### 在Messaging API頁面生成Channel access token(之後要用)

![](https://i.imgur.com/Os3aU1y.png)

##### 加入好友
申請完Channel後就可以用QRCode加入好友

![](https://i.imgur.com/WNHsweg.png)

##### 自動回應訊息設定
點選下方的Edit可以試試修改基本回應訊息

![](https://i.imgur.com/l6AWjgS.png)
![](https://i.imgur.com/sMnf0dT.png)
![](https://i.imgur.com/V1ifWcq.png)
![](https://i.imgur.com/ASgFESK.png)

# 建立django專案
##### 安裝套件
[line-bot-sdk](https://github.com/line/line-bot-sdk-python)
```bat
pip install line-bot-sdk==1.8.0
pip install django
```
在目標資料夾輸入命令
```bat
django-admin startproject linebot_server
```
##### 建立APP
注意要在和manage.py同層目錄執行
```python
python manage.py startapp testapi
```
##### 建立相關目錄
- templates(html模板)
- static(django使用圖片,CSS,javascript..都在此目錄)

##### 啟動server
```python
python manage.py runserver
```
啟動成功驗證是否正常 http://127.0.0.1:8000/

![](https://i.imgur.com/yJHl14h.png)

##### ngrok轉址
因為line只接受https，可以簡單使用ngrok.exe生成https網址
```bash
ngrok http 8000
```

![](https://i.imgur.com/1ZD1s6d.png)

記得回到line網站設定Webhook URL、開啟Use webhook

![](https://i.imgur.com/hgZ28pL.png)

##### 環境設定
##### **`settings.py`**
###### 設定Channel access token, Channel secret
```python
LINE_CHANNEL_ACCESS_TOKEN = '使用者 Channel access token'
LINE_CHANNEL_SECRET = 'Channel secret'
```
###### ALLOWED_HOSTS 開放所有外部連結權限
```python
ALLOWED_HOSTS = ['*']
```
###### INSTALLED_APPS 新增自訂APP
```python
INSTALLED_APPS = [
    ...
    'testapi', #新增的APP
]
```
###### 指定templates目錄
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR), 'templates'], #templates路徑
        ...
    },
]
```
###### 調整語系、時區
```python
LANGUAGE_CODE = 'zh-Hant' #繁體中文
TIME_ZONE = 'Asia/Taipei' #台北時區
```
###### 新增static目錄
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), #加入static路徑
]
```
##### 設定django網址、函式參照
##### **`urls.py`**
```python
from django.conf.urls import url
from testapi import views
urlpatterns = [
    url('^callback', views.callback), #設定callback對應
    path('admin/', admin.site.urls),
]
```
##### **`views.py`**
撰寫views.py處理回應訊息邏輯

##### 更多訊息種類請參考官方文件
https://github.com/line/line-bot-sdk-python

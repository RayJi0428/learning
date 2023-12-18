# 開發者與WebGL
### RD->引擎->WebGL->OpenGL->GPU->顯示器

# 何謂 WebGL?
#### WebGL (Web Graphics Library)
基於OpenGL ES 2.0的JavaScript操作OpenGL的API

# 何謂 OpenGL?
#### OpenGL (Open Graphics Library)
#### OpenGL ES(OpenGL for Embedded Systems)(針對行動裝置較輕量的OpenGL特殊版)
操作硬體資源的API

# OpenGL上下文(Context)
程式調用OpenGL指令前，要先建立OpenGL Context，是非常龐大的狀態機，保存OpenGL各種狀態。

## 
# CPU vs GPU
#### 依照不同任務需求，交給CPU或GPU處理
#### CPU (Central Processing Unit) 中央處理器
電腦的心臟(射速快的機關槍)

適合處理邏輯

![Imgur](https://i.imgur.com/Y7rPVxM.gif)

#### GPU (Graphics Processing Unit) 圖形處理器
顯示卡的心臟(射速慢，但彈丸數量相當多的霰彈槍)

適合處理計算(Shader盡量不寫if...else因為很慢)

![Imgur](https://i.imgur.com/4a8mwAv.png)

[gif](https://i.imgur.com/HV4TpeX.gif)
# 網頁與WebGL
透過canvas取得OpenGL上下文(Context)

![Imgur](https://i.imgur.com/pvV09Pp.jpg)

# WebGL Context Lost 可能原因？
- 多個頁面使用GPU，GPU超載，瀏覽器將文本回收，再挑其中一個恢復。

- 瀏覽器某頁面對GPU操作時間過長，導致瀏覽器決定重置GPU打破停頓。

- 電腦有多種GPU，切換時也會丟失。 

# WebGL運作
### 沒有WebGL

![](./before.png)

### WebGL協定

![](./after.png)

### webGL2
- 100%向下相容、原本選配變成標配
- webgl(openGL ES2), webgl2(openGL ES3)shader寫法調整
- 如果遊戲引擎只處理webgl2寫法,那也改不回webgl

# 參考文獻
https://zhuanlan.zhihu.com/p/56693625

https://zhuanlan.zhihu.com/p/337561969

https://ithelp.ithome.com.tw/articles/10217819

https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/isContextLost

https://pcgoto.com/gpu-more-important-or-ram/
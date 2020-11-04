# 智慧無人機偵測小花蔓澤蘭技術
專題介紹影片:https://youtu.be/52EtV_MRUfw
Google雲端:https://drive.google.com/drive/u/0/folders/1wh_Kx8QquIs2Vhor61Hc0R7KPG5nhf3-

宣傳海報
---
![image](https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/poster.jpg)

壹、小花蔓澤蘭蔓延程度
---
- 使用的四個工具
  - Google Earth pro
  - Google Map API
  - Python(folium套件)
  - ArcGIS
- 如何操作
  - Google Earth pro
    - 開啟"小花蔓澤蘭蔓延圖.kmz"(github上無法放超過100M的檔案，所以這裡直接展示)
    https://www.youtube.com/watch?v=xVk2QwG2l6g
  - Google Map API
    - 請下載文件"Mikania_micrantha"裡面有地圖上所使用到的照片及程式檔"Mikania.html"
    ![image](https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/GoogleMapApi.gif)
  - Python(folium套件)
    - ![image](https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/folium.gif)
  - ArcGIS
    - 到瀏覽器輸入連結"https://arcg.is/1bCvXC"
    ![image](https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/ArcGis.gif)
    
貳、模型訓練
---
資料數量
小花蔓澤蘭:539
非小花蔓澤蘭:174
- 模型訓練
  - 三層CNN<br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/3CNN.jpg" width="400"/><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/3CNN1.jpg" width="700"/><br/>
  - MobileNet<br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/mobileNet.jpg" width="400"/><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/mobileNet1.jpg" width="700"/><br/>
  - AlexNet<br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/AlexNet.jpg" width="400"/><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/AlexNet1.jpg" width="700"/><br/>
  - RestNet<br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/RestNet18.jpg" width="400"/><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/RestNet18-1.jpg" width="700"/><br/>
- 模型優化
  - 三層CNN<br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/optimal_3CNN.jpg" width="400"/><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/optimal_3CNN1.jpg" width="700"/><br/>
  - MobileNet<br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/optimal_mobileNet.jpg" width="400"/><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/optimal_mobileNet1.jpg" width="700"/><br/>
  - AlexNet<br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/optimal_alex.jpg" width="400"/><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/model_demo/optimal_alex1.jpg" width="700"/><br/>
叄、無人機飛行及錄影
---
- 開發工具
  - Ubuntu18.04LTS
  - Python 3.7
  - PyCharm 2020.2.2
- 無人機飛行跟錄影
  開啟並執行Tello-Python/fly.py
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/tello_fly_and_video.jpg" width="400"/><br/>
  檔案會存在Tello-Python內
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/fly_and_video_save_file.jpg" width="400"><br/>
- 無人機飛行及紀錄影像轉csv檔
  開啟並執行TelloPy/tellopy/record_log.py
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/recode_video.jpg" width="400"><br/>
- 影像邊緣化
  開啟並執行TelloPy/tellopy/video_effect.py
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/tello_image_canny.png"  width="400"><br/>
- 室外執行影片
  https://www.youtube.com/watch?v=hhgbvYMlVEU

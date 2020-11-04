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
  開啟並執行fly_and_record/Tello-Python/fly_and_video.py
  
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/tello_fly_and_video.jpg" width="700"/><br/>
  
  檔案會存在Tello-Python內
  
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/fly_and_video_save_file.jpg" width="700"><br/>
  
- 無人機飛行及紀錄影像轉csv檔
  開啟並執行fly_and_record/TelloPy/tellopy/record_log.py
  
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/recode_video.jpg" width="700"><br/>
  
- 影像邊緣化<br/>
  開啟並執行fly_and_record/TelloPy/tellopy/video_effect.py
  
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/tello_image_canny.png"  width="700"><br/>
  
- 室外執行影片
  https://www.youtube.com/watch?v=hhgbvYMlVEU
 
 肆、ROS_ORBSLAM
 ---
 - 開發環境
    - Ubuntu 18.04LTS
 - 安裝相關依賴:[安裝教學](https://hackmd.io/OzbbO-ihSG6ODoc_QImOlg)
 
 <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/SLAM.png"  width="700"><br/>
伍、YOLO
---
  - 開發環境
    -Windows10
  - 照片標記
  
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/yolo_label.jpg"  width="700"><br/>
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/yolo_label2.jpg"  width="700"><br/>
  
  - yolo訓練
  
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/yolo_train.png"  width="700"><br/>
  
  - yolo優化
  
  <img src="https://github.com/s1063724/Smart-drone-classification-technology/blob/master/ExecuteSample/yolo_optimal.png"  width="700"><br/>

陸、參考資料
---
[小花蔓澤蘭 台灣環境資訊協會](https://teia.tw/zh-hant/natural-valley/species/11961)<br/>
[小花蔓澤蘭](http://kplant.biodiv.tw/%E5%B0%8F%E8%8A%B1%E8%94%93%E6%BE%A4%E8%98%AD/%E5%B0%8F%E8%8A%B1%E8%94%93%E6%BE%A4%E8%98%AD.htm)<br/>
[小花蔓澤蘭 維基百科](https://zh.wikipedia.org/wiki/%E5%B0%8F%E8%8A%B1%E8%94%93%E6%BE%A4%E8%98%AD)<br/>
[她被小黑蚊咬成紅豆冰 小花蔓澤蘭竟然可以防蚊](https://video.udn.com/news/552393)<br/>
[Google Map API](https://developers.google.com/maps/documentation/javascript/tutorial)<br/>
[Google Earth pro](https://www.google.com/earth/outreach/learn/mapping-from-a-google-spreadsheet/#enter-basic-information-and-publish-your-spreadsheet-1-2)<br/>
[Python(folium 套件)](https://python-visualization.github.io/folium/quickstart.html)<br/>
[ArcGis](https://learn.arcgis.com/en/projects/analyze-return-on-investment-at-united-states-colleges/)<br/>
[順序模型](https://keras.io/guides/sequential_model/)<br/>
[RestNet18](https://pytorch.org/docs/stable/torchvision/models.html)<br/>
[【AI实战】基础环境搭建](https://my.oschina.net/u/876354/blog/1924805)<br/>
[【AI实战】动手训练自己的目标检测模型（YOLO篇)](https://my.oschina.net/u/876354/blog/1927881)<br/>
[使用python模組控制Tello無人機](http://blog.hashteacher.com/?p=1048)<br/>
[ROS Melodic Morenia](http://wiki.ros.org/melodic)<br/>
[Tello_ROS_ORBSLAM](https://github.com/tau-adl/Tello_ROS_ORBSLAM)<br/>
[Video Stream does not work #21](https://github.com/damiafuentes/DJITelloPy/issues/21)<br/>
[ROS以控制空拍機](https://www.coderbridge.com/series/726ee8e84edc4073aab642d1ab5965fa/posts/83556de29b6e4fcf9306e8a7ca14f2a1#article-comment-wrapper)<br/>
小花蔓澤蘭危害與防除現況 臺北市立大學地球環境暨生物資源學系 黃基森、薛翔泰
  

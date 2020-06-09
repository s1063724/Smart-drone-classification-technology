# 智慧無人機偵測小花蔓澤蘭技術
專題介紹影片:https://youtu.be/VHwg3SJm8cI

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

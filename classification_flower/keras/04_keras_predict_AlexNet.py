# encoding=utf-8
# 使用 MobileNet 辨識 2 種花朵
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.resnet50 import preprocess_input
import numpy as np
import os

# 輸出花朵類型
classes = ['Mikania', 'NonMikania']

# Step 1: 載入預先訓練好的模型
model = load_model('Flower3_AlexNet.h5')

# Step 2: 指定輸入影像目錄, 影像格式轉換
TEST_DIR = 'test_images'
for f in sorted(os.listdir(TEST_DIR)):
    source = os.path.join(TEST_DIR, f)
    print(f)
    img = image.load_img(source, target_size=(150, 150)) # 轉換解析度
    x = image.img_to_array(img)    # 影像檔轉為陣列格式
    x = np.expand_dims(x, axis=0)  # 新增一維, 記錄影像樣本個數(可批次處理多個影像檔)
    input_shape = (150, 150, 3)    # AlexNet 模型輸入影像大小
    x = x.reshape((-1, ) + input_shape) / 255  # 像素值正規化前置調整

# Step 3: 預測輸入影像的分類
    preds = model.predict(x)

# Step 4: 預測結果格式調整後印出 
#   print('Predicted:', preds)  
    index_max = np.argmax(preds[0])
    print(index_max, classes[index_max], max(preds[0]))
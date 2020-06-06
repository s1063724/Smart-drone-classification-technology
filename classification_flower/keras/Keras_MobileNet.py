# encoding=utf-8

'''
└── dataset [713 data]
    ├── Mikania [539 data]
    └── NonMikania [174 data]
'''

from keras.applications.mobilenet import MobileNet
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten
from keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam
import matplotlib.pyplot as plt
from IPython.display import display
from PIL import Image


# 產生影像維度
img_width, img_height = 150, 150             # 輸入層影像大小
num_classes = 2                             # 輸出類型個數

train_data_dir = 'data/train'            # 訓練影像所在子目錄
validation_data_dir = 'data/valid'  # 驗證影像所在子目錄
image_aug = 5                               # 影像擴增倍率
nb_train_samples = 357 * image_aug           # 訓練影像樣本數
nb_validation_samples = 356 * image_aug      # 驗證影像樣本數
epochs = 10                                  # 訓練世代
batch_size = 10                              # 批次訓練影像張數

classes = ['Mikania', 'NonMikania']

## 遷移學習 Transfer Learning
# 建立模型
# 使用預先建立之 MobileNet 模型
base_model = MobileNet(weights='imagenet', include_top=False)

# 印出模型中各層網路名稱
for i, layer in enumerate(base_model.layers):
   print(i, layer.name)

# 加入 GlobalAveragePooling2D 層
x = base_model.output
x = GlobalAveragePooling2D()(x)
# 加入全連接層
x = Dense(1024, activation='relu')(x)
# 加入最終分類層
predictions = Dense(num_classes, activation='softmax')(x)

# 設定模型
model = Model(inputs=base_model.input, outputs=predictions)

# 僅訓練 top layers 
# 凍結預先建立之 InceptionResNetV2 的 Convolution layers
for layer in base_model.layers:
    layer.trainable = False

# 選擇最佳化器 Optimizer
adam = Adam(lr=0.01)   # learning rate: 先試 0.01,
                     # 看訓練結果再試 0.001 或 0.1, 
					 # 看訓練結果再試 0.0001 或 1
# rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)  
# adagrad = Adagrad(lr=0.005, epsilon=None, decay=0.0)       
# adadelta = Adadelta(lr=0.8, rho=0.95, epsilon=None, decay=0.0)
# adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)                          
# adamax = Adamax(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
# nadam = Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)

# 編譯模型                          
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

# 產生訓練資料集之擴增影像
train_datagen = ImageDataGenerator(
    rescale=1. / 255)

# 產生驗證資料集之擴增影像
test_datagen = ImageDataGenerator(
    rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
#    save_to_dir='ImageGen/augmented_train',  # 擴增影像放置子目錄
    save_to_dir= None,
    save_prefix='aug',                       # 擴增影像檔名開頭
    save_format='png',                       # 影像檔格式
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
#    save_to_dir='ImageGen/augmented_validation',  # 擴增影像放置子目錄
    save_to_dir= None,
    save_prefix='aug',                            # 擴增影像檔名開頭
    save_format='png',                            # 影像檔格式
    class_mode='categorical')

# 由擴增樣本訓練模型
history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

# 繪出訓練過程準確度變化
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

model.save('Flower3_MobileNet.h5')
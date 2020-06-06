# encoding=utf-8
# 使用 AlexNet

'''
└── dataset [713 data]
    ├── Mikania [539 data]
    └── NonMikania [174 data]
'''
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.layers import BatchNormalization
from keras import backend as K
from keras.optimizers import SGD, Adam
import matplotlib.pyplot as plt


# 產生影像維度
img_width, img_height = 150, 150             # 輸入層影像大小
num_classes = 2                             # 輸出類型個數

train_data_dir = 'data/train'            # 訓練影像所在子目錄
validation_data_dir = 'data/valid'  # 驗證影像所在子目錄
image_aug = 5                               # 影像擴增倍率
nb_train_samples = 539 * image_aug           # 訓練影像樣本數
nb_validation_samples = 174 * image_aug      # 驗證影像樣本數
epochs = 10                                  # 訓練世代
batch_size = 10                              # 批次訓練影像張數

classes = ['Mikania', 'NonMikania']

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# 建立模型
model = Sequential()
# 第 1 層: kernel_size=11, strides=3  適用高解析度影像 
model.add(Conv2D(48, kernel_size=3, strides=1, 
                 activation='relu', padding='same',
                 input_shape=input_shape))
# 第 2 層: pool_size=3, strides=2  適用高解析度影像  
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
model.add(BatchNormalization())
# 第 3 層: kernel_size=5, strides=3  適用高解析度影像  
model.add(Conv2D(128, kernel_size=3, strides=1, activation='relu', padding='same'))
# 第 4 層: pool_size=3, strides=2  適用高解析度影像  
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
model.add(BatchNormalization())
# 第 5 層: kernel_size=3, strides=1 
model.add(Conv2D(192, kernel_size=3, strides=1, activation='relu', padding='same'))
# 第 6 層: kernel_size=3, strides=1 
model.add(Conv2D(192, kernel_size=3, strides=1, activation='relu', padding='same'))
# 第 7 層: kernel_size=3, strides=1 
model.add(Conv2D(128, kernel_size=3, strides=1, activation='relu', padding='same'))
# 第 8 層: pool_size=3, strides=2
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dense(2048, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2048, activation='relu'))
model.add(Dropout(0.5))
# 輸出層： 全連接層, 2048維轉為17維分類
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# 編譯模型
sgd = SGD(lr=0.01,momentum=0.9,decay=0.001)  # learning rate: 先試 0.01, 再試 0.001, 0.1, 0.0001, 1
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
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

model.save('Flower3_AlexNet.h5')

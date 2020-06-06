# encoding=utf-8

'''
└── dataset [674 data]
    ├── Mikania_far [289 data]
    ├── Mikania_medium [243 data]
    ├── Mikania_close [22 data]
    ├── NonMikania_far [19 data]
    ├── NonMikania_medium [66 data]
    └── NonMikania_close [35 data]

---------------------------------------------
└── dataset [713 data]
    ├── Mikania [539 data]
    └── NonMikania [174 data]
'''


from PIL import Image
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.optimizers import SGD, Adam
import matplotlib.pyplot as plt

# 產生影像維度
img_width, img_height = 150, 150
num_classes = 2

train_data_dir = 'data/train'  # 訓練影像所在子目錄
validation_data_dir = 'data/valid'  # 驗證影像所在子目錄
image_aug = 5  # 影像擴增倍率
nb_train_samples = 539 * image_aug  # 訓練影像樣本數
nb_validation_samples = 174 * image_aug  # 驗證影像樣本數
epochs = 10  # 訓練世代
batch_size = 10  # 批次訓練影像張數

classes = ['Mikania', 'NonMikania']

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# 建立模型
model = Sequential()

# CNN1層: 32 個特徵卷積核, 卷積核大小 5x5
model.add(Conv2D(32, (5, 5), strides=1,
                 padding='same',
                 input_shape=input_shape))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))

# CNN2層: 64 個特徵卷積核, 卷積核大小 3x3
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))

# CNN3層: 128 個特徵卷積核, 卷積核大小 3x3
model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
# 全連接層, 128維轉為64維
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
# 輸出層： 全連接層, 64維轉為17維分類
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# Step 3 編譯模型
sgd = SGD(lr=0.01, momentum=0.9, decay=0.001)  # learning rate: 先試 0.01, 再試 0.001, 0.1, 0.0001, 1
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.summary()  # 列印模型架構

# 產生訓練資料集之擴增影像
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=15,  # 擴增影像最多旋轉 15 度
    shear_range=0.2,
    zoom_range=0.2,
    width_shift_range=0,  # 擴增影像最多水平平移 50%
    height_shift_range=0,  # 擴增影像最多垂直平移 20%
    horizontal_flip=True)

# 產生驗證資料集之擴增影像
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    # save_to_dir='ImageGen/augmented_train',  # 擴增影像放置子目錄
    save_to_dir=None,
    save_prefix='aug',  # 擴增影像檔名開頭
    save_format='png',  # 影像檔格式
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    # save_to_dir='ImageGen/augmented_validation',  # 擴增影像放置子目錄
    save_to_dir=None,
    save_prefix='aug',  # 擴增影像檔名開頭
    save_format='png',  # 影像檔格式
    class_mode='categorical')   # one-hot

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

model.save_weights('Flower2_3CNN.h5')

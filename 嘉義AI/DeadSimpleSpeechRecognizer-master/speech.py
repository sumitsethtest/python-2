# 導入函式庫
from preprocess import *
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical

#conda install -c conda-forge librosa 
##pip install tqdm

# 載入 data 資料夾的訓練資料，並自動分為『訓練組』及『測試組』
X_train, X_test, y_train, y_test = get_train_test()
X_train = X_train.reshape(X_train.shape[0], 20, 11, 1)
X_test = X_test.reshape(X_test.shape[0], 20, 11, 1)

# 類別變數轉為one-hot encoding
y_train_hot = to_categorical(y_train)
y_test_hot = to_categorical(y_test)
print("X_train.shape=", X_train.shape)

# 建立簡單的線性執行的模型
model = Sequential()
# 建立卷積層，filter=32,即 output size, Kernal Size: 2x2, activation function 採用 relu
model.add(Conv2D(32, kernel_size=(2, 2), activation='relu', input_shape=(20, 11, 1)))
# 建立池化層，池化大小=2x2，取最大值
model.add(MaxPooling2D(pool_size=(2, 2)))
# Dropout層隨機斷開輸入神經元，用於防止過度擬合，斷開比例:0.25
model.add(Dropout(0.25))
# Flatten層把多維的輸入一維化，常用在從卷積層到全連接層的過渡。
model.add(Flatten())
# 全連接層: 128個output
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.25))
# Add output layer
model.add(Dense(3, activation='softmax'))
# 編譯: 選擇損失函數、優化方法及成效衡量方式
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# 進行訓練, 訓練過程會存在 train_history 變數中
model.fit(X_train, y_train_hot, batch_size=100, epochs=200, verbose=1, validation_data=(X_test, y_test_hot))


X_train = X_train.reshape(X_train.shape[0], 20, 11, 1)
X_test = X_test.reshape(X_test.shape[0], 20, 11, 1)
score = model.evaluate(X_test, y_test_hot, verbose=1)

# 模型存檔
from keras.models import load_model
model.save('ASR.h5')  # creates a HDF5 file 'model.h5'


# 預測(prediction)
mfcc = wav2mfcc('./data/happy/012c8314_nohash_0.wav')
mfcc_reshaped = mfcc.reshape(1, 20, 11, 1)
print("labels=", get_labels())
print("predict=", np.argmax(model.predict(mfcc_reshaped)))

#predict= 2 代表正確

# load
model = load_model('ASR.h5')
print('test after load: ', model.predict(mfcc_reshaped))

語音處理的概念

人類講話的聲音可以以『示波器』(Oscilloscope)測量成一個隨時間變化的波形信號，這種信號對時間的關係，稱之為『時域』

(Time Domain)，在電腦對信號進行分析時，通常信號會先被轉換成在不同頻率下對應的振幅及相位，稱之為『頻域』

（frequency domain），轉換的公式稱為『傅立葉變換』（Fourier transform)，信號經過每隔一段時間取樣，就得到可

以進行分析的數位音檔，附檔名通常是 wav。

我們會對語音作特徵抽取(Feature Extraction)，目前有 FBank、MFCC(Mel frequency cepstral coefficients) 兩種，

特徵抽取前須先對聲音作前置處理：

1.幀(Frame)切割：通常每幀是25ms，幀與幀之間重疊10ms，以避免邊界信號的遺漏。
2.信號加強：針對高頻信號作加強，使信號更清楚。
3.加窗(Window)：目的是消除各個幀兩端可能會造成的信號不連續性，常用的窗函數有方窗、漢明窗等。
4.去除雜訊(denoising or noise reduction)。

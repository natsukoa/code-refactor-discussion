#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')

import keras.datasets
import keras.utils
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')


# In[ ]:


# y_trainが正解タグデータ
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()


# In[ ]:


# データの整形&正規化
X_train = X_train.reshape(60000,784) / 255
X_test = X_test.reshape(10000, 784) / 255

print(X_train.shape)
print(X_test.shape)


# In[ ]:


# 1行のデータが28*28の1つの数字を表している
# データは0-1までの少数で表現されており、これは濃淡の程度を表している
X_train[0][200:210]


# In[ ]:


idx = 0
size = 28

a, b = np.meshgrid(range(size), range(size))
c = X_train[idx].reshape(size, size)
c = c[::-1,:]

print('描かれている数字: {}'.format(y_train[idx]))

plt.figure(figsize=(2.5, 2.5))
plt.xlim(0, 27)
plt.ylim(0, 27)
plt.tick_params(labelbottom="off")
plt.tick_params(labelleft="off")
plt.pcolor(a, b, c)
plt.gray()


# In[ ]:


# ダミーコーディング
y_train = keras.utils.np_utils.to_categorical(y_train)
y_test = keras.utils.np_utils.to_categorical(y_test)


# In[ ]:


#  arrayに1が立っている部分がその数字である、というふうに表示させている。
# 今回の場合は0,1,2,3,4,5,6,7,8,9 のうち5を選択しているので、6番目にフラグが立っている
# というようにもともと数値ではないものを数値化するのがダミーコーディング
y_train[0]


# In[ ]:


# 1ノードにくるデータは重み付けされている。それを全て集約して、ノード内で次元圧縮する（活性化関数を使って）


# In[ ]:


# DLのモデル作成
import keras.layers
import keras.layers.core
import keras.models


# In[ ]:


model = keras.models.Sequential()
# Dense = 層 activation = 活性化関数 
# 隠れ層
model.add(keras.layers.Dense(512, activation='sigmoid', input_shape=(784,)))
# 出力層(いくつかのカテゴライズを行う場合はsoftmaxと使う)
model.add(keras.layers.Dense(10, activation='softmax'))


# In[ ]:


model.summary()


# In[ ]:


model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])


# In[ ]:


model.fit(X_train, y_train, batch_size=200, verbose=1, epochs=10)


# In[ ]:


score = model.evaluate(X_test, y_test, verbose=1)


# In[ ]:


score[1]


# In[ ]:


# 活性化関数の変更
model = keras.models.Sequential()
model.add(keras.layers.Dense(512, activation='relu', input_shape=(784,)))
model.add(keras.layers.Dense(10, activation='softmax'))

# 活性化関数リスト
# https://keras.io/ja/activations/

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=200, verbose=1, epochs=10)
score = model.evaluate(X_test, y_test, verbose=1)
#score[0]はロス
score[1]


# In[ ]:


# 最適化関数の変更
# https://keras.io/ja/optimizers/
model = keras.models.Sequential()
model.add(keras.layers.Dense(512, activation='relu', input_shape=(784,)))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=200, verbose=1, epochs=10)
score = model.evaluate(X_test, y_test, verbose=1)
score[1]


# In[ ]:


# Dropout(汎化性能up/過学習防止)
model = keras.models.Sequential()
model.add(keras.layers.Dense(512, activation='relu', input_shape=(784,)))
model.add(keras.layers.core.Dropout(0.2))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=200, verbose=1, epochs=10)
score = model.evaluate(X_test, y_test, verbose=1)
score[1]


# In[ ]:





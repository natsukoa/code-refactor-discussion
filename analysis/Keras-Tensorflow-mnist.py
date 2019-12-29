#!/usr/bin/env python
# coding: utf-8

from keras.datasets import mnist
import keras.utils
import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Dense
from keras.layers.core import Dropout
from keras.models import Sequential
plt.style.use('ggplot')


# https://github.com/PyLadiesTokyo/code-refactor-discussion

EPOCH_NUM = 10
INPUT_SIZE = 784
PIXEL = 255
HIDDEN_TENSOR = 512
OUTPUT_TENSOR = 10
BATCH_SIZE = 200
VERBOSE = 2


def get_clean_data(train_size, test_size):
    # y_trainが正解タグデータ
    X_train, y_train, X_test, y_test = mnist.load_data()
    
    # データの整形&正規化
    X_train = X_train.reshape(train_size, INPUT_SIZE) / PIXEL
    X_test = X_test.reshape(test_size, INPUT_SIZE) / PIXEL
    # ダミーコーディング
    y_train = keras.utils.np_utils.to_categorical(y_train)
    y_test = keras.utils.np_utils.to_categorical(y_test)
    
    return X_train, y_train, X_test, y_test


# TODO: 引数が固定のものをリストに書き出し
def train_model(X_train, y_train, drop_flg, hidden_activation, 
                output_activation, loss_fanc, optimizer, metrics, **drop_rate):
    """
    
    :param X_train: 
    :param y_train: 
    :param drop_flg: 
    :param hidden_activation: 
    :param output_activation: 
    :param loss_fanc: 
    :param optimizer: 
    :param metrics: 
    :param drop_rate: 
    :return: 
    """
    
    # DLのモデル作成
    model = Sequential()
    # Dense = 層 activation = 活性化関数 
    # 隠れ層
    model.add(Dense(HIDDEN_TENSOR, activation=hidden_activation, 
                    input_shape=(INPUT_SIZE,)))
    if drop_flg:
        model.add(Dropout(drop_rate))
    # 出力層(いくつかのカテゴライズを行う場合はsoftmaxと使う)
    model.add(Dense(OUTPUT_TENSOR, activation=output_activation))
    
    
    model.compile(loss=loss_fanc, optimizer=optimizer, metrics=metrics)
    model.fit(X_train, y_train, batch_size=BATCH_SIZE, verbose=VERBOSE, 
              epochs=EPOCH_NUM)

    return model


def calc_score(model, X_test, y_test):
    return  model.evaluate(X_test, y_test, verbose=VERBOSE)


def plot_num(size, idx):
    color_a, color_b = np.meshgrid(range(size), range(size))
    color_c = X_train[idx].reshape(size, size)
    color_c = color_c[::-1, :]

    print('描かれている数字: {}'.format(y_train[idx]))

    plt.figure(figsize=(2.5, 2.5))
    plt.xlim(0, 27)
    plt.ylim(0, 27)
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")
    plt.pcolor(color_a, color_b, color_c)
    plt.gray()



def main():
    X_train, y_train, X_test, y_test = get_data()

    model1 = train_model(X_train, y_train, drop_flg=0,
                         hidden_activation='sigmoid',
                         output_activation='softmax',
                         loss_fanc='categorical_crossentropy',
                         optimizer='sgd', metrics=['accuracy'])
    print('活性化関数:, 最適化関数:, dropout:なし', 
          calc_score(model1, X_test, y_test))
    # 活性化関数の変更
    model2 = train_model(X_train, y_train, drop_flg=0, hidden_activation='relu',
                         output_activation='softmax',
                         loss_fanc='categorical_crossentropy',
                         optimizer='sgd', metrics=['accuracy'])
    print('活性化関数:, 最適化関数:, dropout:なし', calc_score(model2, X_test, y_test))
    # 最適化関数の変更
    model3 = train_model(X_train, y_train, drop_flg=0, hidden_activation='relu',
                         output_activation='softmax',
                         loss_fanc='categorical_crossentropy',
                         optimizer='adam', metrics=['accuracy'])
    print('活性化関数:, 最適化関数:, dropout:なし',calc_score(model3, X_test, y_test))
    # Dropout(汎化性能up/過学習防止)
    model4 = train_model(X_train, y_train, drop_flg=1, hidden_activation='relu',
                         output_activation='softmax',
                         loss_fanc='categorical_crossentropy',
                         optimizer='adam', metrics=['accuracy'], drop_rate=0.2)
    print('活性化関数:, 最適化関数:, dropout:なし',calc_score(model4, X_test, y_test))
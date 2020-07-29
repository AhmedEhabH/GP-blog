# keras
from tensorflow.python.keras.layers import BatchNormalization, Dropout, Dense, Conv2D, MaxPool2D, Activation, SeparableConv2D, Flatten
from tensorflow.python.keras.models import Sequential

import cv2
import numpy as np
import tensorflow as tf


def make_model():
    tf.keras.backend.clear_session()
    loaded = Sequential()
    # First Block
    loaded.add(Conv2D(16, activation='relu', kernel_size=(
        3, 3), padding='same', input_shape=(128, 128, 3)))
    loaded.add(Conv2D(16, activation='relu',
                      kernel_size=(3, 3), padding='same'))
    loaded.add(MaxPool2D(pool_size=(3, 3)))

    # Second Block
    loaded.add(SeparableConv2D(32, kernel_size=(3, 3), padding='same'))
    loaded.add(SeparableConv2D(32, kernel_size=(3, 3), padding='same'))
    loaded.add(SeparableConv2D(32, kernel_size=(3, 3), padding='same'))
    loaded.add(BatchNormalization())
    loaded.add(Activation('relu'))
    loaded.add(MaxPool2D(pool_size=(3, 3)))

    # Third Block
    loaded.add(SeparableConv2D(64, kernel_size=(3, 3), padding='same'))
    loaded.add(SeparableConv2D(64, kernel_size=(3, 3), padding='same'))
    loaded.add(BatchNormalization())
    loaded.add(Activation('relu'))
    loaded.add(MaxPool2D(pool_size=(3, 3)))

    # Forth Block
    loaded.add(SeparableConv2D(128, kernel_size=(3, 3), padding='same'))
    loaded.add(SeparableConv2D(128, kernel_size=(3, 3), padding='same'))
    loaded.add(BatchNormalization())
    loaded.add(Activation('relu'))
    loaded.add(MaxPool2D(pool_size=(3, 3)))
    loaded.add(Dropout(0.25))

    # Fully Connected Layer
    loaded.add(Flatten())
    loaded.add(Dense(units=128, activation='relu'))

    # Output layer
    loaded.add(Dense(1, activation='sigmoid'))
    loaded.load_weights('./flaskblog/BESTWeights.hdf5')
    return loaded


def model_predict(img_path, model, graph):
    print("CHEST")
    print(img_path)
    IMG = cv2.imread(img_path)

    # Pre-processing the image
    Model_input = cv2.resize(IMG.copy(), (128, 128))

    Model_input = np.array(Model_input)

    Model_input = Model_input / 255

    pred = model.predict([np.array([Model_input])])
    print(pred)
    prediction = np.round(pred)
    print(prediction)
    return prediction


def predict(img_path):
    classes = ['NORMAL', 'PNEUMONIA']
    model = make_model()
    graph = tf.compat.v1.get_default_graph()
    prediction = model_predict(img_path, model, graph)
    predicted_class = classes[prediction[0][0].astype('int')]
    print('We think that is {}.'.format(predicted_class))
    return str(predicted_class)

import keras
import librosa
import numpy as np
import tensorflow as tf
from keras import models
from tensorflow.python.keras.models import load_model

# Загрузка аудио файла
audio_file = '23941.wav'
y, sr = librosa.load(audio_file)

# Выделение спектрограммы источника звука
D = librosa.stft(y)
magnitude = np.abs(D)
phase = np.angle(D)

# Загрузка модели DeepSalience
model = load_model('vocal.h5')

# Предобработка данных
X = np.stack([magnitude, phase], axis=-1)
X = np.expand_dims(X, axis=0)

# Получение предсказаний
predictions = model.predict(X)

# Извлечение вокальной и аккомпанемент компонентов
vocal = predictions[0][:, 0]
accompaniment = predictions[0][:, 1]

# Сохранение компонентов в файлы
librosa.output.write_wav('vocal.wav', vocal, sr)
librosa.output.write_wav('accompaniment.wav', accompaniment, sr)

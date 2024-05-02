import torch
import torchaudio
import numpy as np
import scipy
# import youtube_dl
import stempeg
import os
# from google.colab import files
from IPython.display import Audio, display
import musdb
from scipy import signal
from openunmix import predict
import soundfile as sf

use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")

# Путь к вашему WAV или MP3 файлу
audio_file_path = "23941.wav"  # Измените на путь к вашему файлу

# Загрузка аудиофайла с помощью torchaudio
waveform, sample_rate = torchaudio.load(audio_file_path, normalize=True)

# Приведение аудио к нужному формату для open-unmix
if waveform.shape[0] == 2:
    # Если аудио имеет 2 канала, преобразуем его в моно
    waveform = torch.mean(waveform, dim=0, keepdim=True)

# Подготовка аудио для обработки
waveform = waveform.to(device).float()

# Предсказание компонентов с помощью open-unmix
estimates = predict.separate(waveform, rate=sample_rate, device=device)

for target, estimate in estimates.items():
    print(target)
    audio = estimate.detach().cpu().numpy()[0]

    # Сохранение компонента в WAV файл
    component_path = f"{os.path.basename(audio_file_path)}_{target}.wav"
    sf.write(component_path, audio.T, sample_rate)

    # Отображение компонента в виде аудиоплеера
    display(Audio(audio, rate=sample_rate))

    print(f"Component {target} saved to {component_path}")
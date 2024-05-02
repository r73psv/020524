import streamlit as st
import demucs
import numpy as np
import scipy.io.wavfile as wav
from torchaudio.pipelines import HDEMUCS_HIGH_MUSDB_PLUS

# Load the Demucs model
# model = demucs.load_model()
bundle = HDEMUCS_HIGH_MUSDB_PLUS

model = bundle.get_model()
# Create a Streamlit web app
st.title("Music Separator App")

# Upload a music file
uploaded_file = st.file_uploader("Upload a music file", type=["wav"])

if uploaded_file is not None:
    audio_data = uploaded_file.read()

    # Separate components using Demucs model
    audio_array = np.frombuffer(audio_data, dtype=np.int16)
    audio = (44100, audio_array)  # Assuming the sample rate is 44100 Hz
    vocals, bass, drums, other = model.separate(audio, sources=["vocals", "bass", "drums", "other"])

    # Save the separated components as audio files
    wav.write("vocals.wav", 44100, vocals.T)
    wav.write("bass.wav", 44100, bass.T)
    wav.write("drums.wav", 44100, drums.T)
    wav.write("other.wav", 44100, other.T)

    # Display the separated components
    st.audio("vocals.wav", format="audio/wav", start_time=0)
    st.audio("bass.wav", format="audio/wav", start_time=0)
    st.audio("drums.wav", format="audio/wav", start_time=0)
    st.audio("other.wav", format="audio/wav", start_time=0)
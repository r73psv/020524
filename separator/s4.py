import openunmix
import soundfile as sf

# Load the OpenUnmix model
model = openunmix.umxl()

# Load the music file
audiodata, samplerate = sf.read("23941.wav")

# Reshape the audio data if it has multiple channels
if audiodata.shape[1] > 1:
    # Convert stereo to mono by taking the mean
    audiodata = audiodata.mean(axis=1)

# Use the model to separate the components
components = model.forward(audiodata)

# Save the separated components as audio files
sf.write("vocals.wav", components['vocals'], samplerate)
sf.write("bass.wav", components['bass'], samplerate)
sf.write("drums.wav", components['drums'], samplerate)
sf.write("other.wav", components['other'], samplerate)
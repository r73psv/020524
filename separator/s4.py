import openunmix

import openunmix
import soundfile as sf

# Load the OpenUnmix model
model = openunmix.umxl()

# Load the music file
audiodata, samplerate = sf.read("23941.wav")

# Separate components using OpenUnmix model
results = model.run(audiodata)



# Save the separated components as audio files
sf.write("vocals.wav", results['vocals'], samplerate)

sf.write("bass.wav", results['bass'], samplerate)

sf.write("drums.wav", results['drums'], samplerate)

sf.write("other.wav", results['other'], samplerate)
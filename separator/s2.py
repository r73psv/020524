import tkinter as tk
from tkinter import filedialog
import openunmix
import soundfile as sf


class MusicSeparationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Separation App")

        self.model = openunmix.openunmix()

        self.load_button = tk.Button(self.master, text="Load Music File", command=self.load_music_file)
        self.load_button.pack()

    def load_music_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if not file_path:
            return

        audio_data, sample_rate = sf.read(file_path)
        results = self.model.run(audio_data)

        vocals_path = file_path.replace(".wav", "_vocals.wav")
        bass_path = file_path.replace(".wav", "_bass.wav")
        drums_path = file_path.replace(".wav", "_drums.wav")
        other_path = file_path.replace(".wav", "_other.wav")

        sf.write(vocals_path, results['vocals'], sample_rate)
        sf.write(bass_path, results['bass'], sample_rate)
        sf.write(drums_path, results['drums'], sample_rate)
        sf.write(other_path, results['other'], sample_rate)

        print("Music components separated and saved to files.")


root = tk.Tk()
app = MusicSeparationApp(root)
root.mainloop()
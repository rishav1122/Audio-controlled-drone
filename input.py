import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 48000
# Recording duration
duration = 3

recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)  
# Record audio for the given number of seconds
print("start")
sd.wait()

write("recording0.wav", freq, recording)
# Convert the NumPy array to audio file
wv.write("res.wav", recording, freq, sampwidth=2)

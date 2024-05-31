import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

samplerate = 16000 
duration = 7

print("recording...")
audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='float32')
sd.wait()  
print("finish")


audio_path = "audio_health.wav"
write(audio_path, samplerate, audio_data)



import wave
import sys
# import librosa

from vosk import Model, KaldiRecognizer, SetLogLevel

# You can set log level to -1 to disable debug messages
SetLogLevel(0)

# wf = wave.open(sys.argv[1], "rb")
# if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
#     print("Audio file must be WAV format mono PCM.")
#     sys.exit(1)

audio_file = "path/to/audio/file.wav"
audio, sample_rate = librosa.load(audio_file, sr=16000)

#model = Model(lang="en-us")

# You can also init model by name or with a folder path
model = Model("Speech-Recognition-Model")
# model = Model("models/en")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
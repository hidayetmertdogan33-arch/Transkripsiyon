import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import GoogleTranslator   # googletrans yerine bu

print("Ses Tanıma Ve Çevirme Uygulamasına Hoşgeldiniz")
print("Bu uygulama, konuşmanızı kaydedecek ve ardından metne dönüştürecektir. Daha sonra, metni başka bir dile çevirebilirsiniz. Lütfen konuşmaya başlamadan önce mikrofonunuzun çalıştığından emin olun.")
print("Lisans bilgileri için LICENSE dosyasını okuyun. README dosyasında önemli bilgileri, yüklenecek dosyaları ve .")

duration = 5 
sample_rate = 44100
print("Şimdi konuşun...")
recording = sd.rec(
  int(duration * sample_rate), 
  samplerate=sample_rate,      
  channels=1,                 
  dtype="int16")       
sd.wait()  
wav.write("output.wav", sample_rate, recording)
print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="tr")
    print("Şunu söylediniz:", text)
except sr.UnknownValueError:             
    print("Konuşma tanınamadı. (Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadı.)")
except sr.RequestError as e:             
    print(f"Hizmet hatası. (WI-FI ve bağlı değilsiniz ve ya API kullanılamıyor.): {e}")
    text = None  

if text:  
    translated = GoogleTranslator(source='tr', target='es').translate(text)
    print("Çeviri:", translated)

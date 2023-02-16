import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
import time

# 必要なリソースがダウンロードされているか確認する
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    # ダウンロードしていないリソースがある場合はダウンロードする
    nltk.download('punkt', quiet=True)
    while True:
        try:
            nltk.data.find('tokenizers/punkt')
            break
        except LookupError:
            time.sleep(1)

# 音声入力
r = sr.Recognizer()
with sr.Microphone() as source:
    print("話しかけてください")
    audio = r.listen(source)

# 音声認識
audio_data = sr.AudioData(audio.get_raw_data(convert_rate=16000, convert_width=2), 16000, 2)
try:
    text = r.recognize_google(audio_data=audio_data, language='ja-JP')
    print("認識結果: " + text)
except sr.UnknownValueError:
    print("音声が認識できませんでした")
except sr.RequestError as e:
    print("Google Speech Recognition APIへのリクエストに失敗しました; {0}".format(e))

# 自然言語処理
tokens = word_tokenize(text)
print("トークン化: " + str(tokens))
import speech_recognition as sr
from datetime import datetime

filename = datetime.now().strftime('%Y%m%d_%H:%M:%S')
txt = filename + ".txt"

with open(txt, 'w') as f:  #txtファイルの新規作成
  f.write(filename + "\n")  #最初の１行目にfilenameを記載
 
r = sr.Recognizer()
mic = sr.Microphone()

while True:
  print("Say something ...")

  with mic as source:
    r.adjust_for_ambient_noise(source)  # 雑音対策
    audio = r.listen(source)
  
  print("Now to recognaize it ...")

  try:
    print(r.recognize_google(audio, language='ja-JP'))

    #stopと言えば音声認識を止める
    if r.recognize_google(audio, language='ja-JP') == "ストップ":
      print("end")
      break
    with open(txt, 'a') as f:  #ファイルの末尾に追記していく
      f.write("\n" + r.recognize_google(audio, language='ja-JP'))   
  
  #以下は認識できない場合に認識が止まらないようにする対策
  except sr.UnknownValueError:
    print("could not understand audio")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
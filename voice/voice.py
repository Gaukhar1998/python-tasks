# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hi this is working ");
# engine.setProperty('volume',0.9)
# engine.runAndWait()

# import subprocess
# from gtts import gTTS
# audio_file = "hello.mp3"
# tts = gTTS(text="Hello World!", lang="en")
# tts.save(audio_file)
# return_code = subprocess.call(["afplay", audio_file])

# from pygame import mixer # Load the required library
# mixer.init()
# mixer.music.load('C:/Users/hp/Desktop/voice/bts.mp3')
# mixer.music.play()

# import cv2
# import tesseract
# #import numpy as np
# #import pyttsx
# import say
# import os
# import mp3play
# from gtts import gTTS
# from win32com.client import constants, Dispatch
# scr = cv2.imread('C:/Users/hp/Desktop/voice/voice.png',0)
# api = tesseract.TessBaseAPI()
# api.Init(".","eng",tesseract.OEM_DEFAULT)
# api.SetPageSegMode(tesseract.PSM_AUTO)
# image = cv2.CreateImageHeader((scr.shape[1],scr.shape[1]), cv2.IPL_DEPTH_8U,1)
# cv2.SetData(image, scr.tostring(), scr.dtype.itemsize*scr.shape[1])
# tesseract.SetCvImage(image,api)
# text = api.GetUTF8Text()
# conf = api.MeanTextConf()
# g=open('god.txt','w')
# g.write(text)
# g.close()
# g = open("god.txt")
# thegod = g.read()
# with open("god.txt","r") as f:
#     for line in f:
#         cleanedLine = line.strip()
#         if cleanedLine:
#             print (cleanedLine)
# speaker = Dispatch("SAPI.SpVoice")
# speaker.Speak(text)
# del speaker

# from gtts import gTTS
# def makeMP3(words, mp3name, language="fr"):
#     tts = gTTS(text=words, lang=language)
#     tts.save("%s.mp3" %mp3name)
#     print ("File %s.mp3 created" %mp3name)
# text = "merci beaucoup"
# makeMP3(text,"french")

from gtts import gTTS
with open("text.txt", encoding="UTF-8") as file:
    file = file.read()

speak = gTTS(file, lang="en")
speak.save("audio_new.mp3")
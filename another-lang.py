import speech_recognition as sr
from gtts import gTTS
import time
from datetime import date
from datetime import datetime
import webbrowser
import os
import playsound

run2 = False
run3 = True
robotb =  ""
r = sr.Recognizer()

def speak(text):
	tts = gTTS(text=text, lang='vi') #set language in lang='vi' (en,fr,ch,....)
	filename = 'voice.mp3'
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)


#main code (rewrite code with your language)
while run3:
	with sr.Microphone() as source:
		print("Robot: I'm listening")
		audio_data = r.record(source, duration=5)
		
	try:
		you = r.recognize_google(audio_data, language="vi")
	except :
		you = "(không thấy gì)"
	print("You: ",str(you)) 
	

	if you == "Xin chào" :
		robotb = "chào bạn"
	elif you == "wikipedia" :
		robotb = ""
	elif you == "(không thấy gì)" :
		robotb = "tôi không hiểu"
	elif "Hôm nay" in you :
		robotb = time.strftime("%B, %d, %Y")
	elif "mấy giờ" in you :
		robotb = time.strftime("%H gio %M phut %S giay")
	elif you == "Bạn tên là gì":
		robotb = "tôi là Alise,một trí tuệ nhân tạo"
	elif "open " in you :

		run2 = True
		run3 = False
	elif you == "tạm biệt" :
		robotb = "Chào bạn"
		print("Robot: " + robotb)
		speak(robotb)
		break
	else:
		robotb = "tôi chưa được lập trình phần đó"

	print("Robot:... ")
	print("Robot: " + robotb)
	speak(robotb)
	
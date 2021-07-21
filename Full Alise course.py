from datetime import date
from datetime import datetime
from gtts import gTTS
from tkinter import *
import tkinter as tk
import sys, os 
import time
import webbrowser
import keyboard
import playsound
import speech_recognition as sr
import requests

#tạo các giá trị
win = tk.Tk()
robot_ear = sr.Recognizer()
robotb = ""
today = date.today()
now = datetime.now()
run = True
run2 = True
run3 = True
run4 = True

#giá trị về thời tiết
res = requests.get('https://ipinfo.io/')
data = res.json()
city = data['city']
user_api = 'fdf44e726eb32e35c792708deb85dedf'

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

r = sr.Recognizer()
def resource_path(relative_path):
		if hasattr(sys, '_MEIPASS'):
			return os.path.join(sys._MEIPASS, relative_path)
		return os.path.join(os.path.abspath("."), relative_path)

def speak(text):
	tts = gTTS(text=text, lang='en')
	filename = 'voice.mp3'
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)

while run:
	with sr.Microphone() as source:
		print("Robot: I'm listening")
		audio_data = r.record(source, duration=5)
		
	try:
		you = r.recognize_google(audio_data)
	except :
		you = "(nothing)"
	print("You: ",str(you)) 
	
	if you == "hello" or "Hello":
		robotb = "Hello master" or "hi there" 
	elif you == "(nothing)" :
		robotb = "i can't hear you" or "i don't understand"
	elif "today" or "Today" in you :
		robotb = today.strftime("%B %d %Y")
	elif "time" or "Time" in you :
		robotb = time.strftime("%H hour %M minute %S second")
	elif "f***"  in you :
		robotb = "you can't say badword"
	elif you == "what is your name" or "What is your name":
		robotb = "I am Alise, a AI assistant"
	elif you == "hey you" :
		robotb = "I'm here"
	elif "website" in you :
		robotb = "change to another service please wait"
		win.title("Find something")
		win.geometry("800x600")

		lb = Label(win, text="Press your URL(link)", fg="red" , font=("Arial", 12))
		lb.grid(column=0, row=0)

		txt = Entry(win, width=20)
		txt.grid(column=0, row=1)

		def button():
			lb.configure(text = "Searching "  + txt.get())
			webbrowser.open(txt.get())
			return

		halo = Button(win, text="Search", command=button)
		halo.grid(column=1, row=3)
		win.mainloop()
	elif "weather" or "Weather" in you :
		print("Latitude : ", latitude)
		print("Longitude : ", longitude)
		print("City : ", city)


		print ("-------------------------------------------------------------")
		print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
		print ("-------------------------------------------------------------")

		print ("Current temperature is: {:.2f} deg C".format(temp_city))
		print ("Current weather desc  :",weather_desc)
		print ("Current Humidity      :",hmdt, '%')
		print ("Current wind speed    :",wind_spd ,'kmph')

	elif "Vietnamese" in you:
		robotb = "change to Vietnamese mode"
		while run3:
			def speak(text):
				tts = gTTS(text=text, lang='vi')
				filename = 'voice.mp3'
				tts.save(filename)
				playsound.playsound(filename)
				os.remove(filename)

			with sr.Microphone() as source:
				print("Robot: Tôi đang nghe bạn nói đây")
				audio_data = r.record(source, duration=5)
				
			try:
				you = r.recognize_google(audio_data, language="vi")
			except :
				you = "(không thấy gì)"
			print("You: ",str(you)) 
			

			if you == "Xin chào" or "xin chào" :
				robotb = "chào bạn"
			elif you == "(không thấy gì)" :
				robotb = "tôi không hiểu"
			elif "hôm nay" or "Hôm nay" in you :
				robotb = time.strftime("%B, %d, %Y")
			elif "mấy giờ" or "Mấy giờ" in you :
				robotb = time.strftime("%H gio %M phut %S giay")
			elif you == "Bạn tên là gì":
				robotb = "tôi là Alise,một trí tuệ nhân tạo"
			elif "mở tìm kiếm" or "Mở tìm kiếm" in you :
				robotb = "đang chuyển sang dịch vụ khác , xin chờ"
				win.title("Find something")
				win.geometry("800x600")

				lb = Label(win, text="Bạn muốn tìm cái gì ?", fg="red" , font=("Arial", 12.5))
				lb.grid(column=0, row=0)

				txt = Entry(win, width=20)
				txt.grid(column=0, row=1)

				def button():
					lb.configure(text = "Đang tìm "  + txt.get())
					webbrowser.open(txt.get())
					return

				halo = Button(win, text="Tìm kiếm", command=button)
				halo.grid(column=1, row=3)
				win.mainloop()
			elif "tạm biệt" in you :
				robotb = "Chào bạn"
				def speak(text):
					tts = gTTS(text=text, lang='en')
					filename = 'voice.mp3'
					tts.save(filename)
					playsound.playsound(filename)
					os.remove(filename)
				print("Robot: " + robotb)
				speak(robotb)
				break
			else:
				robotb = "tôi chưa được lập trình phần đó"

			print("Robot:... ")
			print("Robot: " + robotb)
			speak(robotb)
	elif "bye" in you :
		robotb = "Bye master, See you again"
		print("Robot: " + robotb)
		speak(robotb)
		break
	else:
		robotb = "I have not programmed this part yet"

	print("Robot:... ")
	time.sleep(1)
	print("Robot: " + robotb)
	speak(robotb)

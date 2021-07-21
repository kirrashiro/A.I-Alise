import speech_recognition as sr

r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		audio_data = r.record(source, duration=5)
		print("dang dich")
	try:
		text = r.recognize_google(audio_data,language="vi") or r.recognize_google(audio_data,language="en")
	except:
		text = ""
		print(text)

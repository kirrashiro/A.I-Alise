import wikipedia
import time


wikipedia.set_lang("vi")
while True:
	wiki = input()
	if wiki == "Tiến" or "Đặng Việt Tiến":
		time.sleep(2)
		print("Tiến hay Đặng việt Tiến là thằng trẻ trâu,3 đời làm màu và hay ghen")
	elif wiki == "Hà Linh":
		time.sleep(2)
		print("Hà LInh là 1 thực thể trong phân nhánh con người và là crush của Tiến")

	else:	
		try:
			lol = wikipedia.summary(str(wiki), sentences=1)
		except:
			lol = "không tìm thấy thông tin của " + str(wiki)
		print(lol)
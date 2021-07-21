from tkinter import *
import tkinter as tk
import wikipedia
 
wikipedia.set_lang("vi")
win = tk.Tk()

win.title("Find something")
win.geometry("800x600")
lb = Label(win, text="Nhập URL", fg="red" , font=("Arial", 25))
lb.grid(column=0, row=0)
txt = Entry(win, width=20)
txt.grid(column=0, row=5)
def button():
	lb.configure(text = wikipedia.summary(txt.get()))
	wikipedia.summary(txt.get(), sentences=1)
	return
halo = Button(win, text="TÌM KIẾM", command=button)
halo.grid(column=1, row=5)
win.mainloop()

import pyautogui
from tkinter import *


def get_screenshot():
    add_data = entry.get()
    path = add_data+'\\screenshot1.png'
    print(path)
    ss = pyautogui.screenshot()
    ss.save(path)


win = Tk()
win.title('ScreenShot')
win.geometry('700x400')
win.config(bg='yellow')
win.resizable(False, False)

entry = Entry(win, font=('Arial', 30))
entry.place(x=20, height=70, width=660, y=50)


button = Button(win, text='Pronto', font=('Arial', 50), command=get_screenshot)
button.place(x=250, y=140, height=100, width=200)




win.mainloop()
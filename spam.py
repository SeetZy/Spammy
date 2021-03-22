from tkinter import *
from tkinter.ttk import *
import pyautogui, time

root = Tk()

root.title("Spammy")
root.config(bg="#100e17")
root.iconbitmap('')
root.geometry("400x500")

time.sleep(5)

img = PhotoImage(file=r"")


def startSpam():
    input = Enter.get()
    while True:
        for word in input:
            time.sleep(0.3)
            pyautogui.typewrite(word)
            pyautogui.press("enter")

        if pyautogui.press("enter") == 9:
            time.sleep(2)
        else:
            time.sleep(0.3)


def stopSpam():
    quit()


Enter = Entry(root, width=53)
Enter.place(x=38, y=200)

btn = Button(root, text='Start', command=lambda: startSpam()).place(x=100, y=350)
btn2 = Button(root, text='Stop', command=lambda: stopSpam()).place(x=230, y=350)
btn3 = Button(root, text='i').place(x=360, y=460)

root.mainloop()

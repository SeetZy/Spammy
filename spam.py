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

textBox = Text(root, height=3, width=29, font=("Helvetica", 14)).place(x=38, y=200)


def startSpam():
    INPUT = textBox.get("1.0", "end-1c")
    for word in INPUT:
        time.sleep(0.3)
        pyautogui.typewrite(word)
        pyautogui.press("enter")


def stopSpam():
    quit()


btn = Button(root, text = 'Start').place(x=100, y=350)
btn['command'] = startSpam()

btn2 = Button(root, text = 'Stop').place(x=230, y=350)
btn2['command'] = stopSpam()

root.mainloop()

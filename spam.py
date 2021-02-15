import pyautogui, time
time.sleep(5)


def spam():
    f = open("spamtext.txt", 'r')
    for word in f:
        time.sleep(0.3)
        pyautogui.typewrite(word)
        pyautogui.press("enter")

    if pyautogui.press("enter") == 9:
        time.sleep(2)
    else:
        time.sleep(0.3)


while True:
    spam()

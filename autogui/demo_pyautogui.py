import pyautogui
import time

maxcount = 500
for i in range(1,maxcount):
    if (i%2) == 0:
        pyautogui.moveTo(10,5)
    else:
        pyautogui.moveTo(300, 5)
    pyautogui.click()  

    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print("move and click at " + str(result) + " " + str(i) + " of " + str(maxcount))
    time.sleep(15)

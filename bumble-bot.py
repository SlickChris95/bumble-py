import webbrowser
import pyautogui
import time

url = 'https://bumble.com/app'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
# pyautogui.click(312,55)
# pyautogui.typewrite('https://tinder.com/app/matches')
time.sleep(5.3)

i = 0
while i < 5:
    # pyautogui.click(1265,981)
    pyautogui.press("right")
    time.sleep(2.2)
    i = i + 1

time.sleep(3)

print('All Done.')

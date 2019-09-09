import webbrowser

url = 'https://www.google.com/'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
print('done')

# time.sleep(10)
#
# subprocess.call("bumble-bot.py", shell=True)
# print('done')

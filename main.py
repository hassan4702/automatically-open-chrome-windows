import time
import webbrowser
from pynput.keyboard import Key, Controller
import winapps

application = 'chrome'
for apps in winapps.search_installed(application):
    pass

list1 = str(apps.install_location)
url = "google.com"
chrome_path = list1 + "/chrome.exe"
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get("chrome").open(url)
time.sleep(0.5)
keyboard = Controller()
for x in range(5):
    keyboard.press(Key.ctrl)
    keyboard.press("n")
    keyboard.release("n")
    keyboard.release(Key.ctrl)

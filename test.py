from pyautogui import moveTo, click, ImageNotFoundException, locateOnScreen, moveRel
from win32gui import FindWindow, SetWindowPos, MoveWindow, GetWindowRect
from time import sleep
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW
import share
import random

print("寻找有无更新，有无进入游戏关键图像")
while True:
    num = random.randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = random.uniform(0.1, 0.3)
    try:
        auto_3 = locateOnScreen("images/2.png", confidence=0.9)
        moveRel(888, 888, duration=1)
        click()
    except ImageNotFoundException:
        print("没找到")

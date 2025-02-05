from pyautogui import moveTo, click, ImageNotFoundException, locateOnScreen, moveRel
from win32gui import FindWindow, SetWindowPos, MoveWindow, GetWindowRect
from time import sleep
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW
import share
from random import randint, uniform
from threading import Event

# 创建一个线程事件
share.stop_event = Event()
def running():
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    while not share.stop_event.is_set():
        print("寻找有无更新，有无进入游戏关键图像")
        try:
            auto_3 = locateOnScreen("images/image.png", confidence=0.8)
            moveTo(auto_3, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
        

            
        except ImageNotFoundException:
            print("没有找到进入游戏的关键图像")


def FGO():
    while not share.stop_event.is_set():
        print("寻找窗口句柄中")
        hwnd = FindWindow("Qt5156QWindowIcon", "MuMu模拟器12")
        if hwnd:
            print("成功找到模拟器句柄")
            sleep(0.5)
            a, b, c, d = GetWindowRect(hwnd)
            x = c - a
            y = d - b
            SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, x, y, SWP_SHOWWINDOW)
            break
        else:
            print("没有找到窗口句柄，继续循环查找")
            sleep(1)
    while not share.stop_event.is_set():
        num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
        num_f = uniform(0.1, 0.3)
        print("开始点击代理")
        try:
            auto_2 = locateOnScreen("images/img_2.png", confidence=0.8)
            moveTo(auto_2, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            break
        except ImageNotFoundException:
            print("没有找到小猫")
            sleep(1)

from subprocess import Popen
from pyautogui import moveTo, click, ImageNotFoundException, locateOnScreen, moveRel
from win32gui import FindWindow, SetWindowPos
from time import sleep
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW
from threading import Thread, Event
from random import randint, uniform
from start_part import Start_FGO, launching
import share


def mumu_error():
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    while True:
        try:
            auto_1 = locateOnScreen("images/img.png", confidence=0.8)
            print("找到模拟器错误了")
            moveTo(auto_1, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            share.stop_event.set()
            sleep(10)
            # 这里需要清除标记再启动
            share.stop_event.clear()
            Start_FGO()
            # 注意要重新获取窗口句柄
            break
        except ImageNotFoundException:
            print("多线程进行中，没有找到模拟器错误")
            sleep(5)


def start_daily():
    print("进入模拟器中...")
    launcher = Popen(["E:\\MuMu\\MuMuPlayer-12.0\\shell\\MuMuPlayer.exe"])
    sleep(10)
    mumu_error1 = Thread(target=mumu_error)
    mumu_error1.start()
    Start_FGO()
    # 找句柄放在FGO里，这样每启动一次，就能置顶一下，很ok
    # 还需要做一个启动PC端clash，然后再杀进程的逻辑
    # 不然每次都进不去，或者说还要检查，麻烦
    sleep(2)
    launching()

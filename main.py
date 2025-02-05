from tkinter import Tk, Button, Label, Frame
from ctypes import windll
from start import start_daily
windll.shcore.SetProcessDpiAwareness(1)  # 禁用 DPI 缩放


# 定义按钮功能


def exit_app():
    root.quit()


# 初始化主窗口
root = Tk()
root.title("FGO自动化")
root.geometry("1080x720")
root.configure(bg="#f7f7f7")  # 背景颜色

# 标题
main_label = Label(
    root,
    text="FGO 自动化工具",
    font=("微软雅黑", 36, "bold"),
    bg="#f7f7f7",
    fg="#4a4a4a",
    pady=20
)
main_label.pack()

# 按钮框架
button_frame = Frame(root, bg="#f7f7f7")
button_frame.pack(pady=30)


# 创建按钮的通用函数
def create_button(parent, text, command, row, column, bg_color, hover_color, **grid_kwargs):
    button = Button(
        parent,
        text=text,
        command=command,
        width=15,
        height=2,
        font=("微软雅黑", 16),
        bg=bg_color,
        fg="white",
        activebackground=hover_color,
        activeforeground="white",
        bd=0,
        relief="flat",
        cursor="hand2"  # 鼠标悬停时显示手形光标
    )
    button.grid(row=row, column=column, padx=20, pady=10, **grid_kwargs)

    # 添加悬停效果
    def on_enter(event):
        button.config(bg=hover_color)  # 鼠标悬停时更改颜色

    def on_leave(event):
        button.config(bg=bg_color)  # 鼠标离开时恢复原色

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)


# 添加按钮
create_button(button_frame, "一键启动日常", start_daily, 0, 0, bg_color="#4CAF50", hover_color="#3E8E41")
create_button(button_frame, "退出程序", exit_app, 0, 1, bg_color="#F44336", hover_color="#D32F2F")  # 红色按钮

# 状态栏
status_label = Label(
    root,
    text="© 2025 FGO自动化工具 | Designed by 干净的小周",
    font=("微软雅黑", 12),
    bg="#f7f7f7",
    fg="#9e9e9e"
)
status_label.pack(side="bottom", pady=10)

# 启动主循环
root.mainloop()

if __name__ == '__main__':
    print('PyCharm')

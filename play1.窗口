import random
import time
import tkinter as tk

# 抑制 Tkinter 弃用警告
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def create_warm_tip():
    # 创建窗口
    window = tk.Toplevel()
    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # 窗口尺寸和位置（随机）
    window_width = 250
    window_height = 100
    x = random.randint(50, screen_width - window_width - 50)
    y = random.randint(50, screen_height - window_height - 50)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.resizable(False, False)
    window.attributes('-topmost', True)  # 窗口置顶

    # 定义多种背景颜色方案
    bg_schemes = [
        {'bg': '#FFE4E6', 'fg': '#BE123C'},
        {'bg': '#F0F9FF', 'fg': '#0369A1'},
        {'bg': '#F0FDF4', 'fg': '#15803D'},
        {'bg': '#FEF7CD', 'fg': '#854D0E'},
        {'bg': '#FAF5FF', 'fg': '#7C3AED'},
    ]
    scheme = random.choice(bg_schemes)
    window.configure(bg=scheme['bg'])

    # 暖心提示语列表
    tips = [
        "在干嘛", "笨蛋琪", "所有烦恼都消失", "小胖脸",
        "好好加油", "早点休息", "期待下一次见面", "顺顺利利",
        "每天元气满满", "你很棒了", "每天都要开心", "记得想我"
        "按时吃饭啊笨", "记得回我消息啊笨", "多笑笑啊笨", "相信你"
    ]
    tip = random.choice(tips)

    # 显示提示语
    tip_label = tk.Label(
        window,
        text=tip,
        bg=scheme['bg'],
        fg=scheme['fg'],
        font=('微软雅黑', 14),
        wraplength=200,
        justify='center'
    )
    tip_label.place(relx=0.5, rely=0.5, anchor='center')

    # 3秒后自动关闭窗口
    window.after(4000, window.destroy)

def main():
    # 创建主窗口并隐藏
    root = tk.Tk()
    root.withdraw()

    # 生成多个提示窗口
    for _ in range(30):  # 可修改数量控制窗口个数
        create_warm_tip()
        root.update()
        time.sleep(0.8)  # 窗口生成间隔

    # 程序结束前的处理
    root.after(5000, root.destroy)
    root.mainloop()

if __name__ == '__main__':
    main()

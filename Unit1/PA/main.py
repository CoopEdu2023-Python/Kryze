import os
# 引用的清屏函数
def clear_screen():
    if os.name == 'posix':
        # Unix/Linux/MacOS
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        # Windows
        os.system('cls')
# 判断输赢
def win(list, x ,y):
    if list[0][y] == list[1][y] == list[2][y]:
        return 1
    elif list[x][0] == list[x][1] == list[x][2]:
        return 1
    elif (list[0][0] == list[1][1] == list[2][2]) or (list[0][2] == list[1][1] == list[2][0]) and (not list[1][1] == ' '):
        return 1
    else:
        return 0
# 开始界面
print("井字棋")
# 初始化棋子状态
ir = 0
list = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
tp = ['O', 'X']
x = 0
y = 0
i = 0
flag = 0
os.system('cls')
# 主要部分
while flag == 0:
    clear_screen()
    if ir == 1:
        print("非法输入，请重新输入")
    bk = f"{list[0][0]}  | {list[0][1]} |  {list[0][2]}\n___|___|___\n   |   |   \n{list[1][0]}  | {list[1][1]} |  {list[1][2]}\n___|___|___\n   |   |   \n{list[2][0]}  | {list[2][1]} |  {list[2][2]}"
    print(bk)
    print(f"现在是{tp[i % 2]}")
    xx = input("输入棋子X轴值（从1开始）")
    yy = input("输入棋子Y轴值（从1开始）")
    x = int(xx) - 1
    y = int(yy) - 1
    if ((x < 0) or (x > 2)) or ((y < 0) or (y > 2)):
        ir = 1
        continue
    if list[x][y] == ' ':
        list[x][y] = tp[i % 2]
        ir = 0
    else:
        ir = 1
        continue
    i += 1
    flag = win(list, x, y)
    # 特殊情况判断
    if flag == 1:
        print(f"{tp[(i - 1) % 2]}赢了")
        bk = f"{list[0][0]}  | {list[0][1]} |  {list[0][2]}\n___|___|___\n   |   |   \n{list[1][0]}  | {list[1][1]} |  {list[1][2]}\n___|___|___\n   |   |   \n{list[2][0]}  | {list[2][1]} |  {list[2][2]}"
        print(bk)
        break
    if (i == 9) and (flag == 0):
        print("平局")
        break


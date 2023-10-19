import os
def choose_mode():
    mode = int(input("请输入下棋模式，删除(1)或者下棋(2)"))
    return mode


def score_enough(score):
    if score[0] <= 0:
        return 2
    elif score[1] <= 0:
        return 1
    else:
        return 0


def print_score(data):
    print(f"当前积分:\n玩家1 {data[0]}\n玩家2 {data[1]}")


def print_table(data):
    table = (f"{data[0][0]}  | {data[0][1]} |  {data[0][2]}\n___|___|___\n   |   |   \n{data[1][0]}  | {data[1][1]} |  {data[1][2]}\n___|___|___\n   |   |   "
          f"\n{data[2][0]}  | {data[2][1]} |  {data[2][2]}")
    print(table)


# 引用的清屏函数
def clear_screen():
    if os.name == 'posix':
        # Unix/Linux/MacOS
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        # Windows
        os.system('cls')


# 判断输赢
def is_win(data, x ,y):
    if data[0][y] == data[1][y] == data[2][y]:
        return 1
    elif data[x][0] == data[x][1] == data[x][2]:
        return 1
    elif (data[0][0] == data[1][1] == data[2][2]) or (data[0][2] == data[1][1] == data[2][0]) and (not data[1][1] == ' '):
        return 1
    else:
        return 0


#判断数字函数
def is_num(str):
    if str[0] == '0':
        return 0
    for i in str:
        if i < '0' or i > '9':
            return 0
    return 1


def score_input(player_score):
    score_enough = False
    score_isnum = False
    while(score_isnum == False or score_enough == False):
        score_start = input("请输入一局所需积分:")
        if not is_num(score_start):
            # clear_screen()
            score_isnum = False
            print("非法输入,请重试")
        else:
            score_isnum = True
        score_start = int(score_start)
        if score_start > player_score[0] or score_start > player_score[1]:
            # clear_screen()
            score_enough = False
            print("积分不足,请重试")
        else:
            score_enough = True
    return score_start


def input_position(postype):
    while True:
        pos = input(f"请输入{postype}轴坐标:")
        if is_num(pos):
            if 1 <= int(pos) <= 3:
                break
            else:
                clear_screen()
                print("请输入合法坐标")
                continue
        else:
            clear_screen()
            print("请输入数字")
            continue
    return int(pos) - 1
def main():
    # 开始界面
    print("井字棋")
    # 初始化状态
    ir = 0
    chess_data = [[' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
    tp = ['O', 'X']
    i = 0
    win = 0
    player_score = [100, 100]
    # 主要部分
    while player_score[0] > 0 and player_score[1] > 0:
        print_score(player_score)
        score = score_input(player_score)
        while(win == 0):
            clear_screen()
            print_score(player_score)
            print_table(chess_data)
            print(f"现在是{tp[i % 2]}")
            # 检查是否可以删除
            xx = input_position("x")
            yy = input_position("y")
            # 排除重复情况
            if chess_data[xx][yy] != ' ' and i < 7:
                clear_screen()
                print("非法输入")
                continue
            if i >= 7:
                mode = choose_mode()
                if mode == 2:
                    if chess_data[xx][yy] != ' ':
                        clear_screen()
                        print("非法输入")
                        continue
                    else:
                        chess_data[xx][yy] = tp[i % 2]
                elif mode == 1:
                    if chess_data[xx][yy] == ' ':
                        clear_screen()
                        print("非法输入")
                        continue
                    else:
                        chess_data[xx][yy] = ' '
            else:
                chess_data[xx][yy] = tp[i % 2]
            i += 1
            win = is_win(chess_data, xx, yy)
            # 特殊情况判断
            if win == 1:
                print(f"{tp[(i - 1) % 2]}赢了")
                player_score[(i - 1) % 2] += score
                player_score[i % 2] -= score
                print_table(chess_data)
                input('输入任意键继续')
                clear_screen()
                break
        if score_enough(player_score):
            print(f"玩家{score_enough(player_score)}赢了")
            clear_screen()
            break
    print("游戏结束")
main()
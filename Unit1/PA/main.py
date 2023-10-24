import os

# 判断是否平局
def is_stop(data):
    for i in data:
        for j in i:
            if j == ' ':
                return False
    else:
        return True
# 判断异常情况
def print_special(situation):
    sit = ["请输入合法数字", "请输入在范围内的位置", "积分不足"]
    print(sit[situation])


# 检测两人积分是否足够
def score_enough(score):
    if score[0] <= 0:
        return 2
    elif score[1] <= 0:
        return 1
    else:
        return 0


# 输出积分
def print_score(data):
    print(f"当前积分:\n玩家1 {data[0]}\n玩家2 {data[1]}")


# 输出棋盘
def print_table(data):
    table = (f"{data[0][0]}  | {data[0][1]} |  {data[0][2]}\n___|___|___\n   |   |   "
             f"\n{data[1][0]}  | {data[1][1]} |  {data[1][2]}\n___|___|___\n   |   |   "
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
def is_win(data, x, y):
    if data[0][y] == data[1][y] == data[2][y]:
        return 1
    elif data[x][0] == data[x][1] == data[x][2]:
        return 1
    elif ((data[0][0] == data[1][1] == data[2][2]) or (data[0][2] == data[1][1] == data[2][0])
          and (not data[1][1] == ' ')):
        return 1
    else:
        return 0


# 判断数字函数
def is_num(st):
    if st[0] == '0':
        return 0
    for i in st:
        if i < '0' or i > '9':
            return 0
    return 1


# 输入分数
def score_input(player_score):
    score_is_enough = False
    score_is_num = False
    score_start = 0
    while (not score_is_num) or (not score_is_enough):
        score_start = input("请输入一局所需积分:")
        if not is_num(score_start):
            # clear_screen()
            score_is_num = False
            print("非法输入,请重试")
            continue
        else:
            score_is_num = True
        score_start = int(float(score_start))
        if (score_start > player_score[0]) or (score_start > player_score[1]):
            # clear_screen()
            score_is_enough = False
            print("积分不足,请重试")
            continue
        else:
            score_is_enough = True
    return score_start


# 输入目标位置
def input_position():
    while True:
        pos = input(f"请输入位置:")
        if is_num(pos):
            if 1 <= int(pos) <= 9:
                break
            else:
                clear_screen()
                print("请输入合法坐标")
                continue
        else:
            clear_screen()
            print("请输入数字")
            continue
    return int(pos)


def main():
    # 开始界面
    print("井字棋\n自制井字棋游戏，有积分限制，特殊模式在7回合之后可以选择删除棋子\n请按任意键继续")
    input()
    clear_screen()
    player_score = [100, 100]
    # 主要部分
    while player_score[0] > 0 and player_score[1] > 0:
        # 初始化状态
        chess_data = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        movement = [[], []]
        _tp = ['O', 'X']
        turns = 0
        # 输出当前玩家积分状态
        print_score(player_score)
        score = score_input(player_score)
        win = 0
        mode = int(input("请输入游戏模式，普通模式1 或者 特殊模式2\n"))
        while win == 0:
            # 输出当前选手信息
            clear_screen()
            print_score(player_score)
            print_table(chess_data)
            print(f"现在是{_tp[turns % 2]}\n是第{turns + 1}回合")
            # 在7回合之后删除
            if turns >= 6 and mode == 2:
                print(f"删除第{movement[turns % 2][0] + 1}个棋\n输入任意键继续")
                input()
                target_back = movement[turns % 2][0]
                back_x = target_back // 3
                back_y = target_back % 3
                chess_data[back_x][back_y] = ' '
                movement[turns % 2].pop(0)
                clear_screen()
                print_table(chess_data)
            # 输入目标位置
            pos = int(input_position()) - 1
            pos_x = pos // 3
            pos_y = pos % 3
            # 排除特殊情况
            if chess_data[pos_x][pos_y] != ' ' and turns < 7:
                clear_screen()
                print("非法输入")
                continue
            # 记录步骤
            movement[turns % 2].append(pos)
            # 落子
            chess_data[pos_x][pos_y] = _tp[turns % 2]
            turns += 1
            # 判断输赢
            win = is_win(chess_data, pos_x, pos_y)
            if win == 1:
                print(f"{_tp[(turns - 1) % 2]}赢了")
                player_score[(turns - 1) % 2] += score
                player_score[turns % 2] -= score
                print_table(chess_data)
                input('输入任意键继续')
                clear_screen()
                break
            # 判断平局
            if is_stop(chess_data):
                print("平局")
                input('输入任意键继续')
                clear_screen()
                break
        # 判断分数是否足够
        if score_enough(player_score):
            print(f"玩家{score_enough(player_score)}赢了")
            clear_screen()
            break
    print("游戏结束")


main()

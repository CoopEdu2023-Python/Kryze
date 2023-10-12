def cal(num1, num2, op):
    if op == "addition":
        return num1 + num2
    elif op == "subtraction":
        return num1 - num2
    elif op == "multiplication":
        return num1 * num2
    elif op == "division":
        return num1 / num2
    else:
        return "非法符号"
def check(a):
    if len(a) > 1 and a.find('-', 1, len(a) - 1):
        print(1)
        return False
    if len(a) > 1 and a[0] == '0':
        print(2)
        return False
    for i in a:
        if (i < '0' or i > '9') and (not i == '.'):
            # print(3)
            return False
    return True
while(True):
    n1 = input("请输入第一个数")
    n2 = input("请输入第二个数")
    op = input("请输入操作符号")
    if (not check(n1)) or (not check(n2)):
        print("非法输入")
        continue
    n1 = float(n1)
    n2 = float(n2)
    if op == "division" and n2 == 0:
        print("除数不为0")
        continue
    else:
        print(cal(n1, n2, op))
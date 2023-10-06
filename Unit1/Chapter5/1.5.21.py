def check(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return False
    return True
def form(num, dig, v):
    if dig >= 5:
        return
    if dig == 4 and check(num):
        for i in range(1, 4):
            print(num[i], end = "")
        print("\n")
    else:
        num[dig] = v
        for i in range(1, 5):
            form(num, dig + 1, i)
n = [0, 0, 0, 0, 0]
form(n, 0, 0)
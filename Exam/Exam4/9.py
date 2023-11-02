str1 = input()
str2 = input()
if len(str1) > len(str2):
    str2 = '0' * (len(str1) - len(str2)) + str2
else:
    str1 = '0' * (len(str2) - len(str1)) + str1
digits_1 = []
digits_2 = []
digits_3 = []
for i in range(max(len(str1), len(str2)) - 1, -1, -1 ):
    digits_1.append(int(str1[i]))
    digits_2.append(int(str2[i]))
# print(digits_1, digits_2)
add_point = 0
for i in range(len(digits_1)):
    digits_3.append((digits_1[i] + digits_2[i] + add_point) % 10)
    add_point = (digits_1[i] + digits_2[i] + add_point) // 10
if add_point:
    digits_3.append(add_point)
for i in range(len(digits_3) - 1, -1, -1):
    print(digits_3[i], end='')
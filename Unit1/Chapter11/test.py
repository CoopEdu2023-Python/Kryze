def hanoi(n):
	if n == 1:
		return 1
	else:
		return hanoi(n - 1) * 2 + 1


print(hanoi(5))
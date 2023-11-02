s = input()
k = int(input())
parts = []
_mid = ''
for i in range(1, len(s) + 1):
    if i % (2 * k + 1) == 0:
        parts.append(_mid)
        _mid = ''
        _mid += s[i - 1]
    else:
        _mid += s[i - 1]
parts.append(_mid)
# print(parts)
for i in parts:
    rev_parts = i[k - 1::-1]
    print(rev_parts + i[k::],end='')
def check(score):
    return score >= 0 and score <= 100
s = 0
i = 1
while i <= 30:
    r = int(input())
    while not check(r):
        print("Invalid score, please enter again")
        r = int(input())
    s += r
    i += 1
print(f"Input completed! The average score is {s / 30} points")
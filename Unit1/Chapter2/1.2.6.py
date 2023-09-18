pr = 13999 * 0.905
pr_N = int(13999 * 0.905)
save = 67890 + 200
rem = (int(save - (save // pr_N) * pr))
print(rem * (2 ** 12))
common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(12):
    print(f"{name[i]} has {common[i]} days in common years and {leap[i]} days in leap years")

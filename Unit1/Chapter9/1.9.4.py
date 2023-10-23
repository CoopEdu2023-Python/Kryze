def count_str(raw_str):
    output = {"letters": 0, "spaces": 0, "digits": 0, "others": 0}
    for i in raw_str:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            output["letters"] += 1
        elif i == ' ':
            output["spaces"] += 1
        elif '0' <= i <= '9':
            output["digits"] += 1
        else:
            output["others"] += 1
    return output


input_str = 'aA12 ?'
print(count_str(input_str))

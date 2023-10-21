def no_space(key_str):
    res = ""
    for i in key_str:
        if i != " ":
            res += i
    return res


def remove_space(data):
    format_data = dict()
    for key, value in data.items():
        format_data[no_space(key)] = value
    return format_data


student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print(remove_space(student_list))
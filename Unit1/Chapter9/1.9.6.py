def str_join(content, connector):
    output_str = ""
    for i in range(len(content) - 1):
        output_str += content[i] + connector
    output_str += content[-1]
    return output_str


str_6 = '123'
list_6 = ['a', 'b', 'c']
print(str_join(list_6, str_6))
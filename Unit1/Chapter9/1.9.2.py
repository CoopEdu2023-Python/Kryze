def reverse_str(raw_str):
    output_str = ""
    for i in range(len(raw_str)):
        output_str += raw_str[-(i + 1)]
    return output_str


input_str = "Hello there"
print(reverse_str(input_str))
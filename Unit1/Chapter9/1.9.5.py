import string
str_low = string.ascii_lowercase
str_upper = string.ascii_uppercase
def transform_str(raw_str):
    output_str = ""
    for i in raw_str:
        if 'a' <= i <= 'z':
            output_str += str_low[-(str_low.index(i) + 1)]
        elif 'A' <= i <= 'Z':
            output_str += str_upper[-(str_upper.index(i) + 1)]
    return output_str


input_str = 'abcABC'
print(transform_str(input_str))
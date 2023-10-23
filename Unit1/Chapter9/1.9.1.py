def is_palindrome(input_str):
    for i in range(len(input_str)):
        if input_str[i] != input_str[-(i + 1)]:
            return False
    else:
        return True


print(is_palindrome("12321"))
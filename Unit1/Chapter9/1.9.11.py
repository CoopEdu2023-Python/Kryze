def isPalindrome(s: str) -> bool:
    data = ""
    for i in s:
        if 'a' <= i <= 'z':
            data += i
        if 'A' <= i <= 'Z':
            data += i.lower()
        if i.isdigit():
            data += i
    print(data)
    return data == data[::-1]


print(isPalindrome("0P"))
def convertToTitle(columnNumber: int) -> str:
    if columnNumber <= 26:
        return chr(columnNumber + 64)
    else:
        return convertToTitle(columnNumber % 27) + convertToTitle(columnNumber // 26)

print(convertToTitle(701))
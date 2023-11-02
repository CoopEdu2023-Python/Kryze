def romanToInt(s: str) -> int:
    s += " "
    value_of_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, " ": 0}
    value = 0
    i = 0
    while i < len(s) - 1:
        if value_of_roman[s[i]] < value_of_roman[s[i + 1]]:
            value += value_of_roman[s[i + 1]] - value_of_roman[s[i]]
            i += 2
        else:
            value += value_of_roman[s[i]]
            i += 1
    return value



print(romanToInt("MCMXCIV"))
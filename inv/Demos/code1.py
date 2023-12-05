def simplify_path(path):
    stack = []
    components = path.split('/')
    for comp in components:
        if comp == '..':
            if stack:
                stack.pop()
        elif comp and comp != '.':
            stack.append(comp)
    result = '/' + '/'.join(stack)
    return result


# 验证用的代码：
path1 = "/home/"
path2 = "/a/./b/../../c/"
result1 = simplify_path(path1)
result2 = simplify_path(path2)
print(result1)  # 输出 "/home"
print(result2)  # 输出 "/c"

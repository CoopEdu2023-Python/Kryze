login_info = {'user1': ['pw1'], 'user2': ['pw3_now', 'pw2', 'pw1']}


def reset_password(username: str, password_old: str, password_new: str) -> None:
    if not username in login_info.keys():
        print("User not include")
        return
    if password_old != login_info[username][0]:
        print("Wrong password!")
        return
    elif len(password_new) < 8:
        print("Illegal new password (too short)")
        return
    with_num = False
    with_letter = False
    for i in password_new:
        if i.islower() or i.isupper():
            with_letter = True
        if '0' <= i <='9':
            with_num = True
    if with_num == False or with_letter == False:
        print("Illegal new password (without numbers or letters)")
        return
    else:
        print('done')
        if len(login_info[username]) < 3:
            login_info[username].insert(0, password_new)
        else:
            login_info[username].pop(-1)
            login_info[username].insert(0, password_new)
        print(login_info)


username = input()
password_old = input()
password_new = input()
# print(username, password_old, password_new)
reset_password(username, password_old, password_new)
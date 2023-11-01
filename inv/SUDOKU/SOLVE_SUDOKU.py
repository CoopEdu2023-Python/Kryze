def make_data(raw_str):
    return raw_str.split(" ")


def input_data(num_data):
    for i in range(1):
        raw_input = input()
        _dat = make_data(raw_input)
        for key in _dat:
            if key == '?':
                num_data[i].append(-1)
            else:
                num_data[i].append(int(key))


def create_prob(data):
    prob_data = []
    pro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        for j in range(9):
            if data[i][j] == -1:
                prob_data[i][j].append(pro)
            else:
                prob_data[i][j].append(data[i][j])
    return prob_data


def search_line(pos_x, pos_y, data):
    target = data[pos_x][pos_y][0]
    for i in range(len(data[pos_x])):
        if data[pos_x][i].find(target) != -1:
            data[pos_x][i].pop(data[pos_x][i].index(target))


num_data = [[[] * 9] * 9]
input_data(num_data)
data_prob = create_prob(num_data)
print(num_data)


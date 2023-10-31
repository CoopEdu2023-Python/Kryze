raw_data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
trans_data = list(reversed(raw_data))
rotated_data = list(zip(*trans_data))
print(rotated_data)
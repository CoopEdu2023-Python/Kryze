import random

def random_grouping(people, num_groups):
    # 首先，将人员列表随机排序
    random.shuffle(people)

    # 计算每组的平均人数和余下的人数
    avg_group_size = len(people) // num_groups
    remaining_people = len(people) % num_groups

    # 初始化分组
    groups = []

    # 循环创建每个组
    start_index = 0
    for i in range(num_groups):
        # 计算当前组的人数
        group_size = avg_group_size + (1 if i < remaining_people else 0)

        # 获取当前组的人员并添加到分组列表中
        group = people[start_index:start_index + group_size]
        groups.append(group)

        # 更新下一个组的起始索引
        start_index += group_size

    return groups

# 测试
people = list(range(1, 12))  # 生成1到11的人员列表
num_groups = 5
result = random_grouping(people, num_groups)
name_player = []
name_group = []

# 打印结果
for i, group in enumerate(result):
    print(f"Group {name_group[i + 1]}: {name_player[group]}")
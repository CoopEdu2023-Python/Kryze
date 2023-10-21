def remove_duplicates(data):
    seen = dict()
    for key, value in data.items():
        for j in seen.values():
            if value['name'] == j['name']:
                break
        else:
            seen[key] = value
    return seen


sample_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
   'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
   'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}
remove_duplicates(sample_data)
print(remove_duplicates(sample_data))
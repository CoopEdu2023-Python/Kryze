def del_str(target_str, remove_list):
    output_str = ""
    for i in target_str:
        if remove_list.find(i) == -1:
            output_str += i
    return output_str


text = "They are students."
remove = "aeiou"
print(del_str(text, remove))
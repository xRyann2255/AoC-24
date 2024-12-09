f = open("9.txt").read().strip()
print(len(f))
print(f[-1])

def convert_file(f):
    converted_file = []
    for i in range(len(f)):
        if i % 2 == 0:
            converted_file += [str((i // 2))] * int(f[i])
        else:
            converted_file += ["."] * int(f[i])
    return converted_file

def compact_file(char_list):
    idx = 0
    for i in range(len(char_list) - 1, -1, -1):
        if char_list[i] == ".":
            continue
        while idx < len(char_list) and char_list[idx] != ".":
            idx += 1
        if i < idx:
            break
        char_list[i], char_list[idx] = char_list[idx], char_list[i]
    while char_list[-1] == ".":
        char_list.pop()
    return char_list

answer = 0

file_system = compact_file(convert_file(f))
print(file_system)
for i in range(len(file_system)): 
    answer += i * int(file_system[i])

print(answer)

# Part 2

answer = 0

def convert_file_2(f):
    converted_file = []
    for i in range(len(f)):
        if i % 2 == 0:
            converted_file.append([str((i // 2))] * int(f[i]))
        else:
            converted_file.append(["."] * int(f[i]))
    return converted_file

def compact_file_2(converted_file):
    idx = 0
    for i in range(len(converted_file) -1, -1, -1):
        if converted_file[i][0] == ".":
            continue
        idx = 0
        while idx < i and (converted_file[idx][0] != "." or len(converted_file[idx]) < len(converted_file[i])):
            idx += 1
        if len(converted_file[idx]) == len(converted_file[i]):
            converted_file[idx], converted_file[i] = converted_file[i], converted_file[idx]
        elif len(converted_file[idx]) > len(converted_file[i]):
            space = len(converted_file[idx])
            converted_file[idx], converted_file[i] = converted_file[i], ["."] * len(converted_file[i])
            converted_file.insert(idx + 1, ["."] * (space - len(converted_file[i])))
    return [elem for group in converted_file for elem in group]

file_system = compact_file_2(convert_file_2(f))
for i in range(len(file_system)): 
    if file_system[i] != ".":
        answer += i * int(file_system[i])
print(file_system)
print(answer)
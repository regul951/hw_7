file_list = ['1.txt', '2.txt', '3.txt']

lenght_file = {}
for file in file_list:
    with open(file, 'r', encoding='utf-8') as f:
        lenght_file[file] = len(f.readlines())

sorted_lenght_file = sorted(lenght_file.items(), key=lambda x: x[1])

with open('result.txt', 'a', encoding='utf-8') as f:
    f.truncate(0)
    for file in sorted_lenght_file:
        with open(file[0], 'r', encoding='utf-8') as f_sorted:
            f.write(f_sorted.name + '\n' + str(file[1]) + '\n')
            for line in f_sorted.readlines():
                f.write(line)
            f.write('\n')

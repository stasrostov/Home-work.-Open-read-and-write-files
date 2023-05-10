file1_name = '1.txt'
file2_name = '2.txt'
file3_name = '3.txt'
result_file = 'Result.txt'
files_list = [file1_name, file2_name, file3_name]
files_dict = {}


def lines_counter(file_obj):
    with open(file_obj, encoding='utf-8') as document:
        data = str(len(document.readlines()))
        return data


for file in files_list:
    with open(file, encoding='utf-8') as f:
        files_dict[file] = [lines_counter(file), f.read()]

sorted_keys = sorted(files_dict, key=files_dict.get)
sorted_dict = {}

for element in sorted_keys:
    sorted_dict[element] = files_dict[element]

with open(result_file, 'a', encoding='utf-8') as f:
    for key, value in sorted_dict.items():
        f.write(key)
        f.write('\n')
        f.write(value[0])
        f.write('\n')
        f.write(value[1])
        f.write('\n')

import os

path_text = input('Enter the path (with spaces between folder names): \n').split()
path = str()
if path_text is None:
    path = path + 'C:\\'
else:
    for i in range(len(path_text)):
        if i == 0:
            path = path + path_text[0] + ':\\'
        else:
            path += path_text[i] + '\\'


def counter_func(path_f):
    substring = '.py'
    for address, subdirectories, file_names in os.walk(path_f):
        for file_name in file_names:
            if substring in file_name:
                absolute_path = os.path.join(path_f, file_name)
                with open(absolute_path, 'r', encoding='utf-8') as py:
                    amount = 0
                    for string in py:
                        if string != '\n' and string[0] != '#':
                            amount += 1
# yield [file_name, amount]
            yield amount


summa = 0
strings_in_files = counter_func(path)
while True:
    try:
        summa += next(strings_in_files)
    except StopIteration:
        break
print(summa)

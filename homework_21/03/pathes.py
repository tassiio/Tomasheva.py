import os


def gen_files_path(path_f, catalogue):
    for address, folders_list, file_names in os.walk(path_f):
        for file in file_names:
            yield address + '\\' + file
            if address.split('\\')[-1] == catalogue:
                return StopIteration, 'Found'


path_text = input('Enter the path (with spaces between folder names): \n').split()
catalogue_name = input('Enter the name of catalogue you need: ')
# path = Path(*path_text)
path = str()
if path_text is None:
    path = path + 'C:\\'
else:
    for i in range(len(path_text)):
        if i == 0:
            path = path + path_text[0] + ':\\'
        else:
            path += path_text[i] + '\\'

gen = gen_files_path(path, catalogue_name)
while True:
    print(next(gen))

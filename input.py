# Unit 1

from sys import argv

files_names = []
files_set_name = []

# check for files and their correspond set names
if len(argv) % 2 == 0:
    raise Exception("invalid inputs!")

if len(argv)-1 > 20:
    raise Exception("too many inputs!")

for i in range(1, len(argv), 2):
    files_names.append(argv[i])
    files_set_name.append(argv[i+1])

print(files_names)
print(files_set_name)

#!/usr/bin/python3

from sys import argv 
import myParser


files_names = [argv[1], argv[3], argv[5]]
files_set_name = [argv[2], argv[4], argv[6]]

'''
counter = 1
while True:
    line = input(f"Enter {counter} files name: ")
    if line != "":
        files_names.append(line)
    else:
        break
    line = input(f"Enter {counter} files name for set: ")
    if line != "":
        files_set_name.append(line)
    else:
        break
    counter += 1
'''

sets = dict()
for element in files_names:
    with open(element, encoding="utf8") as f:
        content = f.readlines()

    w = myParser.Processor(content)

    w.remove_backslash_n()
    #w.show()

    w.find_divided_word_into_two_consecutive_lines()
    #w.show()


    w.replace_parentheses_with_space()
    w.replace_tilda_with_space()
    w.replace_black_circle_with_space()
    w.replace_braces_with_space()
    w.replace_dot_comma_with_space()
    w.replace_colon_semicolon_with_space()
    #w.show()

    w.breakdown_to_words()

    #w.key()

    w.find_abreviations()

    #w.abr()

    #w.key()

    w.toLower()

    w.remove_numbers()
    w.remove_one_length_words()
    #w.remove_To_Be_words()
    #w.remove_conjunctions()
    #w.remove_prepositions()
    #w.remove_pronouns()
    #w.remove_uncategorized()

    diction = dict()
    data = w.key()
    for word in data:
        diction[word] = data.count(word)
    index = files_names.index(element)
    sets[files_set_name[index]] = diction

# find union of all sets
u = set()
for key in sets:
    individualSet = set(sets[key].keys())
    u = u.union(individualSet)

# find prime of each set and put them with OG sets
set_of_words = dict()
for key in sets:
    keys = set(sets[key].keys())
    prime = u - keys
    index = files_set_name.index(key)
    set_of_words[f"-{files_set_name[index]}"] = prime

for key in sets:
    the_set = set(sets[key].keys())
    set_of_words[key] = the_set

# make different combination for sets
states = []
n = len(files_names)
for i in range(2**n):
    bits = []
    for j in range(1, n+1):
        if int(i/(2**(n-j))) % 2 == 0:
            bits.append("0")
        else:
            bits.append("1")
    states.append("".join(bits))


for case in states:
    shelf = []
    txt_char = []
    for i in range(len(case)):
        if case[i] == "1":
            txt_char.append(files_set_name[i])
            shelf.append(files_set_name[i])
        else:
            txt_char.append(f"-{files_set_name[i]}")
            shelf.append(f"-{files_set_name[i]}")
    txt_name = "".join(txt_char)
    # ignore full prime set like: -A-B
    try:
        if len(txt_name) / txt_name.count("-") == 2:
            continue
    except:
        pass
    words = set_of_words[shelf[0]]
    for key in shelf[1:]:
        words = words.intersection(set_of_words[key])
    with open(txt_name, "w") as f:
        for word in words:
            f.write(word+"\n")

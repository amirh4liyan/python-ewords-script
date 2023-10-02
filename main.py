#!/usr/bin/python3

import time
import myParser
from sys import argv 


files_names = [argv[1], argv[3], argv[5]]
files_set_name = [argv[2], argv[4], argv[6]]


dictionary = dict()
for element in files_names:
    print(element)
    t0 = time.time()
    with open(element, encoding="utf8") as f:
        content = f.readlines()

    t1 = time.time()
    print("read file: ", t1 - t0)
    p = myParser.Parser(content)

    t2 = time.time()
    print("make object: ", t2 - t1)
    p.remove_backslash_n()

    t3 = time.time()
    print("remove \\n: ", t3 - t2)
    # this should be done before clearing tilda from text
    p.find_the_broken_word_between_two_consecutive_lines()

    t4 = time.time()
    print("find broken words: ", t4 - t3)
    # remove some junk symbols
    p.replace_parentheses_with_space()
    p.replace_tilda_with_space()
    p.replace_black_circle_with_space()
    p.replace_square_braces_with_space()
    p.replace_curly_braces_with_space()
    p.replace_dot_comma_with_space()
    p.replace_colon_semicolon_with_space()

    t5 = time.time()
    print("remove junk symbols: ", t5 - t4)
    # parsing line to words
    p.breakdown_to_words()

    t6 = time.time()
    print("breakdown to words: ", t6 - t5)
    '''
      pull abreviation words from text, this sould be done before con-
      vert words to lower case
    '''
    p.find_abreviations()
    # show abreviation words
    # p.abr()

    t7 = time.time()
    print("abr: ", t7 - t6)
    # convert all words to lowe case
    p.toLower()

    t8 = time.time()
    print("to lower: ", t8 - t7)
    # remove some strings that not regarding as word
    p.remove_numbers()
    p.remove_one_length_words()
    #p.remove_To_Be_words()
    #p.remove_conjunctions()
    #p.remove_prepositions()
    #p.remove_pronouns()
    #p.remove_uncategorized()

    t9 = time.time()
    print("remove non words: ", t9 - t8)
    diction = dict()
    t10 = time.time()
    print("get words from lines ", t10 - t9)
    for word in p.key():
        if word in diction:
            diction[word] += 1
        else:
            diction[word] = 1
    t11 = time.time()
    print("counting words ", t11 - t10)
    index = files_names.index(element)
    dictionary[files_set_name[index]] = diction


# find union of all sets
u = set()
for key in dictionary:
    individualSet = set(dictionary[key].keys())
    u = u.union(individualSet)

# find prime of each set and put them with OG sets
set_of_words = dict()
for key in dictionary:
    keys = set(dictionary[key].keys())
    prime = u - keys
    index = files_set_name.index(key)
    set_of_words[f"-{files_set_name[index]}"] = prime

for key in dictionary:
    the_set = set(dictionary[key].keys())
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

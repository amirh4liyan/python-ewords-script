import argparse

# make parser object
parser = argparse.ArgumentParser()


# add arguments here:
parser.add_argument('path', help='the base')
parser.add_argument('-a', '--alphabetic', action='store_true',
                        help='alphabetic order while sorting')
parser.add_argument('-r', '--reverse', action='store_true',
                        help ='reverse order while sorting')
parser.add_argument('-o', '--output',
                        help='place the output there by <name>.txt')
parser.add_argument('-l', '--length',
                        help='define limit for the words')


# get data from command-line with parse_arge() method
args = parser.parse_args()
filePath = args.path
isAlpha = args.alphabetic
isReverse = args.reverse
outputName = args.output

lLength = 3
rLength = 16
if args.length:
    l = args.length[:args.length.index(':')]
    if l:
        lLength = int(args.length[:args.length.index(':')])

    r = args.length[args.length.index(':')+1:]
    if r:
        rLength = int(args.length[args.length.index(':')+1:])

def compareAlpha(x, y):
    a, b = x, y
    if len(x) > len(y):
        a, b = b, a
    answer = a
    for i in range(len(a)):
        ordX = ord(a[i])
        ordY = ord(b[i])
        if ordX == ordY:
            continue
        elif ordX < ordY:
            break
        elif ordX > ordY:
            answer = b
            break
    if answer == y:
        return True
    elif answer == x:
        return False

def swap(i):
    keys[i], keys[i-1] = keys[i-1], keys[i]
    values[i], values[i-1] = values[i-1], values[i]

def sortByAlpha():
    a = len(keys)
    for j in range(a):
        for i in range(a-1, 0, -1):
            # if second was closer, return True, else will return False
            if compareAlpha(keys[i-1], keys[i]):
                swap(i)

def sortByRepeat():
    a = len(values)
    for j in range(a):
        for i in range(a-1, 0, -1):
            if values[i] > values[i-1]:
                swap(i)

keys = []
values = []
with open(filePath) as f:
    while True:
        line = f.readline().strip()

        if line == '':
            break  

        key, value = line.split()
        if lLength <= len(key) <= rLength:
            keys.append(key)
            values.append(int(value))
        
if isAlpha:
    sortByAlpha()
else:
    sortByRepeat()
if isReverse:
    keys.reverse()
    values.reverse()

print()
NI = len(max(keys, key=len)) + 4
for i in range(len(values)):
    key = keys[i]
    val = values[i]
    padding = NI - len(key)
    print('%s'%key + padding*' ' + '%d'%val)


if outputName:
    with open(outputName, "w") as f:
        for i in range(len(keys)):
            key = keys[i]
            val = values[i]
            padding = NI - len(key)
            f.write('%s'%key + padding*' ' + '%d'%val+'\n')
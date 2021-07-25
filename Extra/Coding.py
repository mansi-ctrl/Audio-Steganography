import queue as Queue

cntr = 0 #total nodes in the tree


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()
    print('Freq = ',freq)
    for key in freq:
        print('Key = ',key,' and f = ',freq[key])
        newNode = Node(freq[key], key)
        x = (freq[key], key, newNode)
        print('node data = ',newNode.data,' and freq = ',newNode.freq,' and count = ',newNode._count,' and total counter = ',cntr)
        q.put(x)

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    print('In decodehuff and root = ',root,' and s = ',s)
    root2 = root
    for i in s:
        if (i == '0'):
            root = root.left
        else:
            root = root.right

        if (root.left == root.right == None):
            print(root.data, end='')
            root = root2

#INPUT
#ip = input()
ip = "abbcccdddd"

#FREQUENCIES
freq = {}  # Create an empty dictionary and map each character to its frequency

cntr = 0
print('\tMaking frequency dictionary')
for ch in ip:
    if (freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1
    print('f = ',freq)


#MAKING TREES
root = huffman_hidden()  # contains root of huffman tree

code_hidden = {}  # contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:  # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""
print('Code = ',code_hidden)
for ch in ip:
    toBeDecoded += code_hidden[ch]
print('To be decoded = ',toBeDecoded)
#The final message to be be sent is toBeDecoded


decodeHuff(root, toBeDecoded)

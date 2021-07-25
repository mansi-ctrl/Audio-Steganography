import queue as Queue
import  Frequency as f
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


def huffman_hidden(freq):  # builds the tree and returns root
    q = Queue.PriorityQueue()
    #print('in huffman hidden')
    #print('Freq = ',freq)
    for key in freq:
        #print('Key = ',key,' and f = ',freq[key])
        newNode = Node(freq[key], key)
        x = (freq[key], key, newNode)
        #print('node data = ',newNode.data,' and freq = ',newNode.freq,' and count = ',newNode._count,' and total counter = ',cntr)
        q.put(x)
    #print('queue size = ',q.qsize())
    #print('Queue empty? - ', q.empty())

    while q.qsize() != 1:
        #print('queue size = ', q.qsize())
        a = q.get()
        b = q.get()
        #print('a = ',a,' and b = ',b)
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    #print('root[2] = ',root)

    return root


def dfs_hidden(obj, already, code_hidden):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1", code_hidden)
    dfs_hidden(obj.left, already + "0",code_hidden)


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

def encode(ip):
    # FREQUENCIES
    cntr, freq = f.frequency(ip)
    # MAKING TREES
    root = huffman_hidden(freq)  # contains root of huffman tree
    code_hidden = {}  # contains code for each object
    dfs_hidden(root, "",code_hidden)

    if len(code_hidden) == 1:  # if there is only one character in the i/p
        for key in code_hidden:
            code_hidden[key] = "0"

    #print('Initial codes = ',code_hidden)
    toBeDecoded = ""
    #l = f.getMaxL(freq)
    #print(' l = ',l)
    for ch in ip:
        #print('ch = ',ch,' and code = ',code_hidden[ch])
        #length = len(code_hidden[ch])
        #print('length = ',length)
        #if length < l:
            #code_hidden[ch] +=  code_hidden[ch]
            #print('Changed code = ',code_hidden[ch])
        toBeDecoded += code_hidden[ch]
        #print('ToBeDecoded  = ',toBeDecoded)

    # The final message to be be sent is toBeDecoded
    #print('Code = ', code_hidden,' and to be decoded = ',toBeDecoded)
    print('\n\t\tYour message is successfully compressed')
    return toBeDecoded, code_hidden, freq, cntr
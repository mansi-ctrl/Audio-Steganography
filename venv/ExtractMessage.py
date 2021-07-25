import  Reciever as reciever
import Decoding as decode
import Encoding as encode
import queue as Queue
cntr = 0
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

def findRoot(key):
    f = open("demo.txt", "r")
    for line in f:
        # print(line)
        if line[:len(key)] == key:
            #print('In decoding, Key = ',key,' is found')
            f.close()
            return line
    f.close()
    return None

def extractMessage(key, newFilePath):
    findKeyResult = findRoot(key)
    if findKeyResult != None:
        compressedMessage = reciever.extract(newFilePath)
        #decode.decodeHuff()
        return findKeyResult, compressedMessage
    else:
        return None

def convertToDictionary(line):
    #print('Line is :',line)
    codes = line.split(' ')
    codes = codes[:len(codes)-1]
    #print('Codes = ',codes,' and length = ',len(codes))
    codeDictionary = {}
    while(len(codes) > 0):
        codeDictionary[codes[0]] = int(codes[1])
        codes = codes[2:]
        #print(codes)
    print('Code dictionary = ',codeDictionary)
    return codeDictionary

def convertToTree(freq):
    q = Queue.PriorityQueue()
    #print('in huffman hidden')
    #print('Freq = ',freq)
    for key in freq:
        #print('Key = ',key,' and f = ',freq[key])
        newNode = Node(freq[key], key)
        x = (freq[key], key, newNode)
        #print('node data = ',newNode.data,' and freq = ',newNode.freq,' and count = ',newNode._count,' and total counter = ',cntr)
        q.put(x)
    #print('queue size = ', q.qsize())
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
    # print('root[2] = ',root)

    return root


#key = "01"
#filePath = "60HzNew.wav"
#key = "02"
#filePath = "50HzNew.wav"
key = "03"
filePath = "preambleNew.wav"
message, compressedMessage = extractMessage(key,filePath)
print('key line = ',message)
if message != None:
    msg = message[len(key) + 1:]
    c = 0
    #print('initial msg = ',msg)
    while msg[c] != ' ':
        c += 1
    c +=1
    msg = msg[c:]
    #print('c = ',c,'final msg = ',msg)
    freq = convertToDictionary(msg)
    root = convertToTree(freq)
    print('Extracted message:')
    decode.decodeHuff(root, compressedMessage)
    #code = convertToDictionary(message[len(key) + 1:])
    #print(decode.decodeCompressed(code, message))
    print('\n\n\tMESSAGE EXTRACTED SUCCESSFULLY...')
else:
    print('Key ',key,' does not exist.\nPlease enter again....')

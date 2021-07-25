
def decodeHuff(root, s):
    #print('In decodehuff and root = ',root,' and s = ',s)
    root2 = root
    for i in s:
        if (i == '0'):
            root = root.left
        else:
            root = root.right

        if (root.left == root.right == None):
            print(root.data, end='')
            root = root2

def decodeCompressed(code, codemessage):
    tmp = ""
    for codeValue in code.values():
            got = True
            i = 0
            for ch in codeValue:
                print(ch)
                if(ch != codemessage[i]):
                    got  =False
                    break
                i+=1
            if got:
                print('Got = ',codeValue)
                tmp += codeValue
                codemessage = codemessage[len(codeValue)-1:]
                print('tmp = ',tmp,' codemsg = ',codemessage)
                break

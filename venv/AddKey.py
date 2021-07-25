def addKey(key, codeList, freq, cntr):
    f = open("demo.txt", "r")
    for line in f:
        #print(line)
        if line[:len(key)] == key and line[len(key)] == ' ':
            #print('Key = ',key,' is found')
            f.close()
            return False
    f.close()

    #s = key+" "
    #for code in codeList:
        #print('code = ',code)
        #s += code+" "+codeList[code]+" "
#    s += "\n"
#    print('s = '+s)
#    f = open("demo.txt", "a+")
#    f.write(s)
#    f.close()
    s = key + " " + str(cntr) + " "
    for ch in freq:
        # print('code = ',code)
        s += ch + " " + str(freq[ch]) + " "
    s += "\n"
    print('s = ' + s)
    f = open("demo.txt", "a+")
    f.write(s)
    f.close()
    return True
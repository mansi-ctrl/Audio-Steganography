#FREQUENCIES
def bin(n):
    m = ""
    #print('n = ', n)
    while n > 0:
        m = str(n % 2) + m
        n = n // 2
        #print('s = ', m, ' and n = ', n)
    return m



def getMaxL(f):
    max = -1
    for i in f.values():
        #print('value = ',i)
        if i > max:
            max = i
        #print('max = ', max)
    max = bin(max)
    x = len(max)
    #print('Bit length = ',x)
    #print('Binary max = ',max,' and length = ',len(max))
    return x

def frequency(ip):

    freq = {}  # Create an empty dictionary and map each character to its frequency
    cntr = 0

    for ch in ip:
        if (freq.get(ch) == None):
            freq[ch] = 1
        else:
            freq[ch] += 1 
    #print('f = ',freq,' and cntr = ',cntr)
    x = getMaxL(freq)
    return cntr,freq
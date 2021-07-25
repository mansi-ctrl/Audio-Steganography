def bin(n):
    m = ""
    print('n = ', n)
    while n > 0:
        m = str(n % 2) + m
        n = n // 2
        print('s = ', m, ' and n = ', n)
    return m


# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    print('s = ', s)
    return [('a', 4), ('b', 1), ('c', 2)]


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(f, s):
    temp = s;
    max = f[0][1]
    for i in f:
        if i[1] > max:
            max = i[1]
        print('max = ', max)
    max = bin(max)
    print('final max = ', max, ' and in binary max = ', max)
    print('freqs = ', f, ' and str = ', s)
    return "0000101111"


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    print('f = ', freqs, ' and bits = ', bits)
    return ""
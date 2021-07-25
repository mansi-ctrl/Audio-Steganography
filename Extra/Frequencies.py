def frequencies(s):
    l = []
    for i in range(len(s)):
        print('s[', i, '] = ', s[i], 'l = ', l)
        got = False
        for j in range(len(l)):
            print('i = ', i, ' and j = ', l[j])
            if s[i] == l[j][0]:
                print(l[j][0], ' and f = ', l[j][1])
                temp = (l[j][0], l[j][1] + 1)
                l[j] = temp
                print('After changing temp = ', temp, ' and l = ', l)
                got = True
        if not got:
            l += [(s[i], 1)]
            print(s[i], ' is not in list and thus l = ', l)
    return l


def bin(n):
    s = ""
    while n > 1:
       s = str(n%2) + s
       n = n//2
       print('s = ',s,' and n = ',n)
    return s
s = "aaaabbbccd"
#frequencies(s)
print(bin(15))

acm = 0
sequence = input().split(',')

for string in sequence:
    res = 0
    for char in string:
        res = ((res+ord(char))*17)%256
    print(string, res)
    acm += res

print(acm)
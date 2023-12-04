p = 0

while True:
    try:
        card, numbers = input().split(': ')
        win, own = numbers.split(' | ')
        win = list(map(int, win.split()))
        own = list(map(int, own.split()))

        n=0
        for i in own:
            if i in win:
                n+=1
                print(i, end= ' ')
        
        print(win, own, n, 2**(n-1))
        if n is not 0:
            p+=2**(n-1)


        
    except EOFError:
        break

print(p)
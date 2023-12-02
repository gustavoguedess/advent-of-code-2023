import re

total = {
    'red':12,
    'green': 13,
    'blue': 14,
}
acm=0

while True:
    try:
        game, sets = input().split(': ')
        game = int(game.replace('Game ', ''))
        
        valid=True
        sets = sets.split('; ')
        for s in sets:
            cubes = s.split(', ')
            for c in cubes:
                n, colour = c.split(' ')
                if int(n)>total[colour]:
                    valid=False
        if valid:
            acm+=game 
    except EOFError:
        break

print(acm)
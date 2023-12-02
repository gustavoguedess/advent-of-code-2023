import re

acm=0

while True:
    try:
        game, sets = input().split(': ')
        game = int(game.replace('Game ', ''))
        

        total = {'red':0,'green': 0,'blue': 0,}
        valid=True
        sets = sets.split('; ')
        for s in sets:
            cubes = s.split(', ')
            for c in cubes:
                n, colour = c.split(' ')
                total[colour] = max(int(n), total[colour])
        acm+=total['red']*total['green']*total['blue']
    except EOFError:
        break

print(acm)
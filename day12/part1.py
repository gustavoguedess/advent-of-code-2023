

def calc_possibles(spring, groups):
    try:
        f = spring.index('?')
    except ValueError:
        check_group = spring.split('.')
        check_group = list(filter(None, check_group))
        check_group = [len(x) for x in check_group]
        if check_group == groups:
            return 1
        else:
            return 0
        
    return calc_possibles(spring[:f] + '#' + spring[f+1:], groups) + calc_possibles(spring[:f] + '.' + spring[f+1:], groups)


acm = 0

while True:
    try:
        spring,groups = input().split()
        groups = list(map(int,groups.split(',')))

        possible = calc_possibles(spring, groups)
        acm += possible
        print(spring, groups, possible)
    except EOFError:
        break
print(acm)
cards = []

def check(card):
    p = 0
    for c in card['nums']:
        if c in card['win']:
            p += 1
    return p

    
while True:
    try:
        card, numbers = input().split(': ')
        card = int(card.replace('Card ',''))
        win, nums = numbers.split(' | ')
        win = list(map(int, win.split()))
        nums = list(map(int, nums.split()))

        cards.append({
            'card': card,
            'win': win,
            'nums': nums,
            'amount': 1
        }) 
    except EOFError:
        break

def print_cards():
    for card in cards:
        print(card['card'], card['win'], card['nums'], card['amount'])
    print('------------------')
print_cards()
for i in range(len(cards)):
    for j in range(check(cards[i])):
        cards[i+j+1]['amount']+=cards[i]['amount']
print_cards()

acm = 0
for card in cards:
    acm += card['amount']
print(acm)

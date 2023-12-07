from collections import Counter
cards = 'J23456789TQKA'
hands = []
while True:
    try:
        hand, bid = input().split()
        bid = int(bid)
        original_hand = hand
        counter = [c[-1] for c in Counter(hand.replace('J','')).most_common()]
        if counter == []: counter = [0]
        counter[0]+=hand.count('J') 
        strength = [cards.index(h) for h in hand]

        hands.append({
            'hand': hand,
            'bid': bid,
            'counter': counter,
            'strength': strength,
        })
    except EOFError:
        break

hands = sorted(hands, key=lambda x: (x['counter'], x['strength']))
for i in range(len(hands)):
    hands[i]['rank']=i+1
    hands[i]['score']=hands[i]['rank']*hands[i]['bid']

for hand in hands:
    print(hand)

print(sum([hand['score'] for hand in hands]))
from collections import Counter
cards = '23456789TJQKA'
hands = []
while True:
    try:
        hand, bid = input().split()
        bid = int(bid)
        original_hand = hand
        counter = [c[-1] for c in Counter(hand).most_common()]
        sorted_hand = ''.join(sorted(hand, key=lambda x: cards.index(x)+13*hand.count(x), reverse=True))
        strength = [cards.index(h) for h in hand]

        hands.append({
            'hand': hand,
            'sorted_hand': sorted_hand,
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
acm = 0

digits = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

while True:
    try:
        text = input()
        numbers = [int(i) for i in text if i.isdigit()]
        n = numbers[0]*10 + numbers[-1]
        acm += n

    except EOFError:
        break

print(acm)
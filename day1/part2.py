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
        

        i=0
        first, last = None, None
        while first is None or last is None:
            for e,v in digits.items():
                if i<len(text) and text[i:].startswith(e) and first is None:
                    first=v
                if i>0 and text[-i:].startswith(e) and last is None:
                    last=v
            # print(i, text, first, last)
            if i<len(text) and text[i].isdigit() and first is None:
                first = int(text[i])
            if i>0 and text[-i].isdigit() and last is None:
                last = int(text[-i])
            i+=1
                        
        n = first*10 + last
        print(f"{n} {text}")
        acm += n



    except EOFError:
        break

print(acm)
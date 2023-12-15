
def hash(string):
    res = 0
    for char in string:
        res = ((res+ord(char))*17)%256
    return res

def print_boxes(op, boxes):
    print(f'After "{op}":')
    for i, box in enumerate(boxes.values()):
        if len(box) > 0:
            print(f'Box {i}: {[(string, value) for string, value in box]}')
    print()

def focusing_power(boxes):
    res = 0
    for box_number, box in boxes.items():
        for i in range(len(box)):
            value = box[i][1]
            res += (box_number+1) * (i+1) * value
    return res

def main():
    sequence = input().split(',')
    boxes = {i:[] for i in range(256)}
    strings = {}

    for op in sequence:
        if '=' in op:
            string,value = op.split('=')
            value = int(value)

            h = hash(string)

            if string in strings.keys():
                old_value = strings[string]
                i = boxes[h].index((string, old_value)) 
                boxes[h][i] = (string, value)
            else:
                boxes[h].append((string, value))

            strings[string] = value
        else:
            string = op.split('-')[0]
            if string in strings.keys():
                value = strings[string]
                h = hash(string)
                boxes[h].remove((string, value))
                del strings[string]
        
        print_boxes(op, boxes)
        print(f'Focusing power: {focusing_power(boxes)}')

main()
s = 0

def predict(hist):
    diff = []
    print(hist)
    for i in range(1, len(hist)):
        diff.append(hist[i] - hist[i-1])
    if any(diff):
        diff.append(predict(diff))
    else:
        diff.append(0)
    return hist[-1] + diff[-1]

while True:
    try:
        hist = list(map(int, input().split()))
        n = predict(hist)
        print(n)
        s += n
    except EOFError:
        break
print(s)
while True:
    try:
        time = int(input().split(':')[-1].replace(' ',''))
        distance = int(input().split(':')[-1].replace(' ',''))
        print(time)
        print(distance)
    except EOFError:
        break

ways=0
for j in range(1,time):
    if (time-j)*j > distance:
        ways += 1
        
print(ways)
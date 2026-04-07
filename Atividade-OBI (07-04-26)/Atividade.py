A = int(input())
B = int(input())
C = int(input())

total = A + B*2 + C*3

if total >= 150:
    print("C")
else:
    if total >= 120:
        print("B")
    else:
        if total >= 100:
            print("A")
        else:
            print("N")
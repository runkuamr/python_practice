t = int(input())
while t > 0:
    A, B = map(int, input().split())
    if A > B:
        print ("A")
    else:
        print ("B")
    t = t -1
    
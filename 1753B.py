def problem():
    length, x = [int(_) for _ in input().split()]
    seq = [int(_) for _ in input().split()]
    factorials = [0 for _ in range(x)]

    for num in seq:
        factorials[num-1] += 1

    for idx in range(x-1):
        if factorials[idx]%(idx+2) == 0:
            factorials[idx+1] += int(factorials[idx]/(idx+2))
            factorials[idx] = 0
        else:
            print("No")
            return
    print("Yes")
    return

problem()

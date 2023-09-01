def problem():
    n = int(input())
    seq = [int(_) for _ in input().split()]

    signs = ["+"]
    total = seq[0]
    for char in seq[1:]:
        if signs[-1] == "-":
            signs.append("+")
            total += char
        elif signs[-1] == "+":
            if total-char != 0:
                signs.append("+")
                total += char
            else:
                signs.append("-")
                total -= char

    if total != 0:
        print(-1)
        return

    partitions = []
    partition_start = 1
    for idx in range(1, len(signs)):
        if signs[idx-1] == signs[idx] == "+":
            partitions.append((partition_start, idx))
            partition_start = idx + 1
    partitions.append((partition_start, len(signs)))

    print(len(partitions))
    for _ in partitions:
        print(*_)


t = int(input())
for _ in range(t):
    problem()
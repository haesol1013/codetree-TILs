n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]


def explode(n, m, bombs):
    while True:
        new_bombs = []
        i = 0
        exploded = False

        while i < len(bombs):
            start = i
            while i < len(bombs) and bombs[start] == bombs[i]:
                i += 1

            if i - start >= m:
                exploded = True
            else:
                new_bombs.extend(bombs[start:i])

        if not exploded:
            break

        bombs = new_bombs

    return bombs


bombs = explode(n, m, bombs)

print(len(bombs))
for bomb in bombs:
    print(bomb)
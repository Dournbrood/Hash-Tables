cache = {}


def expensive_seq(x, y, z):

    n = (x, y, z)
    # Base Case
    if n[0] <= 0:
        return n[1] + n[2]
    if n not in cache:
        cache[n] = expensive_seq(n[0]-1, n[1]+1, n[2]) + expensive_seq(
            n[0]-2, n[1]+2, n[2]*2) + expensive_seq(n[0]-3, n[1]+3, n[2]*3)

    return cache[n]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

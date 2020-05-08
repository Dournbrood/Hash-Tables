def no_dups(str):

    split_str = str.lower().split()

    cache = {}

    result = []

    for word in split_str:
        n = word

        if n not in cache:
            cache[n] = 1
            result.append(n)

    return " ".join(result)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

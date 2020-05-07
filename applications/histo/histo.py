def histo(str):

    blacklist = ['"', ":", ";", ",", ".", "-", "+", "=", "/",
                 "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

    cache = {}

    split_str = str.lower().split()

    for word in split_str:
        for char in blacklist:
            word = word.replace(char, "")

        n = (word)

        if n != "" and n not in cache:
            cache[n] = 1

        elif n != "":
            cache[n] += 1

    counts = cache
    cache = {}

    for word, count in counts.items():
        n = count

        if n not in cache:
            cache[n] = [word]
        else:
            cache[n].append(word)

    counts = cache
    cache = {}

    for count_tup in sorted(counts.items(), reverse=True):
        cache[count_tup[0]] = count_tup[1]

    for count, words in cache.items():
        cache[count] = sorted(words)
        for word in cache[count]:
            tags = "#" * count
            print(f"{tags}: {word}")

    return cache


with open("robin.txt") as f:
    words = f.read()

histo(words)

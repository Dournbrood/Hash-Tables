def word_count(str):

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

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back. ;;;;;;;;;;;;'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))

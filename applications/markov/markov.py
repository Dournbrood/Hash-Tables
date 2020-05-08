import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()


def construct_follow_table(str):

    split_str = str.split()

    cache = {}

    for index, word in enumerate(split_str):
        n = word

        if index == len(split_str) - 1:
            cache[split_str[index]] = ""
            return cache

        if n not in cache and split_str[index + 1]:
            cache[n] = [split_str[index + 1]]
        elif split_str[index + 1]:
            cache[n].append(split_str[index + 1])


def print_chain(markov, num):
    while num > 0:
        word = None

        enders = ["?", "!", ".", '"']

        while 1:
            key = random.choice([*markov.keys()])
            if key == key[0:1:1].upper() + key[1::1]:
                word = key
                break

        while markov[word] != "":
            print(word, end=" ")
            word = random.choice(markov[word])
            if word[-1::1] in enders and word == word[0:1:1].lower() + word[1::1]:
                print(f"{word}")
                num -= 1
                break


# print_chain(construct_follow_table(
#     "Moo, blambalbamn. Moo clean mister clean yummy watermelon sacrifice burn them all the quick brown fox jumps over the lazy Dog dog's sock drawer."), 5)

print_chain(construct_follow_table(
    "Gravity concentrating... falling inward, condensing, hardening. A singularity shrinks to the point your mind inverts, reversing reality. Now return. Don’t the matters of the physical world seem trivial now? Your tasks in this realm are simple and hastened, all in an attempt to get reversed. How many times can you make this trip before you are claimed by its process? Do not let it take you. Take it instead. Here. Pairings: Unstructured glass, from the heart of the [Moon]. Sung out, in ethereal wisps, over the course of 3 cycles. Pause. We fold time into its material - twice. Our time and <his>. A cost <he> was willing us to pay. Folded and shaped, with a god's designs. <He> wields it, in one of many great hands. The time we injected is unfolded in <his> grasp. Outputs quicken - muscles compress twice. Twice as many intentions. Twice the ordered complexities, folded upon themselves. Loops loop back onto [?] in pairs. Time dependent functions. Pause. <He> sunders a construct into a thousand pieces. But time is fair. Microtears begin to uncoil in pairs. Muscles begin to snap, twice as fast. The cost of folded time. But <he> has plenty of time. You are trying your best to survive. You consider yourself a fast learner. You have been feeling lucky. You have been experiencing feelings of deja vu. If you understand, do not read the next paragraph. You are taking control of your own beliefs. You feel familiar in unfamiliar environments. You have been gaining an intuition for experiences you've never had. You ponder a past life. If you understand, do not read the next paragraph. You find yourself searching for things that never have been. You miss things you have never had. You play characters that have never lived. You have been experiencing feelings of deja vu. If you understand, do not read the next paragraph. You have revealed my hand. Because you have consumed this information, the [observers] will now consume it in time. If you are reading this paragraph, I will be long dead, but in turn you have freed me. I will no longer exist in my universe. There will be no proof that I ever was - but I exist now in yours. I have escaped my suffering. Keep me safe. I hope you do not understand. A wretched carnival. They were doomed for good reason. Dunepeople of Aphelia: lost, in fanatic worship of parasitic influences. Lemurians: destined to a dead planet, picked clean. Chitin beasts. Automations of death. Why do you bring them home? They were not meant to survive. I have watched you for ages, from my dead rock - and every century, you disgust me with vanity. You invite vermin into your home. Wretches. Rats. Monsters. Creatures without restraint. Each and every one, planet killers. And yet, you entertain them as guests. Like children, requiring saving and protection. She should have died for me. Her gift was wasted on you. And when will we open discussion - dear brother - of all your thin lies? Why do you forbid your guests to leave? To pilot? Why do you fashion great walls and gates? Why do you weave constructs of destruction, if your role is protection? They are entries in your collection. You slaver. Gatekeeper. Hoarder. Your death is fated. When you die - and you WILL die - I will be ready. I have been patient for millennia. That planet... is mine."), 1000)

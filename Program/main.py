#2022 -ALevel

import random
import os
import math

os.system('cls')

accepted_words = []
file = open("Computational-Projects/Chimps-on-Wordle/Program/accepted_words.txt", "r")
raw_words = file.readlines()
for word in raw_words:
    accepted_words.append(word.strip())


def print_colour(word_list, aim):
    greend = []
    score = []
    for i in range(0, len(aim)):
        x = 0
        y = 0
        if word_list[i] == aim[i]:
            print("\033[1;37;42m" + str(word_list[i]), end="")
            greend.append(word_list[i])
            score.append(2)
        else:
            for j in aim:
                if word_list[i] == j:
                    for k in greend:
                        if word_list[i] == k:
                            y = 1
                    if y == 0:
                        print("\033[1;37;43m" + str(word_list[i]), end="")
                        score.append(1)
                        x = 1
            if x == 0:
                print("\033[1;37;40m" + str(word_list[i]), end="")
                score.append(0)
    print("\033[1;37;40m\n")
    return score


def get_aim():
    while True:
        total = 0
        aim = []
        print("Enter the Wordle:")
        phrase = input("")
        try:
            phrase = phrase.upper()
        except:
            pass
        aim = list(phrase)
        for i in aim:
            for j in printable:
                if i == j:
                    total += 1
        for i in accepted_words:
            isword = phrase.lower()
            if str(isword) == str(i) and total == 5:
                return aim
        else:
            print("~Please enter a five letter word~")
    return aim


def pure_rand(chimps, aim):
    tries = 0
    while chimps != aim:
        first = random.choice(printable)
        if len(list(first)) > 1:
            first = ""
        chimps = [first]
        while len(chimps) != len(aim):
            appendable = random.choice(printable)
            if len(list(appendable)) > 1:
                appendable = ""
            chimps.append(appendable)
        print_colour(chimps, aim)
        tries += 1
    return tries


def rand_words(chimps, aim):
    tries = 0
    while chimps != aim:
        chimps = list(random.choice(accepted_words).upper())
        print_colour(chimps, aim)
        tries += 1
    return tries


def minor_intelligence(chimps, aim, printable):
    tries = 1
    last = list(random.choice(accepted_words).upper())
    score = print_colour(last, aim)
    new_printable = printable
    while chimps != aim and last != aim:
        chimps = []
        index = 0
        yellow = ""
        for i in score:
            if i == 2:
                chimps.append(last[index])
            elif i == 1:
                chimps.append(random.choice(new_printable))
                yellow = last[i]
            else:
                if yellow != "":
                    chimps.append(yellow)
                    yellow == ""
                else:
                    chimps.append(random.choice(new_printable))
                try:
                    new_printable.remove(last[index])
                except:
                    pass
            index += 1
        last = chimps
        score = print_colour(chimps, aim)
        tries += 1
    return tries


def mode(aim, printable):
    chimps = []
    while True:
        print(
            "(a) Entirely random, or (b) Random correct words, or (c) Minor intelligence?"
        )
        choice = input()
        if choice == "a":
            tries = pure_rand(chimps, aim)
            break
        elif choice == "b":
            tries = rand_words(chimps, aim)
            break
        elif choice == "c":
            tries = minor_intelligence(chimps, aim, printable)
            break
    return tries


while True:
    os.system('cls')
    chimps = []
    tries = 0
    printable = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    print("""
  CHIMPS ON WORDLE
  ----------------
  """)

    aim = get_aim()
    tries = mode(aim, printable)

    print("DONE in {} tries".format(tries))
    print("That would take", math.ceil(tries / 6), "days")
    print("Which is", round((tries / 6) / 365, 2), "years")
    print("")
    print("Continue?")
    answer = input()
    if answer == "no" or answer == "n" or answer == "No" or answer == "N":
        break

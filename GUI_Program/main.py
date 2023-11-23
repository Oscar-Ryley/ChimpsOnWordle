#2022 -ALevel

import random
import os
import math
import PySimpleGUI as sg

os.system('cls')

accepted_words = []
file = open("GUI_Program/accepted_words.txt", "r")
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
            print(str(word_list[i]), end="")
            greend.append(word_list[i])
            score.append(2)
        else:
            for j in aim:
                if word_list[i] == j:
                    for k in greend:
                        if word_list[i] == k:
                            y = 1
                    if y == 0:
                        print(str(word_list[i]), end="")
                        score.append(1)
                        x = 1
            if x == 0:
                print(str(word_list[i]), end="")
                score.append(0)
    print("\n")
    return score

def pure_rand(chimps, aim, printable):
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

def mode(choice, aim, printable):
    chimps = []
    if choice == "er":
        tries = pure_rand(chimps, aim, printable)
    elif choice == "rc":
        tries = rand_words(chimps, aim)
    elif choice == "mr":
        tries = minor_intelligence(chimps, aim, printable)
    return tries

def main():
    sg.theme("SystemDefaultForReal")
    width = 420
    height = 700
    SearchScreenLayout = [
    [sg.Button("Entirely random", enable_events = True), sg.Button("Random correct words", enable_events = True), sg.Button("Minor Intelligence?", key = "mr", enable_events = True)],
    [sg.Text("Enter the Wordle:"), sg.InputText(size = (25,1), key = "iwordle") , sg.Button("Enter", enable_events = True)],
    [sg.Output(size = (420, 700))]
    ]
    window = sg.Window("Chimps on Wordle", SearchScreenLayout, size = (width,height), resizable = True)
    printable = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    cmode = "rc"
    while True:
        tries = 0
        event, values = window.read()

        if event == "Entirely random":
            cmode = "er"

        if event == "Random correct words":
            cmode = "rc"

        if event == "Minor Intelligence?":
            cmode = "mr"

        if event == "Enter":
            total = 0
            aim = []
            phrase = (values["iwordle"]).upper()
            aim = list(phrase)
            for i in aim:
                for j in printable:
                    if i == j:
                        total += 1
            for i in accepted_words:
                isword = phrase.lower()
                if str(isword) == str(i) and total == 5:
                    tries = mode(cmode, aim, printable)
                    print("DONE in {} tries".format(tries))
                    print("That would take", math.ceil(tries / 6), "days")
                    print("Which is", round((tries / 6) / 365, 2), "years")
                    
        if event == sg.WIN_CLOSED:
            window.close()
            break

if __name__ == "__main__":
    main()
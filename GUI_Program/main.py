#2022 -ALevel

import random
from math import ceil
import PySimpleGUI as sg

accepted_words = []
file = open("GUI_Program/accepted_words.txt", "r")
raw_words = file.readlines()
for word in raw_words:
    accepted_words.append(word.strip())

def print_colour(word_list, aim, window):
    greend = []
    score = []
    for i in range(0, len(aim)):
        x = 0
        y = 0
        if word_list[i] == aim[i]:
            window["output"].print(str(word_list[i]), end="", text_color="white", background_color="#6ca965")
            greend.append(word_list[i])
            score.append(2)
        else:
            for j in aim:
                if word_list[i] == j:
                    for k in greend:
                        if word_list[i] == k:
                            y = 1
                    if y == 0:
                        window["output"].print(str(word_list[i]), end="", text_color="white", background_color="#c8b653")
                        score.append(1)
                        x = 1
            if x == 0:
                print(str(word_list[i]), end="")
                score.append(0)
    window["output"].print("\n")
    window.refresh()
    return score

def pure_rand(chimps, aim, printable, window):
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
        print_colour(chimps, aim, window)
        tries += 1
    return tries

def rand_words(chimps, aim, window):
    tries = 0
    while chimps != aim:
        chimps = list(random.choice(accepted_words).upper())
        print_colour(chimps, aim, window)
        tries += 1
    return tries

def minor_intelligence(chimps, aim, printable, window):
    tries = 1
    last = list(random.choice(accepted_words).upper())
    score = print_colour(last, aim, window)
    new_printable = printable
    while chimps != aim and last != aim:
        chimps = []
        index = 0
        for i in score:
            if i == 2:
                chimps.append(last[index])
            else:
                chimps.append(random.choice(new_printable))
            index += 1
        last = chimps
        score = print_colour(chimps, aim, window)
        tries += 1
    return tries

def mode(choice, aim, printable, window):
    chimps = []
    if choice == "er":
        tries = pure_rand(chimps, aim, printable, window)
    elif choice == "rc":
        tries = rand_words(chimps, aim, window)
    elif choice == "mr":
        tries = minor_intelligence(chimps, aim, printable, window)
    return tries

def main():
    sg.theme("SystemDefaultForReal")
    width = 420
    height = 700
    SearchScreenLayout = [
    [sg.Button("Entirely random", enable_events = True), sg.Button("Random correct words", enable_events = True), sg.Button("Minor Intelligence", enable_events = True)],
    [sg.Text("Enter the Wordle:"), sg.InputText(size = (25,1), key = "iwordle") , sg.Button("Enter", enable_events = True)],
    [sg.Output(size = (420, 700), background_color="black", text_color="white", key="output")]
    ]
    window = sg.Window("Chimps on Wordle", SearchScreenLayout, size = (width,height), resizable = True)
    printable = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    cmode = "rc"
    while True:
        event, values = window.read()
        tries = 0
        chimps = []

        if event == "Entirely random":
            cmode = "er"

        if event == "Random correct words":
            cmode = "rc"

        if event == "Minor Intelligence":
            cmode = "mr"

        if event == "Enter":
            chimps = []
            tries = 0
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
                    tries = mode(cmode, aim, printable, window)
                    print("DONE in {} tries".format(tries))
                    print("That would take", ceil(tries / 6), "days")
                    print("Which is", round((tries / 6) / 365, 2), "years")
                    
        if event == sg.WIN_CLOSED:
            window.close()
            break

if __name__ == "__main__":
    main()
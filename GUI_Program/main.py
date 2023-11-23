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
    word = []
    greend = []
    score = []
    for i in range(0, len(aim)):
        x = 0
        y = 0
        if word_list[i] == aim[i]:
            word.append(str("\033[1;37;42m" + str(word_list[i])))
            greend.append(word_list[i])
            score.append(2)
        else:
            for j in aim:
                if word_list[i] == j:
                    for k in greend:
                        if word_list[i] == k:
                            y = 1
                    if y == 0:
                        word.append(str("\033[1;37;43m" + str(word_list[i])))
                        score.append(1)
                        x = 1
            if x == 0:
                word.append(str("\033[1;37;40m" + str(word_list[i])))
                score.append(0)
    word.append("\033[1;37;40m\n")
    return score, word

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
        output = print_colour(chimps, aim)
        tries += 1
    return output, tries


def rand_words(chimps, aim):
    output = []
    tries = 0
    while chimps != aim:
        chimps = list(random.choice(accepted_words).upper())
        output.append(print_colour(chimps, aim))
        tries += 1
    return output, tries


def minor_intelligence(chimps, aim, printable):
    output = []
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
        output.append(score)
        tries += 1
    return output, tries


def mode(choice, aim, printable):
    printable = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    chimps = []
    while True:
        if choice == "a":
            output, tries = pure_rand(chimps, aim, printable)
            break
        elif choice == "b":
            output, tries = rand_words(chimps, aim)
            break
        elif choice == "c":
            output, tries = minor_intelligence(chimps, aim, printable)
            break
    return output, tries

def main():
    sg.theme("SystemDefaultForReal")
    width = 1000
    height = 700
    output = [[sg.Text("Output", key="output")]]
    SearchScreenLayout = [
    [sg.Button("Entirely random", key= "er", enable_events = True), sg.Button("Random correct words", key = "rc", enable_events = True), sg.Button("Minor Intelligence?", key = "mr", enable_events = True)],
    [sg.Text("Enter the Wordle:"), sg.InputText(size = (25,1), key = "iwordle") , sg.Button("Enter", enable_events = True)],
    [sg.Column(output, scrollable=True,  vertical_scroll_only=True, size = (1920, 1080), expand_x = True, expand_y = True)]
    ]
    window = sg.Window("The Fountain of Knowledge", SearchScreenLayout, size = (width,height), resizable = True)
    printable = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    choice = "c"
    while True:
        chimps = []
        tries = 0
        event, values = window.read()
        if event == "Enter":
            total = 0
            aim = []
            try:
                phrase = (values["iwordle"]).upper()
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
                    output, tries = mode(choice, aim, printable)
                    output += ("DONE in {} tries".format(tries))
                    output += ("That would take", math.ceil(tries / 6), "days")
                    output += ("Which is", round((tries / 6) / 365, 2), "years")
            
        if event == sg.WIN_CLOSED:
            window.close()
            break
        
        if event == "er":
            choice = "a"

        if event == "rc":
            choice = "b"

        if event == "mr":
            choice == "c"

if __name__ == "__main__":
    main()
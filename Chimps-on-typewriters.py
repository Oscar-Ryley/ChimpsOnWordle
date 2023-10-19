#2021 -GCSE

import os
import random
import string
os.system("cls")
while True:
  os.system("cls")
  chimps = []
  tries = 0

  print("""
  CHIMPS ON TYPEWRITERS
  ---------------------
  """)

  while True:
    aim = []
    print("Enter your text:")
    phrase = input("")
    aim = list(phrase)
    break

  while chimps != aim:
    first = random.choice(string.printable)
    if len(list(first)) > 1:
      first = ""
    chimps = [first]
    while len(chimps) != len(aim):
      appendable = random.choice(string.printable)
      if len(list(appendable)) > 1:
        appendable = ""
      chimps.append(appendable)
    print(chimps)
    tries += 1

  print("DONE in {} tries" .format(tries))
  print("")
  print("Continue?")
  answer = input()
  if answer == "no" or answer == "n" or answer == "No" or answer == "N":
    break
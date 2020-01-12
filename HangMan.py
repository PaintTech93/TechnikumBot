import os
from listen import myCommand
from talk import talk

def hanged(dead):

    fileList = list()
    with open('HangmanPics.txt') as f:
      for line in f:
        fileList.append(line)

    if dead == 0:
        start=1
        ende=8
        while start<=ende:
            print(fileList[start])
            start+=1
    elif dead == 1:
        start=11
        ende=18
        while start<=ende:
            print(fileList[start])
            start+=1
    elif dead == 2:
        start=30
        ende=37
        while start<=ende:
            print(fileList[start])
            start+=1
    elif dead == 3:
        start=40
        ende=47
        while start<=ende:
            print(fileList[start])
            start+=1
    elif dead == 4:
        start=50
        ende=57
        while start<=ende:
            print(fileList[start])
            start+=1
    elif dead == 5:
        start=60
        ende=67
        while start<=ende:
            print(fileList[start])
            start+=1

def winlose(dead,guess_word):
    if dead==7:
        return 1
    for elem in guess_word:
        if elem=="*":
            return 2
    return 0

def charcheck(word):
        if word.lower() =="alpha":
            return "a"
        elif word.lower() == "bravo":
            return "b"
        elif word.lower() == "charlie":
            return "c"
        elif word.lower() == "delta":
            return "d"
        elif word.lower() == "echo":
            return "e"
        elif word.lower() == "foxtrot":
            return "f"
        elif word.lower() == "golf":
            return "g"
        elif word.lower() == "hotel":
            return "h"
        elif word.lower() == "india":
            return "i"
        elif word.lower() == "juliett":
            return "j"
        elif word.lower() == "kilo":
            return "k"
        elif word.lower() == "lima":
            return "l"
        elif word.lower() == "mike":
            return "m"
        elif word.lower() == "november":
            return "n"
        elif word.lower() == "oscar":
            return "o"
        elif word.lower() == "papa":
            return "p"
        elif word.lower() == "quebec":
            return "q"
        elif word.lower() == "romeo":
            return "r"
        elif word.lower() == "sierra":
            return "s"
        elif word.lower() == "tango":
            return "t"
        elif word.lower() == "uniform":
            return "u"
        elif word.lower() == "victor":
            return "v"
        elif word.lower() == "whiskey":
            return "w"
        elif word.lower() == "x-ray":
            return "x"
        elif word.lower() == "yankee":
            return "y"
        elif word.lower() == "zulu":
            return "z"
        else:
            return "wrong"


def game ():

    talk("Random word is generated, game is started")
    word="Hello"
    dead=0
    guess_word=""
    used=""

    for elem in word:
        guess_word=guess_word+"*"

    while True:
        os.system('cls')
        hanged(dead)
        print(dead,"/5 mistakes")
        print("Word: ", guess_word)
        print("Used characters: ", used)
        x=charcheck(myCommand())
        if x == "wrong":
            talk("I didn't understand your letter, please say the word again")
        else:
            right=False
            i=0

            for elem in word:
                if x==elem.lower():
                    right=True
                    guess_word = guess_word[:i] + x + guess_word[i+1:]
                i+=1

            if right==True:
                talk("Right letter!")

            else:
                talk("Wrong letter!")
                dead+=1
            used=used+x
            check=winlose(dead,guess_word)

            if check == 0:
                talk("You win!")
                break
            elif check == 1:
                talk("You lost!")
                break

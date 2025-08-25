

import random
import sys

def gameover():
    with open("../res/GAMEOVER.txt", "r") as file:
        text = file.read()
        print(text)
        gameover = input("try again ? yes - no: ")
        if gameover == "yes":
            start()
        elif gameover == "no":
            sys.exit()

def tuer1():
    with open("../res/Door1.txt", "r") as file:
        text = file.read()
        print(text)
        action = input("stay - search - back:")
        if action == "stay":
            print ("place holder")
        elif action == "search":
            print ("place holder")
        elif action == "back":
            tueren()


def tuer2_2():
    with open("../res/Door2_no_food.txt", "r") as file:
        text = file.read()
        print(text)
        action = input("check cupboard - back:")
        if action == "back":
            tueren()
        elif action == "check" or action == "check cupboard":
            print("its empty...")
            action2 = input("look closer - back:")
            if action2 == "back":
                tuer2()
            elif action2 == "look closer":
                print("insert secret tunnel")

def tuer2():
    with open("../res/Door2.txt", "r") as file:
        text = file.read()
        print(text)
        action = input("eat it - check cupboard - back:")
        if action == "back":
            tueren()
        elif action == "eat" or action == "eat it":
            x = random.randint(1, 10)
            if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
              print("you feel ill but at least you're not hungry anymore...(place holder)")
              action3 = input("back: ")
              if action3 == "back":
                 tuer2_2()
            elif x == 6 or x == 7 or x == 8 or x == 9 or x == 10:
              print("your hunger subsides...for now(place holder)")
              action4 = input("back: ")
              if action4 == "back":
                  tuer2_2()
        elif action == "check" or action == "check cupboard":
            print("its empty...")
            action2 = input("look closer - back:")
            if action2 == "back":
                tuer2()
            elif action2 == "look closer":
                print("insert secret tunnel")



def tueren():
 with open("../res/entry.txt", "r") as file:
        text = file.read()
        print(text)
 door=input ("Door 1 - Door 2 :")
 if door=="Door 1" or door=="1":
     tuer1()

 elif door == "cellar":
     print("You open the hidden cellar and get jumpscared >:)")
     gameover()
 elif door == "Door 2" or door=="2":
    tuer2()


 else:
    tueren()


def eingang():

 enter = input("yes - no : ")

 if enter == "yes":
    # eingang
    with open("../res/entry.txt", "r") as file:
        text = file.read()
        print(text)
    tueren()
 elif enter == "no":
     with open("../res/GAMEOVER.txt", "r") as file:
         text = file.read()
         print(text)
 else:
     eingang()


#start
def start():
  with open ("../res/intro.txt","r") as file:
    intro=file.read()
    print(intro)

    enter = input("yes - no : ")

    if enter == "yes":
        # eingang

        tueren()
    elif enter == "no":
        gameover()


    else:
        eingang()
print("start game ?")
anfang = input("yes - no : ")
if anfang == "yes":
 start()








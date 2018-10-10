# Fibonacci Formula made in python by Daan
# Anyone can copy and use this code



import time
import os



def start():
    global t
    global old
    global new
    global newer
    global counter
    old = 1
    new = 0
    newer = 0
    counter = 0
    t = 0
    info()


def end():
    global t
    global old
    global new
    global newer
    global counter
    old = 1
    new = 0
    newer = 0
    counter = 0
    t = 0
    print("Done! exiting in 3 seconds..")
    time.sleep(3)
    exit()


def ask():
    cls()
    command = raw_input("Typ auto to automatically do a calculation every x seconds\nTyp manual for an instant calculation of choice.\n\n")
    command = str(command)
    if command == "auto":
        global t
        global repeatNum
        t = raw_input("Welcome!, how many seconds do you want the interval to be?\n")
        t = float(t)
        repeatNum = raw_input("How many calculations do you want to get done?\n")
        repeatNum = int(repeatNum)
        auto()
    if command == "manual":
        repeatNum = raw_input("How many calculations do you want to get done?\n")
        repeatNum = int(repeatNum)
        auto()
    else:
        ask()


def info():
    print("Welcome to the Fibonacci Calculator!")
    time.sleep(1)
    ask()


def cls():
    clear = "\n" * 100
    print clear


def count():
    global counter
    counter = counter + 1
    print_string()


def print_string():
    global counter
    global newD
    global oldD
    global newerD
    cnt = str(counter)
    oldD = str(old)
    newD = str(new)
    newerD = str(newer)
    print("Calculation count: " + cnt + "\n---------------------------------------\nCalculation: " + oldD + " + " + newD + " = " + newerD)


def auto():
    global repeatNum
    global t
    global old
    global new
    global newer
    newer = old + new
    cls()
    count()
    print(newer)
    old = new
    new = newer
    time.sleep(t)
    if counter < repeatNum:
        auto()
    else:
        end()

def mCalc():
    global g
    global old
    global new
    global newer
    global repeatNum
    newer = old + new
    old = new
    new = newer
    if counter < repeatNum:
        mCalc()
    if counter == repeatNum:
        cls()
        count()
        end()



start()


    
    





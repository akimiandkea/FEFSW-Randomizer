import random
import os
import sys
import time

def main():
    seed = input("Seed:")
    random.seed(seed)
    base_dir = os.path.dirname(sys.executable)
    #base_dir = os.path.dirname(__file__)
    name_list = []
    class_list = []
    with open(os.path.join(base_dir, "lists", "characters.txt")) as f:
        for x in f:
            name_list.append(x)

    with open(os.path.join(base_dir, "lists", "classes.txt")) as f:
        for x in f:
            class_list.append(x)

    while True:
        mode = input("Class randomizer? (y/n):")
        if mode.lower() == "y" or mode.lower() == "n":
            break
        else:
            print("Please input y or n.")
    while True:
        toGet = input("How many?:")
        try:
            if int(toGet) > len(name_list):
                print("That's too high. There are 108 units.")
            else:
                toGet = int(toGet)
                break
        except ValueError:
            print("That's not a number.")


    path = os.path.join(base_dir, "character_list.txt")


    with open(path,"w") as f:
        
        newlist = random.sample(name_list, toGet)
        parentsUsed = []
        for i in newlist:
            toPrint = i.strip()
            try:
                with open(os.path.join(base_dir, "lists", "kid_parents/", toPrint+".txt")) as g:
                    temp_list = []
                    for x in g:
                        temp_list.append(x.strip())
                    while True:
                        parentChoice = random.choice(temp_list).strip()
                        if parentChoice not in parentsUsed:
                            toPrint = parentChoice + "!" + toPrint
                            parentsUsed.append(parentChoice)
                            break
            except FileNotFoundError or OSError:
                pass
            if(mode.lower() == "y"):
                toPrint = toPrint + ": " + random.choice(class_list)
            f.write(toPrint + "\n")
    print("List printed at " + path)
    try:
        input("Press Enter to finish.")
    except EOFError:
        time.sleep(10)

if __name__ == "__main__":
    main()
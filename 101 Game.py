import random

while True:
    mainmenu = input("S to START, Q to Quit: ")
    if mainmenu == "Q":
        print("\nmade by eysir")
        break
    elif mainmenu == "S":
        gamenumber = 101
        options = {"1", "2", "3", "4", "5", "6", "7"}
        cpuoptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        def start():
            return random.choice((0, 1))


        start = start()
        if start == 0:
            print("You will start. Be ready!\nStarting Number", gamenumber)
        elif start == 1:
            print("Cpu will start. Be ready!\nStarting Number", gamenumber)


        def game(start, gamenumber):
            while True:
                if start == 0 and gamenumber > 0:
                    while True:
                        userchoice = input("Choose a number from 1 to 7(1 and 7 included), R to main menu: ")
                        print(" ")
                        if userchoice in options:
                            print("You choose", userchoice)
                            gamenumber = gamenumber - int(userchoice)
                            print("Remaining Number:", gamenumber)
                            print(" ")
                            start = 1
                            break
                        elif userchoice == "R":
                            start = 2
                            break
                        else:
                            print("Invalid option. Please write again!\n")
                            continue
                elif start == 1 and gamenumber > 0:

                    def cpumove():
                        return random.choice((1, 2, 3, 4, 5, 6, 7))

                    cpumove = cpumove()

                    if gamenumber > 8 * cpuoptions[-1]:
                        cpumove = gamenumber - 8 * cpuoptions[-1]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-2] < gamenumber < 8 * cpuoptions[-1]:
                        cpumove = gamenumber - 8 * cpuoptions[-2]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-3] < gamenumber < 8 * cpuoptions[-2]:
                        cpumove = gamenumber - 8 * cpuoptions[-3]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-4] < gamenumber < 8 * cpuoptions[-3]:
                        cpumove = gamenumber - 8 * cpuoptions[-4]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-5] < gamenumber < 8 * cpuoptions[-4]:
                        cpumove = gamenumber - 8 * cpuoptions[-5]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-6] < gamenumber < 8 * cpuoptions[-5]:
                        cpumove = gamenumber - 8 * cpuoptions[-6]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-7] < gamenumber < 8 * cpuoptions[-6]:
                        cpumove = gamenumber - 8 * cpuoptions[-7]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-8] < gamenumber < 8 * cpuoptions[-7]:
                        cpumove = gamenumber - 8 * cpuoptions[-8]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-9] < gamenumber < 8 * cpuoptions[-8]:
                        cpumove = gamenumber - 8 * cpuoptions[-9]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-10] < gamenumber < 8 * cpuoptions[-9]:
                        cpumove = gamenumber - 8 * cpuoptions[-10]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-11] < gamenumber < 8 * cpuoptions[-10]:
                        cpumove = gamenumber - 8 * cpuoptions[-11]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif 8 * cpuoptions[-12] < gamenumber < 8 * cpuoptions[-11]:
                        cpumove = gamenumber - 8 * cpuoptions[-12]
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif gamenumber < 8:
                        cpumove = gamenumber
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                    elif gamenumber == 8 * 12 or 8 * 11 or 8 * 10 or 8 * 9 or 8 * 8 or 8 * 7 or 8 * 6 or 8 * 5 or 8 * 4 or 8 * 3 or 8 * 2 or 8 * 1:
                        print("Cpu choose", cpumove)
                        gamenumber = gamenumber - int(cpumove)
                        print("Remaining Number:", gamenumber)
                        print(" ")
                        start = 0
                elif gamenumber == 0:
                    if start == 0:
                        print("Cpu Win\n")
                        break
                    elif start == 1:
                        print("You Win\n")
                        break
                elif gamenumber < 0:
                        print("Invalid option. Please write again!\n")
                        gamenumber = gamenumber + int(userchoice)
                        start = 0
                        print("Remaining Number:", gamenumber)
                        continue
                elif start == 2:
                    break
        game(start, gamenumber)
    else:
        print("Invalid option. Please write again!\n")
        continue

import random

ucount, scount = 0, 0
print("Hi!π Welcome to Rock, Paper and Scissors Game\n   Enjoy your time here")
point = int(input("For how many points you would like to play: "))
while True:
    opt = ["Rock", "Paper", "Scissors"]
    print("Rock, Paper or Scissors and Exit")
    inp = input("Enter your choice: ").capitalize()
    res = random.choice(opt)
    print("System choice {0}".format(res))
    if inp in opt:
        if inp == res:
            print("Tie π")
        elif inp == "Rock":
            if res == "Scissors":
                print("π¨βπ» got point")
                ucount += 1
                print("π¨βπ» Score {0}".format(ucount))
            else:
                print("π» got point")
                scount += 1
                print("π» Score {0}".format(scount))
        elif inp == "Paper":
            if res == "Rock":
                print("π¨βπ» got point")
                ucount += 1
                print("π¨βπ» Score {0}".format(ucount))
            else:
                print("π» got point")
                scount += 1
                print("π» Score {0}".format(scount))
        elif inp == "Scissors":
            if res == "Paper":
                print("π¨βπ» got point")
                ucount += 1
                print("π¨βπ» Score {0}".format(ucount))
            else:
                print("π» got point")
                scount += 1
                print("π» Score {0}".format(scount))
        if ucount == point or scount == point:
            if ucount == point:
                print("πββοΈ Won π₯")
                print("π¨βπ» Score {0} add π» Score {1}".format(ucount, scount))
                break
            else:
                print("π» Won π₯")
                print("π» Score {0} add π¨βπ» Score {1}".format(scount, ucount))
                break
        elif inp == "Exit":
            break
    else:
        print("βChoose Correct Option: ")

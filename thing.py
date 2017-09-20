import random
go = raw_input("Would you like to begin? (y/n)\n")
while go == "y":
    a = random.randint(0,99999999999999999999)
    b = raw_input("Guess an number\n")
    if a == b:
        print "Nice job"
    else:
        print "Wrong!\nThe answer was"
        print a

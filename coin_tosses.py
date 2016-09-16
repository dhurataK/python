import random
count = 0
head = 0
tail = 0
for var in range(0,4):
    rand_num = random.random()
    num = round(rand_num)
    if 0.0 <= num <= 1.0:
        count = count + 1
        print "Attempt #"+str(count)+":Throwing a coin...",
        if num == 0:
            print "It's a head!...",
            head = head +1
        elif num == 1:
            print "It's a tail!...",
            tail = tail +1
        print "Got "+str(head)+" head(s) and "+str(tail)+" tail(s) so far!"

def getGrade():
    print "Scores and Grades"
    for i in range(0,9):
        ip = input()
        if(ip < 60):
            print "You failed the exam. Your score is: "+str(ip)+" Good luck next time!"
        elif (ip >= 60 and ip <= 69):
            print "Score: "+str(ip)+"; Your grade is D"
        elif (ip >= 70 and ip <= 79):
            print "Score: "+str(ip)+"; Your grade is C"
        elif (ip >= 80 and ip <= 89):
            print "Score: "+str(ip)+"; Your grade is B"
        elif (ip >= 90 and ip <= 100):
            print "Score: "+str(ip)+"; Your grade is A"
        elif (ip > 100):
            print "Invalid score! "+str(ip)
    print "End of the program. Bye! "

getGrade()

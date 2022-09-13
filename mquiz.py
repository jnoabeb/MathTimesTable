#multiplication quiz
#try to introduce a countdown
# also try except to catch any errors
# modularise using functions
#use something like case instead of if then else
from random import randint
from ast import Try
from msilib.schema import Error
import datetime
from timeit import default_timer as timer
from datetime import timedelta


#WRITE HI SCORE
def writescore(filename,score,playrname,percent_age,exectime):
    msgvar = ""
    scoredate = datetime.datetime.now()
    ftext = "Name: " + str(playrname) + " Score: " + str(score) + " Percentage: " + str(percent_age) + "% Date: " + str(scoredate)+" ExecTime: "+ exectime +"\n"

    try:
        file = open(filename,'a')
        file.write(ftext)
        file.close()
        msgvar = "Success"
    except OSError as exception:
        prmsgvar = exception
    return msgvar

def welcome():
    print ("********************************WELCOME TO THE MATHS QUIZzz ver 1.0*******************\n")
    print("Please select the following:\n 1 - Play the game \n 2 Exit")
    mychoice = int(input())
    return mychoice

def get_name():
     # get name of player
    print ("Hi what is your name?")
    pname = str (input())
    
    return pname

def timeschoice(plname):
    print("Hello ",plname," which times table would you like to play? (choose from 1-12)")
    tbl = str (input())
    print("You chose the ",tbl, " times table. You will be asked 12 questions. Lets start...")
    return tbl




    

def playgame():

    wrongansw=0
    rightansw=0
    playername=""
    scores =""
    # get name of player
    playername=get_name()
    #times table choice
    timestbl=timeschoice(playername)
    start = timer()
    #ask 12 questions
    for i in range (0,2):
        num1 = randint (0,12)
        num2 = int(timestbl)
        print ("Question",i,":",num1,"*",num2,"=", end = " ")
        guess = int(input()) 
        answer = num1 * num2
        
        if guess == answer:
            print ("Well done",playername,"!")
            rightansw=rightansw+1
        else:
            print ("Wrong answer ", playername," the correct answer is: ",answer)
            wrongansw=wrongansw+1

    
    #report on game stat and calc the percentage score
    print("Total Correct answers: ",rightansw," Total Wrong answers: ",wrongansw)
    percentagescore = rightansw / 2 * 100
    format_float = "{:.2f}".format(percentagescore)
    scores = str(rightansw) + " / 12" 
    end = timer()
    ntime=str(timedelta(seconds=end-start))
    #write to file
    writescore("score.txt",scores,playername,format_float,ntime)
    



selchoice = welcome()
while (selchoice !=2):
    playgame()
    print("Press 1 to play again OR 2 to quit:")
    selchoice = int(input())
else:
    print("Thank you for playing. Goodbye")
    exit
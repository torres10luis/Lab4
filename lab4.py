"""
This program allows a user three tries to guess the correct answer to the question  
Question = "what is the capital of california". the answer is "sacramento".

we first set max_tries = 3. then we create a loop to iterate three times. for each iteration, we ask the user for the answer (user input).  then base on the answer the user gives, we check to see if the user input matches the asnwer. If so, print "correct", the terminate the loop with a break statement

if the user could not guess the correct answer within the max_tries, then print "you have used up your allotment of guesses.", then print" the correct answer is "california"

""" 
#print("testing")

"""
main 
    question = "what is the capital california"
    answer = "sacramento"
    ask(question, Answer)

ask 
    tries = 0 
    loop three times
        increment tries by 1
        ask user input()
        check to see of user input is equal to answer
            if so, print "correct" then exit the loop
    if not correct 
        print to the user "you have used up your allotment of guesses." 
        print the correct answer "the correct answer is 'sacramento'"

main
"""

def main():
    question =  "what is the capital california? "
    answer = "sacramento"
    ask(question, answer)

def ask(question, answer, max_tries=3):
    tries = 0
    ans= " "
    while tries < max_tries: 
        tries += 1
        ans = input(question).lower()
        if ans == answer:
            print("correct!")
            break
    if ans != answer:
        print("You have used up your allotment of guesses.")
       
main()
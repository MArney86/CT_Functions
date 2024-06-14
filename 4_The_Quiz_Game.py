def quiz_user(): #define the function that quized the user
    counter = 0 #create a counter for correct answers
    for content in quiz_content: #iterate the quiz contents and check if the answer is correct
        user_answer = input(f"{content[0]} ") #get the user's answer using the questions from the list of question answer pairs
        if user_answer == content[1]: #check if the user input the correct answer
            print("Correct") #print correct when it is
            counter += 1 #add one to the count of correct answers
        else: #not a correct answer
            print("Incorrect") #print incorrect for the missed answer
    return counter #return the correct answer counter

    

quiz_content = [ #Question and answer pairs for the quiz
    ["What is the capital of Texas?", "Austin"],
    ["What is 2 + 2 equal to?", "4"],
    ["Who was president in 1987?", "Ronald Reagan"],
    ["What is the URL for Coding Temple?", "www.codingtemple.com"],
    ["Who wrote the \"The Lord of the Rings\"?", "J.R.R. Tolkien"]
]

print("Welcome to the Quiz!!!")
while True: #start a loop so the user can retake the 
    score = quiz_user() #catch the correct answer number from the quizzing function
    print(f"Your Score was {score} out of {len(quiz_content)}") #print the number of correct answers from the quiz
    if score == len(quiz_content): #check score to give the user commentary
        print("Amazing, you got them all right!") #got them all right
    elif score <= len(quiz_content) - 1 and score > round(len(quiz_content) * .75): #got more than 3/4 right
        print("Good show, got almost all of them right!")
    elif score <= round(len(quiz_content) * .75) and score > round(len(quiz_content) * .5): #got more than half right
        print("Great effort, got more than half correct!")
    elif score <= round(len(quiz_content) * .5) and score > round(len(quiz_content) * .25): #got more than 1/4 right
        print("Better luck next time.")
    elif score <= round(len(quiz_content) * .25) and score > 0: #got atleast one correct answer
        print("Got atleast one right.")
    else: #didn't get a single answer correct
        print("May want to hit the books, you didn't get a single one correct.")

    again = input("Try again? ((Y)es/(N)o): ") #ask the user if they want to try again
    if again.lower() == 'y' or again.lower() == 'yes': #check their answer for a yes
        continue #start the loop over for a retry
    else: #user chose not to try again
        break #end the loop and program
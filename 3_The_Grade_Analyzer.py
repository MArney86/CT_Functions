def calculate_average(): #define average calculating function
    average = sum(student_grades) / len(student_grades) #calculate the average from the grade list
    print(f"Your grade average is: {round(average)}") #print the rounded average to user

def find_highest_lowest(): #define high-low finding function
    sorted = student_grades.copy() #copy list for organization
    sorted.sort() #sort list from lowest to highest
    print(f"Your highest grade was: {round(sorted[0])}") #use the organized list to print lowest grade
    print(f"Your lowest grade was:  {round(sorted[-1])}") #use the organized list to print hightest grade

def get_letter_grades():
    print("Your letter grades:") #start printing heading for letter grades
    for grade in student_grades: #iterate the list to print the grades in a formatted way
        if grade <= 100 and grade >= 90: #test for an A grade
            print(f"A {round(grade)}") #print an A grade with it's rounded value
        elif grade < 90 and grade >= 80: #test for a B grade
            print(f"B {round(grade)}") #print a B grade with it's rounded value
        elif grade < 80 and grade >= 70: #test for a C grade
            print(f"C {round(grade)}") #print a C grade with it's rounded value
        elif grade < 70 and grade >= 60: #test for a D grade
            print(f"D {round(grade)}") #print a D grade with it's rounded value
        else: #all other grades are F
            print(f"F {round(grade)}") #print a F grade with it's rounded value

student_grades = [45.6, 99.1, 50.9, 87.0, 94.2, 88.3, 90.0, 74.2, 74.1, 92.4, 100, 32.1, 66.2, 32.7] #predefined grades list to work with

while True:
    user_decision = input("What would you like to do with your gradelist?: (C)alculate grade average, (F)ind highest and lowest grades, (G)et letter grades, (Q)uit: ") #get user's function choice
    
    if user_decision.lower() == 'c': #check if user wanted to calculate the average
        calculate_average() #calculate the average
    
    elif user_decision.lower() == 'f': #user chose to remove an item
        find_highest_lowest() #print the highest and lowest grades
    
    elif user_decision.lower() == 'g': #user chose to print the list
        get_letter_grades() #print the grades with letter equivalents
    
    elif user_decision.lower() == 'q': #user chose to quit
        break #end loop and program
    
    else: #user selection is not on the menu list
        print("I didn't understand that request, please try again.") #let user know their choice is not in the menu and start loop over
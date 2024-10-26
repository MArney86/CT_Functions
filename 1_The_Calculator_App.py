#Task 1:
def add_numbers(a, b):
    return a + b #returns the sum

def sub_numbers(a, b):
    return a - b #returns the difference

def mult_numbers(a, b):
    return a * b #returns the product

def div_numbers(a, b):
    return a / b #returns the quotient

#Task 2:
while True:
    first_operand = float(input("Please input your first number: ")) #get your first operand from the user
    second_operand = float(input("Please input your second number: ")) #get your second operand for the user
    operation = input("Please choose an operation: (A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision, or (Q)uit: ") #chose an operation
    
    if operation.lower() == 'a': #check if addition was chosen
        solution = add_numbers(first_operand, second_operand) #obtain sum using add_numbers function
        print(f"{first_operand} + {second_operand} = {solution:.5f}") # print sum to user with 5 places of precision behind decimal
        
    elif operation.lower() == 's': #check if user chose subtraction
        solution = sub_numbers(first_operand, second_operand) #obtain difference using sub_numbers function
        print(f"{first_operand} - {second_operand} = {solution:.5f}") # print difference to user with 5 places of precision behind decimal
        
    elif operation.lower() == 'm': #check if user chose multiplictaion
        solution = mult_numbers(first_operand, second_operand) #obtain product using the mult_numbers function
        print(f"{first_operand} * {second_operand} = {solution:.5f}") # print product to user with 5 places of precision behind decimal
        
    elif operation.lower() == 'd': #check if user chose division
        #Task 3:
        if second_operand == 0: #test for divide by 0
            print("Cannot complete operation: divide by zero is undefined") #let user know that the operation is not possible
        else: #operation is not divide by 0
            solution = div_numbers(first_operand, second_operand) #obtain quotient with div_numbers function
            print(f"{first_operand} / {second_operand} = {solution:.5f}") # print quotient to user with 5 places of precision behind decimal
            
    elif operation.lower() == 'q': #check if user chose to quit
        break #quit loop and program
    
    #Task 3:
    else: #unanticipated input from user
        print("I didn't understand that selection, please try again") #let user know their choice is not in the menu and start loop over
    
    next = input("Try another operation? (yes/no): ") #ask if user is done
    if next.lower() == 'yes' or next.lower() == 'y': #check if user chooses to continue
        continue #continue to a new operation
    else: #user does not choose to continue
        break #end loop and program
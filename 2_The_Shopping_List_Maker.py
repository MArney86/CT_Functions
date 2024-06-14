def add_item(item_list, item): #define function that adds user items to our list
    
    if item not in item_list: #check if item is not already in list before adding to list
        item_list.append(item) #add user's item to the list
    
    else: #item is in the list already
        print("That item is already in your list") #let user know that that item is already in the list

def remove_item(item_list, item): #define function that removes user items from the list
    
    if item in item_list: #check first if item to remove is in the list
        item_list.remove(item) #remove the item that the user chose from the list
    
    else: #item is not in list
        print("That item is not in your list") #let the user know they are trying to remove and item not in the list

def print_items(item_list): #define the function that prints the list for user
    print("Your Shopping List:") #Heading for our list
    
    for item in item_list: #iterate the list
        print(f"• {item}") #print item with bullet

user_items = [] #initialize items list

while True:
    user_decision = input("What would you like to do with your list?: (A)dd and item, (R)emove an item, (P)rint your list, (Q)uit: ") #get user's function choice
    
    if user_decision.lower() == 'a': #check if user chose to add an item
        item_to_add = input("What item would you like to add?: ") #ask the user what item they want to add
        add_item(user_items, item_to_add) #add item to the list
    
    elif user_decision.lower() == 'r': #user chose to remove an item
        item_to_add = input("Which item would you like to remove from your list?: ") #ask user which item they want to remove
        remove_item(user_items, item_to_add) #remove the item input from the list
    
    elif user_decision.lower() == 'p': #user chose to print the list
        print_items(user_items) #print the list
    
    elif user_decision.lower() == 'q': #user chose to quit
        break #end loop and program
    
    else: #user selection is not on the menu list
        print("I didn't understand that request, please try again.") #let user know their choice is not in the menu and start loop over
    
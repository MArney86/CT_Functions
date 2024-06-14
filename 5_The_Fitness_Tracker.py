def get_calories_burned(activity,time): #function to get the calories burned by doing an activity for a given time in minutes
    calorie_coefficients = [ #calorie coefficients with keywords for activity
        ['running', 11.4],
        ['dancing', 7.0],
        ['swimming', 12.2],
        ['weightlifting', 4],
        ['pilates', 7.5],
        ['yoga', 5.1]
    ]
    calories_burned = 0 #initialize variable to store burned calories

    for coefficient in calorie_coefficients: #iterate through the coefficients
        if activity.lower() == coefficient[0]: #check if the activity has a coefficient in the list by it's label
            calories_burned =  coefficient[1] * time #multiply the coefficient that matches the activity with duration given
        else: #no coefficient found by label
            continue #continue iterating the list
    return calories_burned #return the resulting calories burned


def daily_calorie_summary(): #calorie summary function
    print("Your Daily Calorie Summary:") #Heading for the summary
    calories = 0 #initialize variable to store the calories during the loop
    total_calories = 0 #initialize variable to store the total of all calories burned
    for activity in activities: #iterate through the list of activities
        calories = get_calories_burned(activity, duration[activities.index(activity)]) #get the calories burned by passing the activity and the matching duration to the get_calories_burned() function
        print(f"You spent {duration[activities.index(activity)]} minutes doing {activity} and burned {calories} calories") #print out the summary for the chosen activity
        total_calories += calories #update the total calories for the current activity
    print(f"For a total of {total_calories} calories for the day.") #print final calorie total
        

activities = ['Running', "Dancing", "Swimming", "Weightlifting", "Pilates", "Yoga"] #list of activities for the day
duration = [15, 30, 20, 60, 20, 30] #matching durations of activities

daily_calorie_summary() #run the summary function
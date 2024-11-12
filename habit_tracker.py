'''
Connor Sweeney
habit_tracker.py
This app will help track the user's weight, caloric intake, macronutrients, water intake, and exercise 
each day to show possible trends and progress visualizations.
Eventually, the application will send a daily reminder for habit building and necessary daily inputs. 
'''
import time
import psycopg2
from connect import connect
from database import * #every function from database.py is used

class Dashboard(object):
    def __init__(self, user):
        self.name = user.upper()
        self.user_habitLyst = ['weight gain', 'weight loss']


    def main_menu(self,user): #this function will replace the "start" function to be more of a broad menu
        #if user in database.... else: go to the 'habit manager menu'
        while True:
            exit_var = self.newHabit(self.name)
            if exit_var == 0:
                continue
            else:
                continue
                
            '''
            if len(self.user_habitLyst) > 0:
                print("{self.name}'S HABITS: ", '  '.join(map(str, self.user_habitLyst)))
            '''
    def start(self): #needs to pass test cases where integers aren't inputted, and add woman calculation
        while True:
            print(f"Hi {self.name}, welcome to your Habit Tracker!")
            time.sleep(1.5)
            self.main_menu(self.name)
            
            '''
            print("In case you don't already know your Base Metabolic Rate (BMR), we can perform a short " +
                "calculation to provide a rough estimate of your BMR and provide your recommended " + 
                "daily caloric maintenance.")
            time.sleep(1)
            self.gender = input("Please enter your gender (press enter if you would rather not say): " )
            self.weight = int(input("Please enter your current weight in pounds: "))
            self.weight_kg = self.weight / 2.205

            self.height = int(input("Please enter your height in inches: "))
            self.height_cm = self.height * 2.54

            self.age = int(input("Please enter your age: "))
            self.exercise_scale = int(input("On a scale from 1-10, how active are you? (1 being little to no movement during the day and 10 being intense daily exercise): \n"))
            '''
            


    def newHabit(self, user):
        habit = ""
        self.lyst_of_habits = ["Weight Loss", "Weight Gain", "Hydration", "Maintain Weight", "Exercise"]
        print(f"{self.name}, what can Habit Tracker help you with?")
        #time.sleep(0.6)
        print("Try typing 'Weight Loss' or 'I need to drink more water.'")
        #time.sleep(0.6)
        print("You can also create your own habit reminders using 'custom'.") #later
        time.sleep(0.6)
        print("For a full list of recognized habits in Habit Tracker, type 'habits'.") 
        while habit == "":
            habit = input("---->  ").lower()
            if habit == 'exit': #exits to "main menu"/start screen
                return 0
            elif habit == "habits":
                for x in self.lyst_of_habits:
                    print(x)
                    time.sleep(0.3)
                habit = input("---->  ")
            habitBool = self.habitIdentifier(habit)
            
            if habitBool == False:
                habit = ""
                continue
            elif habitBool == -1:
                return 0
            elif habitBool == True: #this part will continue after a user has selected a habit
                print(self.user_habitLyst)
                #print("Awesome! We will now work on a plan for your habit!")

         
            
    def habitIdentifier(self,habit): #translates the habit into an existing category or makes a new habit 
       
        habit = habit.lower()
        trans_habit = ""

        if 'loss' in habit or 'cut' in habit or 'lose' in habit:
            trans_habit = "Weight Loss"
        elif 'gain' in habit or 'bulk' in habit:
            trans_habit = "Weight Gain"
        elif 'water' in habit or 'hydrat' in habit:
            trans_habit = "Hydration"
        elif 'maintain' in habit or 'maintenance' in habit:
            trans_habit = "Maintain Weight"
        elif 'gym' in habit:
            trans_habit = "Gym"
        elif 'cardio' in habit or 'run' in habit or 'bike' in habit or 'cycle' in habit:
            trans_habit = "Cardio"
        elif 'custom' in habit:
            pass

        elif habit == 'back':
            return -1

        
        verif = ""
        
        while verif.lower() != 'yes' and verif.lower() != 'y' and verif.lower() != 'no' and verif.lower() != 'n': ## asks if the habit translator was correct; if so, adds to habit list and creates a new habit object
            
            verif = input(f"Would you like to begin a '{trans_habit}' Habit?  --->  ")
            if verif.lower() == 'yes' or verif.lower() == 'y':
                print(f"Great! '{trans_habit}' added to your habits list.")
                h = Habit(trans_habit) #creates a new habit object
                self.user_habitLyst.append(h) #adds habit object to the user's list of habits
                return True
                #print(self.habitLyst)
            elif verif.lower() == 'no' or verif.lower() == 'n' or verif.lower() == "back":
                print("Ok! For a full list of recognized habits, type 'habits'.")
                return False
            elif verif.lower() == "exit":
                return -1
            else:
                print("Sorry, I didn't understand. Try typing 'Yes' or 'No'.")

    def maintenance(self, user):
        self.BMR_var = round(BMR(self.weight_kg, self.height_cm, self.age))
        self.caloric_var = round(self.BMR_var * (1.2 + (0.07 * self.exercise_scale)))
        print(f"Your recommended daily caloric maintenance is {self.BMR_var}.\n")
        time.sleep(1.5)
        print(f"However, many factors can affect caloric needs such as muscle mass, genetics, weather, and diet.\n")
        time.sleep(1.5)
        print(f"Based on your answers, here is an  estimation of your average daily caloric maintenance --- {self.caloric_var} kcal.")
        time.sleep(1.5)
        print(f"Additionally, a caloric range might be more helpful for tracking purposes --- {round(self.caloric_var) - 200} - {round(self.caloric_var) + 200} kcal")
        time.sleep(1.5)

        
        def BMR(self, weight, height, age): # need to add male/female var
            BMR = round(10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age + 5)
            return BMR


class Habit(object):
    def __init__(self, habit):
        self.habit = habit
    def __str__(self):
        return f"{self.habit}"
    def __repr__(self):
        return f"{self.habit}"
        
        










def main():
    n = input("Please enter your name: ")
    
    conn = connect_to_db()   # Connect to the database
    
    if conn:
        # Create the table if not exists; (will likely only matter  on the first run)
        create_users_table(conn)
        create_habits_table(conn)
        if check_name_exists(conn,n) == False:
        
            email = input("Enter your email: ") #email is unique; raises error if dup email is entered
            insert_user(conn, n, email)         #Inserts a user
        else:
            print("Debugggggg")
        
        close_connection(conn)              # Close the connection

        c = Dashboard(n)
        if True:
            c.start()
        else:
            c.main_menu(n)

if __name__ == '__main__':
    main()
    
     
    # if name in database, access data; else: run start function
    # postgresql tutorial: https://www.datacamp.com/tutorial/tutorial-postgresql-python 
    # postgres commands: https://hasura.io/blog/top-psql-commands-and-flags-you-need-to-know-postgresql 
    
    
    
    
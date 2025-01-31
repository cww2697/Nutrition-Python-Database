#NAME: Cody West,
#DATE: 11/30/2017
#COURSE: CS1411-105
#
#GIVEN: BMR and DCN ratios and equations
#
#ANAYLIS:
#input: Patient name, and information
#output: daily calory need and BMR
#
#TEST CASES:
#Test 1:
##input: invalid file
##output: Invalid file - Please try again.
#
#Test 2:
##input: Client New in loading an exisitng client
##output:Please enter the client's name: Client New
###Name: Client New
###Age: 18
###Is this the right client? (y or n): y
###Name: Client New
###Age: 18 years
###Sex: M
###Weight: 180.0 lbs.
###Height: 70.0 in.
###Activity Level: 5
###Would you like to use this information? (y or n): y
#
#Test 3:
##input: Create New Client
##output:
###Please enter the client's first name: New
###Please enter the client's last name: Client
###Is the client Male or Female (M or F)?:M
###Please enter the client's age: 25
###Please enter the client's weight in pounds: 150
###Please enter the client's height in inches: 70
###Please enter the client's activity level (1-5): 5
#
#Test 4:
##nput: Food Selection
#output:
###What would you like to do? 4
###French Fries [570, 30]
###Onion Rings [350, 16]
###Hamburger [670, 39]
###Cheeseburger [760, 47]
###Grilled Chicken Sandwich [420, 10]
###Egg Biscuit [300, 12]
###Mozzarella Sticks [849, 56]
###Cheese Pizza [300, 11]
###Macaroni and Cheese [300, 7]
###Glazed Chicken and Veggies [497, 7]
###Do you want to make a food menu? Choose a food name
###food name: Egg Biscuit
###Egg Biscuit is not good
#
#Test 5:
#input: save and exit
#output:{'Client Other': ['Client Other', 'F', '140', 140.0, 70.0, 1, 1495.0, 1794.0]}
#
#METHOD/ALGORITHM:
#read dictionary function
#sets the name of the file as a string
#opens the file for reading
#evaluates the file
#returns the dictionary to calling function
#if the input is invalid print this
#starts the function again
#creates function to determine the BMR of the client, Type should be a string
#weight, height, and age all should be floating point numbers
#if statement to find the male client's BMR
# #if statement to find the female client's BMR
#return the calculated BMR to the calling statement
#Takes client activity level and BMR
## and determines Daily Calorie Need (DCN)
## based on those factors
#returns DCN to calling statement
#Looks up client information
#asks for input
#creates a list from the dictionary
#Varifies client name and age before displaying
#Moves on to the BMR/DCN Calculator
#returns to menu
#restarts lookup function
#creates function for creating clients
#creates string from client's first name
#creates string from client's last name
#creates string from client's sex
#creates string from client's age
#creates string from client's weight
#creates string from client's height
#creates string from activity
#combines names into one string
#creates blank list
#creates dictionary key
#creates dictionary value
#sets the keys equal to the values
#returns the edited dictionary
#opens file for writing
#writes the dictionary to the file
#looks up patient
#sets the key equal to the patient name
#finds the BMR
#finds the DCN
#Add patient and mutiply by the minimun percentage
#Add patient and multiply by the maximum percentage
#prints the BMR and DCN
#sets the key equal to the patient
#Creates a dictionary of food menu choices
#Print dictionary key and value, row by row
#Ask user if they chose to make a food menu
#Display the food name
#From food dictionary display Calories
#From food dictionary display fat
#Foodfat should be less than not be less than .20 and not greater than .30
#print the name of the food, if good or not
#Creates a dictionary of food menu choices
#creates the dictionary from the loaded file
#starts the menu, and records changes to the dictionary

#PROGRAM:
def read_dictionary_file():                                     #edited read dictionary function
    try:
        initial_file = input('What file should be loaded?: ')       #sets the name of the file as a string
        with open(initial_file,'r') as inf:                         #opens the file for reading
            dict_from_file = eval(inf.read())                       #evaluates the file
            #print(dict_from_file)

        return dict_from_file                                       #returns the dictionary to calling function
    except:
        print('Invalid file - Please try again.')                   #if the input is invalid print this
        read_dictionary_file()                                      #starts the function again

def BMRfunc(list):                      #creates function to determine the BMR of the client, Type should be a string
                                        #weight, height, and age all should be floating point numbers

    type = list[1]
    age = float(list[2])
    weight = float(list[3])
    height = float(list[4])
    BMR = 0

    if type == 'm' or type == 'M':                      #if statement to find the male client's BMR
        BMR=66+(6.23*weight)+(12.7*height)-(6.8*age)
    if type == 'f' or type == 'F':                      #if statement to find the female client's BMR
        BMR = 655+(4.35*weight)+(12.7*height)-(4.7*age)

    return BMR                                          #return the calculated BMR to the calling statement

def dcnfunc(list,BMR):                                  #Takes client activity level and BMR
                                                        ## and determines Daily Calorie Need (DCN)
                                                        ## based on those factors
    Activity_Level = int(list[5])
    BMR = float(BMR)

    cal_calculation = 0
    if Activity_Level == 1:
        cal_calculation = 1.2 * BMR
    elif Activity_Level == 2:
        cal_calculation = 1.375 * BMR
    elif Activity_Level == 3:
        cal_calculation = 1.55 * BMR
    elif Activity_Level == 4:
        cal_calculation = 1.725 * BMR
    elif Activity_Level == 5:
        cal_calculation = 1.9 * BMR

    return cal_calculation                                      #returns DCN to calling statement

def client_lookup_func(dictionary):                             #Looks up client information
    lookup = input('Please enter the client\'s name: ')         #asks for input
    lookup_list = dictionary[lookup]                            #creates a list from the dictionary

    #Assign variables from the list
    client_name = lookup_list[0]
    client_sex = lookup_list[1]
    client_age = lookup_list[2]
    client_weight = lookup_list[3]
    client_height = lookup_list[4]
    client_activity = lookup_list[5]


    print('Name:',client_name)
    print('Age:',client_age)
    right_client = input('Is this the right client? (y or n): ')        #Varifies client name and age before displaying
    if right_client == 'y':
        print('Name:', client_name)
        print('Age:', client_age,'years')
        print('Sex:',client_sex)
        print('Weight:',client_weight,'lbs.')
        print('Height:',client_height,'in.')
        print('Activity Level:',client_activity)
        clinic_use = input('Would you like to use this information? (y or n): ')
        if clinic_use == 'y':
            return lookup_list                                          #Moves on to the BMR/DCN Calculator
        elif clinic_use == 'n':
            main_menu(dictionary)                                            #returns to menu
    if right_client == 'n':
        client_lookup_func(dictionary)                                  #restarts lookup function


def create_client(dictionary):                                                  #creates function for creating clients
    client_name_first = input('Please enter the client\'s first name: ')        #creates string from client's first name
    client_name_last = input('Please enter the client\'s last name: ')          #creates string from client's last name
    client_sex = input('Is the client Male or Female (M or F)?:')               #creates string from client's sex
    client_age = input('Please enter the client\'s age: ')                      #creates string from client's age
    client_weight = float(input('Please enter the client\'s weight in pounds: '))  #creates string from client's weight
    client_height = float(input('Please enter the client\'s height in inches: '))  #creates string from client's height
    client_activity_level = int(input('Please enter the client\'s activity level (1-5): ')) #creates string from activity
    client_name = client_name_first+' '+client_name_last                        #combines names into one string
    client = []                                                                 #creates blank list

    #appends list with values
    client.append(client_name)
    client.append(client_sex)
    client.append(client_age)
    client.append(client_weight)
    client.append(client_height)
    client.append(client_activity_level)


    key = client_name                                                           #creates dictionary key
    value = client[0:]                                                          #creates dictionary value
    #print(client)
    dictionary[key] = value                                                     #sets the keys equal to the values
    return dictionary                                                           #returns the edited dictionary


def write_file(client_dict):                                #creates a writing function
    file = input('Please input a file to save to: ')        #creates a variable with file name
    with open(file, 'w') as file:                           #opens file for writing
        file.write(str(client_dict))                        #writes the dictionary to the file


def main_menu(dictionary, food_dict):
    using = True
    patient = ''
    while using == True:
        print('1. Load New File')
        print('2. Create New Client')
        print('3. Client Lookup/ BMR and Daily Calorie Calculator')
        print('4. Food Selection')
        print('5. Exit')

        user_selection = int(input('What would you like to do? '))
        if user_selection == 1:
            dictionary = read_dictionary_file()
        elif user_selection == 2:
            dictionary = create_client(dictionary)
        elif user_selection == 3:
            patient = client_lookup_func(dictionary)                          #looks up patient
            #print(patient)
            key = patient[0]                                                  #sets the key equal to the patient name
            BMR = BMRfunc(patient)                                            #finds the BMR
            DCN = dcnfunc(patient,BMR)                                        #finds the DCN
            '''The following 4 Functions append the list'''
            patient.append(BMR)
            patient.append(DCN)
            patient.append( .2 * int(patient[7]))                             #Add patient and mutiply by the minimun percentage
            patient.append( .3 * int(patient[7]))                             #Add patient and multiply by the maximum percentage
            '''-----------------------------------------'''

            print(patient[0],'has a BMR of',patient[6],'and a Daily Calorie Need of',patient[7])    #prints the BMR and DCN
            dictionary[key] = patient                                                               #sets the key equal to the patient
        elif user_selection == 4:
                #Creates a dictionary of food menu choices
            food_dict = {'French Fries':[570 , 30],'Onion Rings':[350,16], 'Hamburger':[670,39],'Cheeseburger':[760,47],
                 'Grilled Chicken Sandwich':[420,10],'Egg Biscuit':[300,12],'Mozzarella Sticks':[849,56],
                 'Cheese Pizza':[300,11],'Macaroni and Cheese':[300,7],'Glazed Chicken and Veggies':[497,7]}

            for key, value in food_dict.items():                              #Print dictionary key and value, row by row
                 print(key, value)
            print("Do you want to make a food menu? Choose a food name")      #Ask user if they chose to make a food menu
            food_name = input("food name: ")                                  #Display the food name
            foodCal= food_dict[food_name][0]                                  #From food dictionary display Calories
            foodFat= food_dict[food_name][1]                                  #From food dictionary display fat

            if (foodCal > patient[7] or foodFat>patient[9] or foodFat<patient[8]):  #Foodfat should be less than not be less than .20 and not greater than .30
                print(food_name,"is not good")                                     #print the name of the food, if good or not
            else:
                print(food_name, "is good")

        elif user_selection == 5:
            write_file(dictionary)
            using = False

#Creates a dictionary of food menu choices
food_menu = {'French Fries':[570 , 30],'Onion Rings':[350,16], 'Hamburger':[670,39],'Cheeseburger':[760,47],
             'Grilled Chicken Sandwich':[420,10],'Egg Biscuit':[300,12],'Mozzarella Sticks':[849,56],
             'Cheese Pizza':[300,11],'Macaroni and Cheese':[300,7],'Glazed Chicken and Veggies':[497,7]}


client_dict = read_dictionary_file()                #creates the dictionary from the loaded file
main_menu(client_dict, food_menu)                                   #starts the menu, and records changes to the dictionary

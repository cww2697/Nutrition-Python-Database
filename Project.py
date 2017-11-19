def read_dictionary_file(file_name):            #creates function to load file
    client_dict = {}                            #creates a blank client dictionary
    with open(file_name,'r') as client_file:    #opens the file for reading
        for line in client_file:                #creates a for loop to read lines from the file
            x=line.strip('\n').split(',')       #strips the lines of "\n" and splits the lines at commas
            key=x[0]                            #uses the first value to create the dictionary key
            val = x[0:]                         #creates the values list for the dictionary
            client_dict[key] = val              #creates the dictionary

        return client_dict                      #returns the client dictionary to the calling function


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
            menu(dictionary)                                            #returns to menu
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
    dictionary[key] = value                                                     #sets the keys equal to the values
    return dictionary                                                           #returns the edited dictionary

##Food Menu Function

def menu(dictionary):
    using = True
    list = []
    while using == True:
        print('1. Load New File')
        print('2. Create New Client')
        print('3. Client Lookup/ BMR and Daily Calorie Calculator')
        print('5. Exit')

        user_selection = int(input('What would you like to do? '))
        if user_selection == 1:
            dictionary = read_dictionary_file(input('Please enter the file name: '))
        elif user_selection == 2:
            dictionary = create_client(dictionary)
        elif user_selection == 3:
            list = client_lookup_func(dictionary)
            key = list[0]
            BMR = BMRfunc(list)
            DCN = dcnfunc(list,BMR)
            list.append(BMR)
            list.append(DCN)
            print(list[0],'has a BMR of',list[6],'and a Daily Calorie Need of',list[7])
            dictionary[key] = list
        # elif user_selection == 4

#Creates a dictionary of food menu choices
food_menu = {'French Fries':[570 , 30],'Onion Rings':[350,16], 'Hamburger':[670,39],'Cheeseburger':[760,47],
             'Grilled Chicken Sandwich':[420,10],'Egg Biscuit':[300,12],'Mozzarella Sticks':[849,56],
             'Cheese Pizza':[300,11],'Macaroni and Cheese':[300,7],'Glazed Chicken and Veggies':[497,7]}

initial_file = input('What file should be loaded? ')            #Asks user what file to load
client_dict = read_dictionary_file(initial_file)                #creates the dictionary from the loaded file
menu_dict = menu(client_dict)                                   #starts the menu, and records changes to the dictionary

 #write the full meaning and specify the regions they represent

sw_morning = ["a. jollof rice", "b. white rice", "c. bread and tea", "d. pap", "e. fried rice"]
sw_afternoon = ["a. roasted plantain", "b. fufu and egusi", "c. bean cake", "d. beans and dodo", "e. beans pudding"]
sw_evening = ["a. peppersoup", "b. eba", "c. plantain porridge", "d. pounded yam", "e. amala" ]

ss_morning = ["a. edikaikong", "b. afang", "c. ofeakwu", "d. ugba", "e. oha"]
ss_afternoon = ["a. ogbona", "b. bitterleaf soup", "c. pepper soup", "d. banga soup", "e. abacha"]
ss_evening = ["a. nsala", "b. ukwa", "c. isiewu", "d. nkwobi", "e. abacha"]

north_morning = ["a. danwake", "b. kunu", "c. awara", "d. taliyar", "e. masa"]
north_afternoon = ["a. tuwo masara", "b. tuwo shinkafa", "c. gurasa", "d. dambun kaza", "e. fura de nunu"]
north_evening = ["a. shinkafa de wake", "b. fate", "c. gumba", "d. awara", "e. cous cous alele", "f. tuwon alakama"]

all_meals = ["1. jollof rice", "2. white rice", "3. bread and tea", "4. pap", "5. fried rice", "6. roasted plantain", "7. fufu and egusi", "8. beancake", "9. beans dodo", "10. beans pudding", "11. peppersoup", "12. eba", "13. plantain porridge", "14. pounded yam", "15. amala", "16. edikaikong", "17. afang", "18. ofeakwu", "19. ugba", "20. oha", "21. ogbona", "22. bitterleaf soup", "23. pepper soup", "24. banga soup", "25. abacha", "26. nsala", "27. ukwa", "28. isiewu", "29. nkwobi", "30. abacha", "31. danwake", "32. kunu", "33. awara", "34. taliyar", "35. masa", "36. tuwo masara", "37. tuwo shinkafa","38. gurasa", "39. dambun kaza", "40. fura de nunu", "41. shinkafa de wake", "42. fate", "43. gumba", "44. awara", "45. cous cous alele", "46. tuwon alakama \n"]

locations = ["1. south_west 2. south-south 3. south-east 4. north"]
time_of_the_day = ["1. morning", "2. afternoon", "3. evening"]

def meal_options():
    #This function takes a meal option input and displays your input.
    meal_option = (input('Choose a meal \n'))
    ordered_meal_list.append(meal_option)
    print('\nYour ordered meal is option {}'.format(ordered_meal_list))

ordered_meal_list = []

def meal(customer_location,time):
    #This function takes name input, suggests location and takes input for selected location. it also suggest meals based on the location.
    name = (input("What is your name? \n"))
    print('\nHello {}, choose your location\n'.format(name))

    location =int(input("1. south_west \n2. south-south \n3. south-east \n4. north \n"))

    time_of_order = int(input("\nChoose the time of the day \n1. morning \n2. afternoon \n3. evening \n"))

    
    if location == 1 and time_of_order == 1:
        print("\nMeal options")
        for x in sw_morning:
            print(x)
        meal_options()

    elif location == 1 and time_of_order == 2:
        print("\nMeal options")
        for x in sw_afternoon:
            print(x)
        meal_options()

    elif location == 1 and time_of_order == 3:
        print("\nMeal options")
        for x in sw_evening:
            print(x)
        meal_options()

    elif location == 2 or location == 3 and time_of_order == 1:
        print("\nMeal options")
        for x in ss_morning:
            print(x)
        meal_options()

    elif location == 2 or location == 3 and time_of_order == 2:
        print("\nMeal options")
        for x in ss_afternoon:
            print(x)
        meal_options()
        
    elif location == 2 or location == 3 and time_of_order == 3:
        print("\nMeal options") 
        for x in ss_evening:
            print(x)
        meal_options()
    
    elif location == 4 and time_of_order == 1:
        print("\nMeal options")
        for x in north_morning:
            print(x)
        meal_options()  

    elif location == 4 and time_of_order == 2:
        print("\n Meal options")
        for x in north_afternoon:
            print(x)
        meal_options()

    elif location == 4 and time_of_order == 3:
        print("\nMeal options:")
        for x in north_evening:
            print(x)
        meal_options()

    else:
        print('Invalid option! please try again \n')
        meal(customer_location=locations,time=time_of_the_day)
        
meal(customer_location=locations,time=time_of_the_day)

def more_foods():
    #This function request if you are interested in more food, it prints out a list of all available foods.
    more_food = (input('Will you like to eat some more food? Y/N \n')).upper()
    if more_food == "Y":
        for x in all_meals:
            print(x)
        meal_option = int(input('Choose a meal \n'))
        ordered_meal_list.append(meal_option)
        print('\nYour ordered meals are options {}'.format(ordered_meal_list))
        print('\nThanks for using ZIYTECHS program')
        
    elif more_food == "N":
         print('\nThanks for using ZIYTECHS program')

    else:
        print('\nInvalid option! please try again \n')
        more_foods()
more_foods()



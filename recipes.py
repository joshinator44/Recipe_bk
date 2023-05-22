#!/usr/bin/env python3
from urllib import request, parse
from recipe_objects import Category, Area, Meal
import recipe_objects
import json
import ssl
import textwrap

ssl._create_default_https_context = ssl._create_unverified_context

def show_title():
    "Display the title"
    
    print("My Recipes Program")
    print()

def show_menu():
    """
        This method displays the menu to screen"
    """
    print()
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all areas")
    print("6 - Search Meals by area")
    print("7 - Menu")
    print("0 - Exit the program\n\n")

def get_input():
    "Get the users input from the menu"
    put = input("Command: ").strip()
    if put == "1":
        recipe_category()
    elif put == "2":
        meal_category()
    elif put == "3":
        get_meal_info()
    elif put == "4":
        random_meal()
    elif put == "5":
        meal_area()
    elif put == "6":
        search_meal_area()
    elif put == "7":
        show_menu()
    elif put == "0":
        print("Thank you for dining with us!")
        return False
        
        
    else:
        print("This command is not valid")
    return True

def recipe_category():
    "Display each category"
    
    url = "https://www.themealdb.com/api/json/v1/1/categories.php"
    file = request.urlopen(url)
    meal_info = json.loads(file.read())
    categories = []
    for num in meal_info['categories']:
        category = Category(num['idCategory'], num['strCategory'], num['strCategoryThumb'], num['strCategoryDescription'])
        categories.append(category)
    for category in categories:
        print("    " + category.get_name())
        
        
        
def meal_category():
    "Allow user to search for a category and get the meals"
    
    category = input("Enter a category: ")
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category.strip().lower()
    file = request.urlopen(url)
    meal_info = json.loads(file.read())
    print(category.upper() + " MEALS:")
    if meal_info['meals'] == None:
        print("This is not a valid input.")
        return
    meals = []
    for num in meal_info['meals']:
        print("    " + num['strMeal'])
def meal_from_dictionary(meal_dictionary):
    "Dictionary of all keys for the JSON file"

    meal = Meal(
        meal_dictionary['idMeal'], 
        meal_dictionary['strMeal'], 
        meal_dictionary['strDrinkAlternate'], 
        meal_dictionary['strCategory'],
        meal_dictionary['strArea'], 
        meal_dictionary['strInstructions'], 
        meal_dictionary['strMealThumb'], 
        meal_dictionary['strTags'],
        meal_dictionary['strYoutube'], 
        meal_dictionary['strSource'], 
        meal_dictionary['strImageSource'], 
        meal_dictionary['strCreativeCommonsConfirmed'],
        meal_dictionary['dateModified'], 
        meal_dictionary['strIngredient1'], 
        meal_dictionary['strIngredient2'], 
        meal_dictionary['strIngredient3'],
        meal_dictionary['strIngredient4'], 
        meal_dictionary['strIngredient5'], 
        meal_dictionary['strIngredient6'], 
        meal_dictionary['strIngredient7'],
        meal_dictionary['strIngredient8'], 
        meal_dictionary['strIngredient9'], 
        meal_dictionary['strIngredient10'], 
        meal_dictionary['strIngredient11'], 
        meal_dictionary['strIngredient12'],  
        meal_dictionary['strIngredient13'], 
        meal_dictionary['strIngredient14'], 
        meal_dictionary['strIngredient15'], 
        meal_dictionary['strIngredient16'], 
        meal_dictionary['strIngredient17'], 
        meal_dictionary['strIngredient18'], 
        meal_dictionary['strIngredient19'], 
        meal_dictionary['strIngredient20'], 
        meal_dictionary['strMeasure1'], 
        meal_dictionary['strMeasure2'], 
        meal_dictionary['strMeasure3'], 
        meal_dictionary['strMeasure4'], 
        meal_dictionary['strMeasure5'], 
        meal_dictionary['strMeasure6'], 
        meal_dictionary['strMeasure7'], 
        meal_dictionary['strMeasure8'],
        meal_dictionary['strMeasure9'], 
        meal_dictionary['strMeasure10'], 
        meal_dictionary['strMeasure11'], 
        meal_dictionary['strMeasure12'], 
        meal_dictionary['strMeasure13'], 
        meal_dictionary['strMeasure14'],      
        meal_dictionary['strMeasure15'], 
        meal_dictionary['strMeasure16'], 
        meal_dictionary['strMeasure17'], 
        meal_dictionary['strMeasure18'], 
        meal_dictionary['strMeasure19'], 
        meal_dictionary['strMeasure20'])
    return meal
def display_meal(meal):
    "Format the meals and print the meal"
    recipe_name = "\nRecipe Name: {}\n".format(meal.get_strMeal())
    wrapper = textwrap.TextWrapper(width = 80)
    instructions  = wrapper.wrap("Instructions: " + meal.get_strInstructions()) 
    print(recipe_name)
    for line in instructions:
        print(line)
    
    for num in range(len(meal.get_ingredients())):
        print(meal.get_measurements()[num] + " " + meal.get_ingredients()[num])
def get_meal_info():
    "Allow user to search a meal by name"
    
    meal_name = input("Enter a meal: ")
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s="+meal_name.strip().lower().replace( " ", "_")
    file = request.urlopen(url)
    meal_info = json.loads(file.read())
    meals = []
    if meal_info['meals'] == None:
        print("This is not a valid input.")
        return
    
    
    for meal_dictionary in meal_info['meals']:
        meal = meal_from_dictionary(meal_dictionary)
                            
        meals.append(meal)
        
    for meal in meals:
        display_meal(meal)

            
        
        
        
                                                                    
                                            
def random_meal():
    "Display a random meal"
    
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    file = request.urlopen(url)
    meal_info = json.loads(file.read())
    for meal_dictionary in meal_info['meals']:
        meal = meal_from_dictionary(meal_dictionary)
        display_meal(meal)
def meal_area():
    "Display all meal areas"
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    file = request.urlopen(url)
    meal_info = json.loads(file.read())
    print("AREAS: ")
    for dictionary in meal_info['meals']:
        area = Area(dictionary['strArea'])
        print("    " + area.get_area())
        
def search_meal_area():
    "Search for a specific area and display that areas meals"
    area = input("Enter a Area: ")
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area.strip().lower()
    file = request.urlopen(url)
    meal_info = json.loads(file.read())
    print(area.upper() + " MEALS:")
    if meal_info['meals'] == None:
        print("This is not a valid input.")
        return
    for num in meal_info['meals']:
        print("    " + num['strMeal'])

    
def main():
    show_title()
    show_menu()
    while get_input():
        pass
            
            
        
if __name__ == "__main__":
    main()


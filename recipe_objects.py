class Category:
    def __init__(self,idnum, name, thumbnail, description):
        self.__id = idnum
        self.__name = name
        self.__thumbnail = thumbnail
        self.__description = description
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_thumbnail(self):
        return self.__thumbnail
    def get_description(self):
        return self.__description


class Area:
    def __init__(self, strArea):
        self.__strArea = strArea
    def get_area(self):
        return self.__strArea
class Meal:
    def __init__(self, idMeal,strMeal,strDrinkAlternate,strCategory,strArea,strInstructions,strMealThumb,strTags,strYoutube,strSource,strImageSource,strCreativeCommonsConfirmed,
             dateModified,strIngredient1,strIngredient2,strIngredient3,strIngredient4,strIngredient5, strIngredient6, strIngredient7, strIngredient8, strIngredient9,
             strIngredient10, strIngredient11, strIngredient12, strIngredient13, strIngredient14, strIngredient15, strIngredient16, strIngredient17, strIngredient18,
             strIngredient19, strIngredient20, strMeasure1, strMeasure2, strMeasure3, strMeasure4, strMeasure5, strMeasure6, strMeasure7, strMeasure8, strMeasure9, strMeasure10,
             strMeasure11, strMeasure12, strMeasure13, strMeasure14, strMeasure15, strMeasure16, strMeasure17, strMeasure18, strMeasure19, strMeasure20):
        self.__ingredientList = []
        self.__ingredientList.extend([strIngredient1, strIngredient2, strIngredient3, strIngredient4, strIngredient5, strIngredient6, strIngredient7, strIngredient8,
                                     strIngredient9, strIngredient10, strIngredient11, strIngredient12, strIngredient13, strIngredient14, strIngredient15, strIngredient16,
                                     strIngredient17, strIngredient18, strIngredient19, strIngredient20])
        self.__measurementList = []
        self.__measurementList.extend([strMeasure1, strMeasure2, strMeasure3, strMeasure4, strMeasure5, strMeasure6, strMeasure7, strMeasure8, strMeasure9, strMeasure10, strMeasure11,
             strMeasure12, strMeasure13, strMeasure14, strMeasure15, strMeasure16, strMeasure17, strMeasure18, strMeasure19, strMeasure20])
        self.__idMeal = idMeal
        self.__strMeal = strMeal
        self.__strDrinkAlternate = strDrinkAlternate
        self.__strCategory = strCategory
        self.__strArea = strArea
        self.__strInstructions = strInstructions
        self.__strMealThumb = strMealThumb
        self.__strTags = strTags
        self.__strYoutube = strYoutube
        self.__strSource = strSource
        self.__strImageSource = strImageSource
        self.__strCreativeCommonsConfirmed = strCreativeCommonsConfirmed
        self.__dateModified = dateModified
        if None in self.__ingredientList:
            last = self.__ingredientList.index(None)


        else:
            try:
                last = self.__ingredientList.index("")
            except(ValueError):
                last = len(self.__ingredientList)
        self.__ingredientList = self.__ingredientList[:last]
        self.__measurementList = self.__measurementList[:last]
      
        
        
        
        
        pass
    def get_idMeal(self):
        return self.__idMeal
    def get_strMeal(self):
        return self.__strMeal
    def get_strDrinkAlternate(self):
        return self.__strDrinkAlternate
    def get_strCategory(self):
        return self.__strCategory
    def get_strArea(self):
        return self.__strArea
    def get_strInstructions(self):
        return self.__strInstructions
    def get_strMealThumb(self):
        return self.__strMealThumb
    def get_strTags(self):
        return self.__strTags
    def get_strYoutube(self):
        return self.__strYoutube
    def get_strSource(self):
        return self.__strSource
    def get_strImageSource(self):
        return self.__strImageSource
    def get_strCreativeCommonsConfirmed(self):
        return self.__strCreativeCommonsConfirmed
    def get_dateModified(self):
        return self.__dateModified
 
    def get_ingredients(self):
        return self.__ingredientList
    def get_measurements(self):
        return self.__measurementList
    
    
    
    
               


        



"""

{'idCategory': '1', 'strCategory': 'Beef', 'strCategoryThumb': 'https://www.themealdb.com/images/category/beef.png', 'strCategoryDescription': 'Beef is the culinary name for meat from cattle, particularly skeletal muscle.
 Humans have been eating beef since prehistoric times.[1] Beef is a source of high-quality protein and essential nutrients.[2]'}


"""







                 

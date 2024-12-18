class Recipe:
    def __init__(self, ingredients="", instructions=""):
        self.ingredients = ingredients or "Ingredients not available"
        self.instructions = instructions or "Instructions not available"
    
    #to get the ingredients
    def get_ingredients(self):
        return self.ingredients

   #to get the instructions
    def get_instructions(self):
        return self.instructions

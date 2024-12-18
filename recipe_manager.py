from recipe import Recipe

class RecipeManager:
    def __init__(self):
        self.recipes = {}
        self.load_recipes()

    def load_recipes(self):
        # Default recipes
        self.recipes["ginisang sayote"] = Recipe(
            "\n- 2 large sayote(or 3 medium)\n- 300grams ground pork\n- 3 medium tomatoes\n- 1 medium onion\n- 4 cloves garlic\n- salt and pepper to taste\n- 1 pc pork broth crube\n- 1/2 cup water\n- patis to taste",
            "\n1. Balatan,then alisin ang buto ng sayote.then,Hiwain into slices,hugasan then set aside.\n\n2. Sa isang pan, ilagay ang ground pork. isangkutsa ito hanggang magbrown at magmantika at lumabas ang sariling mantika. Saka ito ilagay sa bawang,sibuyas at tomatoes. igisa ng ilang minuto. Then lagyan ng kaunting water at pork broth cube. Takpan at lutuin ng 10 minutes gamit ang medium low heat.\n\n3. After 10 mintues ilagay na ang sayote. Lutuin ito ng ilang minuto hanggang maging half cooked. Timplahan ng asin at paminta depende sa alat na gusto mo. Kapag medyo malambot na ang sayote, okay na ito."
        )
        self.recipes["pizza"] = Recipe(
            "\n- Pizza dough\n- Tomato sauce\n- Mozzarella cheese\n- Toppings of choice",
            "\n1. Roll out the pizza dough.\n2. Spread tomato sauce evenly.\n3. Add mozzarella and toppings.\n4. Bake in the oven at 220°C for 15 minutes."
        )
        self.recipes["sinarsahang manok"] = Recipe(
            "\n- 1kilo chicken(thighs and drumstick)\n- 1 cup Sprite\n- 1 medium onion\n- 5 cloves garlic\n- 1 teaspoon salt\n- 1 teaspoon pepper\n- 1/4 cup soy sauce\n- 1/2 cup green peas\n- 1/3 cup tomato sauce\n- red and green bellpepper oil for sauteing",
            "\n1. Timplahan ng kaunting asin at paminta ang manok., tomato.\n\n2. Sa isang kawali magpainit ng kaunting mantika. Saka iprito ng bahagya ang manok hanggang magbrown both sides.\n\n3. Saka igisa ang bawang at sibuyas hanggang bumango ito. Saka ibalik ang manok. Lagyan ng sprite at soy sauce. Lutuin ng 15 minutes using medium heat\n\n4. After 15 minutes at kaunti na ang sauce,grean peas at bellpeper. Lutuin pa ng ilang minuto hangang sa lumapot ang sauce."
        )
    #to get recipe
    def get_recipe(self, food_name):
        return self.recipes.get(food_name)
    
    #to add ingredients
    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = Recipe(ingredients, instructions)

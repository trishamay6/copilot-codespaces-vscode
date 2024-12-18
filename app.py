import tkinter as tk
from tkinter import messagebox, simpledialog
from recipe_manager import RecipeManager

class RecipeFinderApp:
    def __init__(self, root):
        #ui for Recipe Finder
        self.root = root
        self.root.title("Recipe Finder")
        self.root.geometry("600x500")

       

        self.recipe_manager = RecipeManager()

        #mainframe
        self.mainframe = tk.Frame(self.root, bg="violet")
        self.mainframe.pack(fill="both", expand=True)

        #design for title
        self.titleLabel = tk.Label(self.mainframe, text="Recipe Finder", font=("Comic Sans", 18, "bold"), bg="violet")
        self.titleLabel.pack(pady=20)

        #output for recipe and instruction
        self.displayOutput = tk.Text(self.mainframe, width=70, height=15, wrap=tk.WORD, state=tk.DISABLED)
        self.displayOutput.pack(pady=10)

        #design for inputs(Search bar,Search button)
        self.inputFrame = tk.Frame(self.mainframe, bg="violet")
        self.inputFrame.pack(pady=10)

        
        self.inputlabel = tk.Label(self.inputFrame, text="Enter Recipe Name:", bg="violet")
        self.inputlabel.grid(row=0, column=0, padx=5)

        
        self.SearchBar = tk.Entry(self.inputFrame, width=30)
        self.SearchBar.grid(row=0, column=1, padx=5)

        
        self.searchButton = tk.Button(self.inputFrame, text="Search", command=self.searchRecipe, width=15)
        self.searchButton.grid(row=0, column=2, padx=5)

        #frame for another button(add recipe, exit)
        self.buttonFrame = tk.Frame(self.mainframe, bg="violet")
        self.buttonFrame.pack(pady=10)

        
        tk.Button(self.buttonFrame, text="Add Recipe", command=self.add_recipe_prompt, width=15).grid(row=0, column=0, padx=5)

        
        tk.Button(self.buttonFrame, text="Exit", command=self.root.quit, width=15).grid(row=0, column=1, padx=5)
     
    def searchRecipe(self):
        
        foodName = self.SearchBar.get().strip()
        if not foodName:
            messagebox.showwarning("Input Required", "Please enter a recipe name.")
            return

        recipe = self.recipe_manager.get_recipe(foodName)
        self.displayOutput.config(state=tk.NORMAL)
        self.displayOutput.delete(1.0, tk.END)
        if recipe:
            self.displayOutput.insert(tk.END, f"Recipe for {foodName}:\n\n")
            self.displayOutput.insert(tk.END, "Ingredients:\n")
            self.displayOutput.insert(tk.END, recipe.get_ingredients() + "\n\n")
            self.displayOutput.insert(tk.END, "Instructions:\n")
            self.displayOutput.insert(tk.END, recipe.get_instructions() + "\n")
        else:
            self.displayOutput.insert(tk.END, f"Recipe for {foodName} not found.")
        self.displayOutput.config(state=tk.DISABLED)

    def add_recipe_prompt(self):#opening another window an add new recipe
        
        name = self.SearchBar.get().strip()
        if not name:
            messagebox.showwarning("Input Required", "Please enter a recipe name.")
            return

        ingredients = simpledialog.askstring("Add Ingredients", f"Enter Ingredients for {name}:")
        if not ingredients:
            return

        instructions = simpledialog.askstring("Add Instructions", f"Enter Instructions for {name}:")
        if not instructions:
            return

        self.recipe_manager.add_recipe(name, ingredients, instructions)
        messagebox.showinfo("Success", f"Recipe for {name} added successfully!")
        self.SearchBar.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeFinderApp(root)
    root.mainloop()

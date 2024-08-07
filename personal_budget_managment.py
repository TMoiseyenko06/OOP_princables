class BudgetCategory():
    def __init__(self,name,budget):
        self.__budget = budget
        self.__starting_budget = budget
        self.name = name

    def add_exspense(self,amount):
        if self.__budget - amount < 0:
            print('Your budget cannot fit this exspense!') 
        else: 
            self.__budget -= amount

    def display_category_summary(self):
        print(f'Category: {self.name} \nStarting budget: {self.__starting_budget} \nAmount spent: {self.__starting_budget - self.__budget} \nBudget remaining: {self.__budget}')

food_category = BudgetCategory("Food",500)
food_category.add_exspense(300)
food_category.display_category_summary()

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}

def insert_coins(required_cost):
    """ 
    Requests the user for input of number of:
        quarters = $0.25 each
        dimes = $0.10 each
        nickles = $0.05 each
        pennies = $0.01 each 
    The function then compares this with the cost of the drink. If the user has not provided enough coins, then the transaction is cancelled.
    If the user has provided more than the required cost, change is provided. 
    """ 
    
    cost_enough = True 
    change = 0 
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles =  int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    total_cost = calculate_cost(quarters,dimes,nickles,pennies)
    if total_cost < required_cost:
        cost_enough = False
    else:
        change = total_cost - required_cost
    return cost_enough,change 
    
def calculate_cost(quarters,dimes,nickles,pennies):
    """
    Calculates the total cost based on the number of quarters, dimes, 
    nickles and pennies inserted.
    """
    total_cost = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01 
    return total_cost 

def retrieve_ingredients(resources):
    """ Retrieve water, milk, and coffee from the given dictionary input. """
    milk = resources["milk"]
    coffee = resources["coffee"]
    water = resources["water"]
    order_ingredients = [water,milk,coffee]
    return order_ingredients
    
def generate_report(resources):
    """Generates a report of the available resources for the coffee machine."""
    print(f'Water: {resources["water"]} ml')
    print(f'Milk: {resources["milk"]} ml')
    print(f'Coffee: {resources["coffee"]} g')
    print(f'Money: ${resources["money"]}')
    
def secret_off_switch():
    coffee_machine_on = False 
    return coffee_machine_on

coffee_machine_on = True 

while coffee_machine_on:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        # 1. Retrieve cost of the espresso, latte or cappuccino 
        drink = MENU[user_input]
        drink_cost = drink["cost"]
        # 2. Ask user to insert coins, calculate total input and see if this is enough 
        cost_enough,change = insert_coins(drink_cost)
        if not cost_enough:
            # End transaction prematurely
            print("Sorry that's not enough. Money refunded.")
        else:
            # Retrieve other dictionary entries for drink item
            order_ingredients = retrieve_ingredients(drink["ingredients"])
            total_ingredients = retrieve_ingredients(resources)
            # Change this code to check if there are enough resources to make the drink 
            insufficient_items = False
            resource_names = ["water","milk","coffee"]
            for i in range(0,len(order_ingredients)):
                if total_ingredients[i] - order_ingredients[i] < 0:
                    print(f"Sorry, there is not enough {resource_names[i]} left.") 
                    insufficient_items = True 
        
            if not insufficient_items:
                # Deduct ingredients consumed and add money to resources
                total_money = resources["money"]
                for i in range(0,3):
                    total_ingredients[i] -= order_ingredients[i]
                total_money += drink_cost 
                resources["water"] = total_ingredients[0]
                resources["milk"] = total_ingredients[1]
                resources["coffee"] = total_ingredients[2]
                resources["money"] = total_money 
                # Give the user change if there is any 
                if change != 0:
                    print(f"Here is ${round(change,2)} in change.")
                
                # Print the drink that they received
                print(f'Here is your {user_input} ???. Enjoy!')
            
    
    elif user_input == "report":
        generate_report(resources)
        
    elif user_input == "off":
        coffee_machine_on = secret_off_switch()
    
    
    
    
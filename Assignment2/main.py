import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        choice = input("What size ham sandwich? (small/medium/large): ").lower()

        if choice == "off":
            break

        elif choice == "report":
            print("Current Resources:")
            for item, amount in resources.items():
                print(f"{item}: {amount}")

        elif choice in recipes:
            selected_sandwich = recipes[choice]
            ingredients = selected_sandwich["ingredients"]
            cost = selected_sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("Invalid choice. Try again.")
if __name__=="__main__":
    main()

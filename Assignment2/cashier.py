class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change}.")
                return True
            else:
                print("Sorry, that is not enough money. Money will be refunded.")
                return False

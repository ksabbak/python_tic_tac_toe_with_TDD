class Controller:
    def run(self):
        print("Welcome!")
        print("this is tic-tac-toe!")
        print("Here are your options: ")
        print("  1. Human vs. Human")
        print("  2. Human vs. Computer")
        print("  3. Computer vs. Computer")
        print("Please enter the number of your selection: ")
        game_choice = input().strip()
        if game_choice in "1":
            return "Human vs. Human!"
        elif game_choice in "2":
            return "Human vs. Computer!"
        else:
            return "Computer vs. Computer!"


import json
import modules

class Game:
    game_dict = {}

    #load game to file
    def load_game(self):
        with open("save.json") as jsonfile:
            self.game_dict = json.load(jsonfile)
        if self.game_dict.get("current_module") == "None":
            return "prologue"
        return self.game_dict.get("current_module")

    #save game to file
    def save_game(self, current_module):
        self.game_dict["current_module"] = current_module
        with open("save.json", "w") as jsonfile:
            json.dump(self.game_dict, jsonfile)

    #Handle when a game ends, ask user whether they want to start a new adventure
    def end_game(self):
        print("\nNew Adventure: yes or no?")
        while True:
            choice = input()
            if choice in ["yes", "y", "Yes", "YES"]:
                return False
            elif choice in ["no", "n", "No", "NO"]:
                return True
            else:
                print("Input either yes or no")

    #The main game loop it runs, loads, and saves modules
    def game_loop(self):
        current_module = self.load_game()
        while True:
            #below is equivalent to: current_module = modules.module_name.func(game_dict)
            #example: current_module = modules.prologue.func(game_dict)
            current_module = getattr(modules, current_module).func(self.game_dict)
            if current_module == "end":
                modules.end.func()
                current_module = "prologue"
                if self.end_game():
                    break
            self.save_game(current_module)
    
    #Handles game start up. Loads game from save and ask whether user wants to continue or start a new game. 
    #Lastly it runs the main game loop method
    def game_start(self):
        current_module = self.load_game()
        if current_module != "prologue":
            while True:
                print("Enter '1' to continue where you left off, enter '2' to start a new game")
                option = int(input())
                if option == 1:
                    break
                elif option == 2:
                    current_module = "prologue"
                    self.save_game(current_module)
                    break
                else:
                    print("Please enter either 1 or 2")
        self.game_loop()
            
game = Game()
game.game_start()
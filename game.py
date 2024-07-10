import json
import modules

class Game:
    game_dict = {}
    def load_game(self):
        with open("save.json") as jsonfile:
            self.game_dict = json.load(jsonfile)
        if self.game_dict.get("current_module") == "None":
            return "prologue"
        return self.game_dict.get("current_module")

    def save_game(self, current_module):
        self.game_dict["current_module"] = current_module
        with open("save.json", "w") as jsonfile:
            json.dump(self.game_dict, jsonfile)

    def game_loop(self):
        current_module = self.load_game()
        while True:
            current_module = getattr(modules, current_module).func(self.game_dict)
            if current_module == "end":
                current_module = "prologue"
                modules.end.func()
                break
            self.save_game(current_module)
        self.save_game(current_module)
    
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
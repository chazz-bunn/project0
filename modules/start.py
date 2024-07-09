def func(dict):
    dict["games_played"] += 1
    choich = ""
    while(True):
        print("Choich 1 or Choich 2?")
        choich = str(input())
        if choich in ["1", "one", "choich 1"]:
            return "choich_one"
        elif choich in ["2", "two", "choich 2"]:
            return "choich_two"
        else:
            print("I don't recognize that option")
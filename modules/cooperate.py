from modules.print_text import print_text

def func(dict):
    print_text('\nPete decided it was best not to defy the guardswomen. He nodded reluctantly. "Okie dokie. I’ll be a good Pete.”\n')

    print_text("\nThe guardswomen led Pete through the towering fungi to their kingdom, a bustling village built among the mushroom stalks. Houses and shops were carved into the caps and stems, and all manner of fantastical people moved about their daily lives, casting curious glances at the newcomer. Pete was locked in a jail cell to await trial.\n")

    print_text("\nTo pass the time, the guards gave him a small, chess-playing robot. It was shorter than Pete, and its face appeared on a touchscreen monitor.\n")

    print_text("\nThe robot beeped and whirred, its movements jerky and hesitant.\n")

    print_text('\n“Greetings, male human child,” the little robot said with a metallic voice. “I’ve been assigned to keep you entertained while your case is reviewed.” A chessboard appeared on its face. “Touch my face to begin.”\n')

    print_text('\nPete approached with fascination. “Chess? Hey, I’ve heard of that game!” Pete played chess with the robot, but it wasn\'t very skilled, and Pete could see it was troubled with self-doubt.\n')

    print_text('\n“Darn it,” the robot would mutter. Groans and sighs of frustration filled the room. Pete began to feel bad for the little robot.\n')

    print_text('\nAs they played, Pete pondered his options: should he easily defeat the robot, showing his superior prowess, or should he go easy and try to lift its spirits?\n')

    choice_one_choices = [
        "defeat",
        "defeat robot",
        "win",
        "superior prowess",
        "show superior prowess"
    ]
    choice_two_choices = [
        "go easy",
        "easy"
        "lose",
        "lift its spirits",
        "lift",
        "lift robot's spirits"
    ]
    while True:
        choice = input()
        if choice in choice_one_choices:
            pass
        elif choice in choice_two_choices:
            pass
        else:
            print_text("\nPick one of the choices.\nShould he win or go easy?\n")
from modules.print_text import print_text
from modules.format_text import format_text

def func(dict):
    print_text("\nPete decided to boost the robot's self-esteem by letting it win, but only just. He made a few subtle mistakes, allowing the robot to capture his pieces and eventually declare victory. The robot's eyes glowed with joy as it made the final move.\n")

    print_text('\n"You played well, male child," the robot beeped, its voice filled with newfound confidence, "I’ve never won a game of chess before, but I bet you were holding back. I’ll keep practicing and challenge you again someday, and you’ll have to give it your all.”\n')

    print_text('\n“You’ve got a deal,” Pete agreed.\n')

    print_text("\nPete smiled, glad to have lifted the robot's spirits. Soon after, the guards came to escort him to his trial. As he entered the courtroom, Pete was taken aback to see the judge—a pig! Not just any pig, but Hamilton, wearing a black robe and powdered wig. Hamilton grunted and snorted as he settled into his judge's seat.\n")

    print_text('\n"Pete, you stand accused of illegal immigration," Hamilton declared, sounding surprisingly authoritative. "How do you plead?" This wasn’t the Hamilton Pete knew.\n')

    print_text('\n“Hamilton, you learned to talk!” Pete explained. “And you got a law degree. Wowie, you’re a fast learner!”\n')

    print_text("\nPete was given a crucial decision: should he represent himself or request an attorney?\n")

    choice_one_choices = [
        "represent himself",
        "represent",
        "himself"
    ]
    choice_two_choices = [
        "request an attorney",
        "request attorney",
        "request",
        "have attorney",
        "attorney"
    ]
    while True:
        choice = input()
        choice = format_text(choice)
        if choice in choice_one_choices:
            return "represent_himself"
        elif choice in choice_two_choices:
            return "request_an_attorney"
        else:
            print_text("\nPick one of the choices.\nShould he represent himself or have an attorney?\n")
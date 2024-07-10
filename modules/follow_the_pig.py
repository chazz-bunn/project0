from modules.print_text import print_text
from modules.format_text import format_text

def func(dict):
    print_text("\nDetermined not to lose sight of Hamilton, Pete decided to follow the pig. He sprinted through the forest, dodging trees and leaping over fallen branches. The chase led him deeper into the woods, where the canopy grew thicker and the light dimmer. He could hear Hamilton's grunts up ahead and pushed himself to run faster, faster, faster.\n")

    print_text("\nJust as he caught up to Hamilton, Pete's foot slipped on a lone mushroom hidden within the leaves. With a yelp, he tumbled down a small hill, rolling head over heels until he came to a stop, bumping his head on a bronze statue of Kenny Loggins, glinting in the sparse sunlight.\n")

    print_text("\nWhen Pete woke up hours later, he found himself in a strange land filled with towering mushrooms, their caps forming a colorful canopy overhead. The air was thick with the earthy scent of fungi, and the ground was soft underfoot. As he sat up, rubbing his sore head, two mushroom guardswomen approached him, one tall and one short, their faces stern and their crossbows menacing.\n")

    print_text("\nWhen Pete woke up hours later, he found himself in a strange land filled with towering mushrooms, their caps forming a colorful canopy overhead. The air was thick with the earthy scent of fungi, and the ground was soft underfoot. As he sat up, rubbing his sore head, two mushroom guardswomen approached him, one tall and one short, their faces stern and their crossbows menacing.\n")

    print_text('\n"Who are you?" one of them demanded. "And what are you doing in the Great General’s land?"\n')

    print_text('\n"I\'m Pete," he replied, trying to sound braver than he felt, “but most people call me Pete. I was looking for my truffle-hunting pig, Hamilton, and I got lost, then I hit my head, then I woke up here, and then I don’t know what happens."\n')

    print_text('\nAfter a brief but intense interrogation, the mushroom women exchanged glances. "You have two choices," the taller one said. "Face trial, or certain doom."\n')

    print_text("\nPete's heart raced. Should he go with the mushroom women and hope for the best, or risk whatever doom they had in store?\n")
    choice_one_choices = [
        "face trial",
        "trial",
        "go to trial"
        "go with the mushroom women",
        "mushroom women",
        "hope for the best"
    ]
    choice_two_choices = [
        "certain doom",
        "doom",
        "risk",
        "risk it",
        "run away",
        "refuse",
        "refuse trial"
    ]
    while True:
        choice = input()
        choice = format_text(choice)
        if choice in choice_one_choices:
            return "cooperate"
        elif choice in choice_two_choices:
            return "refuse_their_demands"
        else:
            print_text("\nPick one of the choices.\nTrial or risk it?\n")
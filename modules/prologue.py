from modules.print_text import print_text
from modules.format_text import format_text

def func(dict):
    dict["games_played"] += 1

    print_text("\nOn a crisp autumn morning, Pete ventured into a great forest with his trusty truffle-hunting pig, Hamilton. Pete, armed with a carrot and stick, attempted to coax his stubborn companion into action.\n")
    print_text('\n"Come on, Hamilton, it\'s trufflin\' time!" Pete urged, waving a carrot enticingly.\n')
    print_text("\nHamilton, however, had his own ideas, snorting and rooting around. As they made their way through the forest, Pete noticed an assortment of oddities scattered along their path. There was a toy robot, several bird plushes, a smelly bearskin rug that seemed especially out of place, plastic army men in various battle poses, and even a judge’s gavel, half-buried in the leaves.\n")
    print_text('\n"Who leaves amazing stuff just lying around?" Pete wondered aloud, shaking his head at the peculiar sight. “How dare this person or persons.”\n')
    print_text("\nAs the struggle continued, an owl swooped by chasing a crow, its wings nearly silent against the morning air. Hamilton's eyes lit up with curiosity. Before Pete could react, the swift pig darted off after the bird, leaving Pete in the clearing.\n")
    print_text('\n"Hamilton, wait!" Pete shouted, but his words were lost in the rustling leaves and the excited grunts of his porky friend. “I thought what we had was special!”\n')
    print_text("\nPete now faced a decision: should he let the pig go or sprint after his runaway companion?\n")

    choice_one_choices = [
        "let the pig go",
        "let go"
    ]
    choice_two_choices = [
        "sprint after his runaway companion",
        "sprint after",
        "go after",
        "after",
        "sprint"
    ]
    while True:
        choice = input()
        choice = format_text(choice)
        if choice in choice_one_choices:
            return "forget_about_it"
        elif choice in choice_two_choices:
            return "follow_the_pig"
        else:
            print_text("\nPick one of the choices.\nShould he let the pig go or sprint after his runaway companion?\n")
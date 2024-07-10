from modules.print_text import print_text

def func(dict):
    print_text('\nPete decided to play it safe and requested an attorney. Moments later, a very cocksure owl entered the room, carrying a massive law book. The courtroom fell silent as the owl made his way to the defense table, his feathers ruffling with confidence. Judge Hamilton gave the owl nasty glances and growled, "Dr. Woo."\n')

    print_text('\nDr. Woo paused dramatically before his great book, the silence in the room growing thicker. Without warning, he hurled the book at Judge Hamilton, causing a commotion. "Run!" Dr. Woo hooted, his voice urgent.\n')

    print_text("\nWithout a second thought, Pete bolted for the door. He leapt through a nearby window and tumbled into the streets outside. As he scrambled to his feet, he found himself face-to-face with an army of plastic men, their tiny faces set in fierce determination. Leading the march was none other than General Kenny Loggins, as a marching band performed Highway to the Danger Zone.\n")

    print_text("\nPete's heart raced. He had to decide quickly: should he escape into the sewer, or stand and face the plastic army?\n")

    choice_one_choices = [
        "escape into the sewer",
        "escape into the sewers",
        "sewer",
        "sewers",
        "escape"
    ]
    choice_two_choices = [
        "face the plastic army",
        "face the army",
        "army",
        "face"
    ]
    while True:
        choice = input()
        if choice in choice_one_choices:
            return "run_for_sewers"
        elif choice in choice_two_choices:
            return "face_the_army"
        else:
            print_text("\nPick one of the choices.\nShould he escape into the sewer, or stand and face the plastic army?\n")
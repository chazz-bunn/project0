import time
import sys

def print_text(text):
    ctr = 0
    for i in text:
        if ctr > 65 and i == " ":
            print(i, end="\n")
            ctr = 0
        else:
            print(i, end="")
        time.sleep(0.04)
        sys.stdout.flush()
        ctr += 1
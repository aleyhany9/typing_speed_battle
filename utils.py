import os
import sys
import random
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg="\nPress Enter to continue..."):
    try:
        input(msg)
    except EOFError:
        pass

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def now():
    return time.time()

class C:
    B = "\033[1m"
    R = "\033[31m"
    G = "\033[32m"
    Y = "\033[33m"
    C = "\033[36m"
    M = "\033[35m"
    GR = "\033[90m"
    RS = "\033[0m"
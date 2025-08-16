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
def colorize(s, col):
    if sys.stdout.isatty():
        return f"{col}{s}{C.RS}"
    return s

WORD_LIST = """
time year people way day man thing woman life child world school state family student group country problem hand part place case week company system program question work night point home water room mother area money story fact month lot right study book eye job word business issue side kind head house service friend father power hour game line end member law car city community name president team minute idea kid body information back parent face others level office door health person art war history party result change morning reason research girl guy moment air teacher force education foot boy age policy process music market sense service data window river machine science library planet galaxy python terminal battle rhythm keyboard accuracy progress bonus streak master champion victory
""".split()

def pick_word(min_len, max_len):
    candidates = [w for w in WORD_LIST if min_len <= len(w) <= max_len]
    if not candidates:
        candidates = WORD_LIST[:]
    return random.choice(candidates)
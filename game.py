from utils import clear, pause, clamp, now, colorize, C, pick_word
import random

ROUNDS = 5

DIFFICULTIES = {
    "easy":    {"round_seconds": 30, "min_len": 3, "max_len": 7,  "speed_step": -2, "name": "Easy"},
    "normal":  {"round_seconds": 25, "min_len": 3, "max_len": 9,  "speed_step": -3, "name": "Normal"},
    "hard":    {"round_seconds": 20, "min_len": 4, "max_len": 12, "speed_step": -4, "name": "Hard"},
}

LETTER_POINTS = 2
WORD_BONUS = 4
MISTAKE_PENALTY = 3
STREAK_BONUS = 3
STREAK_THRESHOLD = 3

def round_banner(round_num, total_rounds, difficulty_name, seconds, min_len, max_len):
    clear()
    title = colorize("TYPING SPEED BATTLE", C.B + C.C)
    print(f"{title}\n")
    print(f"Round {round_num}/{total_rounds}  •  Mode: {difficulty_name}")
    print(f"Time Budget: {seconds}s  •  Word length: {min_len}–{max_len}")
    print("-" * 50)
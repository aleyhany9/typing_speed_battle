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

def play_round(round_index, cfg):
    seconds = clamp(cfg["round_seconds"] + cfg["speed_step"] * round_index, 8, 60)
    min_len = clamp(cfg["min_len"] + round_index // 2, 2, 20)
    max_len = clamp(cfg["max_len"] + round_index // 2, min_len, 20)

    round_banner(round_index + 1, ROUNDS, cfg["name"], seconds, min_len, max_len)
    print("Type the shown word exactly (lowercase).")
    pause("Press Enter to start...")

    t_start = now()
    t_end = t_start + seconds

    correct_words = correct_letters = mistakes = streak = best_streak = 0

    while now() < t_end:
        w = pick_word(min_len, max_len)
        remaining = int(t_end - now())
        print(f"\nTime Left: {colorize(str(remaining)+'s', C.Y)}  |  Word: {colorize(w, C.B)}")
        try:
            user = input("> ").strip()
        except EOFError:
            user = ""
        if user == w:
            correct_words += 1
            correct_letters += len(w)
            streak += 1
            best_streak = max(best_streak, streak)
            print(colorize("✓ Correct!", C.G))
        else:
            mistakes += 1
            streak = 0
            print(colorize(f"✗ Wrong! Target was '{w}'", C.R))

    elapsed = max(0.001, now() - t_start)
    base = correct_letters * LETTER_POINTS + correct_words * WORD_BONUS
    streak_bonus = max(0, (best_streak - STREAK_THRESHOLD + 1)) * STREAK_BONUS if best_streak >= STREAK_THRESHOLD else 0
    penalties = mistakes * MISTAKE_PENALTY
    score = max(0, base + streak_bonus - penalties)

    accuracy = 100.0 * (correct_letters / (correct_letters + mistakes)) if (correct_letters + mistakes) > 0 else 0
    wpm = (correct_letters / 5.0) / (elapsed / 60.0)

    pause("\nRound complete! Press Enter to continue...")
    return {"score": score, "wpm": wpm, "accuracy": accuracy, "best_streak": best_streak, "mistakes": mistakes, "correct_words": correct_words}


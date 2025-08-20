from utils import clear, pause, clamp, now, colorize, C, pick_word
import random
import time

ROUNDS = 5

def cinematic(rank, time_taken, accuracy):
    clear()

    banner = [
        "*"*50,
        "             LEVEL COMPLETE! ✅",
        "*"*50
    ]

    for line in banner:
        print(colorize(line, C.Y))
        time.sleep(0.5)
    print()

    for i in range(3):
        print(colorize("             LEVEL COMPLETE! ✅", C.G), end="\r", flush=True)
        time.sleep(0.5)
        print(" " * 50, end="\r", flush=True)  
        time.sleep(0.3)
    print(colorize("             LEVEL COMPLETE! ✅", C.G))
    print()

    stats = [
        f"Final Time: {time_taken:.2f} seconds ⏱️",
        f"Accuracy: {accuracy:.2f}% 🎯",
        f"Rank Achieved: {rank}\n"
    ]
    for line in stats:
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(0.02)
        print()
        time.sleep(0.5)

    outro = "You conquered the typing challenge... well done!"
    for ch in outro:
        print(ch, end="", flush=True)
        time.sleep(0.04)
    print("\n")

    print(colorize("*"*50, C.Y))
    time.sleep(2)


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

def rank_from_score(total_score, avg_wpm, avg_accuracy):
    points = 0
    if total_score >= 300: points += 2
    elif total_score >= 200: points += 1
    if avg_wpm >= 45: points += 2
    elif avg_wpm >= 30: points += 1
    if avg_accuracy >= 92: points += 2
    elif avg_accuracy >= 80: points += 1
    ranks = ["Novice", "Trainee", "Typist", "Speedster", "Blazer", "Keyboard Ninja", "Typing Legend"]
    return ranks[clamp(points, 0, 6)]

def play_game(cfg):
    stats = []
    for i in range(ROUNDS):
        s = play_round(i, cfg)
        stats.append(s)

    total_score = sum(s["score"] for s in stats)
    avg_wpm = sum(s["wpm"] for s in stats) / len(stats)
    avg_accuracy = sum(s["accuracy"] for s in stats) / len(stats)
    rank = rank_from_score(total_score, avg_wpm, avg_accuracy)

    cinematic(rank, avg_wpm, avg_accuracy)
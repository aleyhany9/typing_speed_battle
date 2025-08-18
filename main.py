from utils import clear, pause
from game import DIFFICULTIES, play_game

def choose_difficulty():
    while True:
        d = input("Choose difficulty (easy / normal / hard): ").strip().lower()
        if d in DIFFICULTIES:
            return DIFFICULTIES[d]
        print("Invalid choice.")

def main():
    while True:
        clear()
        print("=== TYPING SPEED BATTLE ===")
        print("Rules: Type words quickly and accurately. 5 rounds.")
        print()
        cfg = choose_difficulty()
        play_game(cfg)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("you just control+c")
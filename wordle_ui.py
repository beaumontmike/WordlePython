from colorama import Fore, Style
from word_checker import WordChecker
from word_generator import WordGenerator


class WordleUI:
    @staticmethod
    def run(max_guesses):
        running = True

        while running:
            guess_count = 1
            game_word = WordGenerator.generate()

            print("Welcome to Wordle ->")
            print("Today's word has " + str(len(game_word)) + " letters...")

            while guess_count < max_guesses:
                guess = input("Enter a guess: ")
                is_correct, letter_status = WordChecker.check(guess, game_word)
                if is_correct:
                    print("")
                    print("You guessed the word " + game_word + " in " + str(guess_count) + " tries!")
                    break
                else:
                    guess_count += 1
                    WordleUI.print_guess_status(guess, letter_status)
                    print("")

            print("")
            input_quit = input("Press any key to continue, or Q to Quit: ")
            if input_quit == 'Q' or input_quit == 'q':
                running = False
    # end run()

    @staticmethod
    def print_guess_status(guess, status):
        current_letter = 0
        for letter in guess.upper():
            if status[current_letter] == 0:
                print(Fore.RED + letter, end="")
            if status[current_letter] == 1:
                print(Fore.YELLOW + letter, end="")
            if status[current_letter] == 2:
                print(Fore.GREEN + letter, end="")
            current_letter += 1
        print(Style.RESET_ALL + "")
    # end print_guess_status()

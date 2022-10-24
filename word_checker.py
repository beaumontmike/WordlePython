class WordChecker:
    @staticmethod
    def check(guess, game_word):
        guess_matches = []
        if guess.upper() == game_word.upper():
            return True, guess_matches
        else:
            guess_position = 0
            for guess_letter in guess.upper():
                guess_matches.append(0)
                word_position = 0

                for word_letter in game_word.upper():
                    if guess_letter == word_letter:
                        if guess_position == word_position:
                            guess_matches[guess_position] = 2

                        else:
                            if guess_matches[guess_position] != 2:
                                guess_matches[guess_position] = 1

                    else:
                        if guess_matches[guess_position] != 2 and guess_matches[guess_position] != 1:
                            guess_matches[guess_position] = 0

                    word_position += 1
                # end for word_letter in game_word.upper()

                guess_position += 1
            # end for guess_letter in guess.upper()

            return False, guess_matches
    # end check_word()

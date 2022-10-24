import json
import urllib.request


class WordGenerator:
    @staticmethod
    def generate():
        response = urllib.request.urlopen("https://random-word-api.herokuapp.com/word?length=6")
        word = json.load(response)

        return str(word[0])
    # end generate_word()

from flask import Flask, render_template, request, redirect, url_for
from hangman import getword

app = Flask(__name__)

global guesscount
guesscount = 6

guesses = []

global word
word = getword()

global wordletters
wordletters = [letter for letter in word]

global lettercount
lettercount = len(word)

@app.route('/', methods=['POST', 'GET'])
def index():
    global guesscount
    if request.method == "POST":
        guess = request.form['User-input']
        if not guess in guesses:
            guesses.append(guess)
            print(guesses)
        if not guess in wordletters:
            guesscount -= 1
        displayimage = f"static/imgs/Hangman0{guesscount}.png"
        return render_template('hangman.html', guesscount=guesscount, displayimage=displayimage, word=word, guesses=guesses)
    else:
        displayimage = f"static/imgs/Hangman0{guesscount}.png"
        return render_template('hangman.html', guesscount=guesscount, displayimage=displayimage, word=word)


if __name__ == "__main__":
    app.run()

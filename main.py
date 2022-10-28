from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hangman.html')

app.route('/', methods=['POST'])

def get_guess():
    guess = request.form['User-input']
    print(guess)

if __name__ == "__main__":
    app.run(host="192.168.1.76")


get_guess()
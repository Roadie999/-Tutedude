from flask import Flask

app = Flask(__name__)  # <-- use __name__

@app.route('/')
def home():
    return 'Hello World from Neeraj Singh Nayal'

@app.route('/second')
def second():
    return 'Welcome to second page from Neeraj'


if __name__ == '__main__':  # <-- use __name__ and __main__
    app.run()
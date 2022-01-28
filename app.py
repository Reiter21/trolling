from flask import Flask, redirect
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ok'
log = logging.getLogger('werkzeug')
log.disabled = True
SESSION_COOKIE_SECURE = True
PORT = 5000


@app.route('/')
def home():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


if __name__ == "__main__":
    app.run()

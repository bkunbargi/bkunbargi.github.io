from flask import Flask

app = Flask(__name__)

print('Flask is installed')
@app.route('/')
def index():
    return 'This is the homepage'

if __name__ == '''__main__''':
    app.run()

from flask import Flask
app = Flask(__name__)  

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello, World!\n'

@app.route('/goodbye')
def goodbye():
    return 'Goodbye World\n'

if __name__ == '__main__':
   app.run(port=1234)

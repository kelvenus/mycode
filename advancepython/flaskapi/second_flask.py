from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)  

@app.route('/')
def home():
    return 'Hi!\n'
@app.route('/hello/<name>')
def hello_name(name):
    return render_template('boogie_man.html', username = name)
	
if __name__ == '__main__':
   app.run(port=5321)

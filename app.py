from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return 'Hello world.It is the next work!'

if __name__=='__main__':
    app.run(debug=True)
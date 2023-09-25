from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

@app.route('/')
def index():
    return render_template('templates/homepage.html')

if __name__ == '__main__':
    app.run()
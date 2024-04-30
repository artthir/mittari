from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', value=50)

@app.route('/', methods=['POST'])
def update_value():
    value = int(request.form['value'])
    return render_template('index.html', value=value)

if __name__ == '__main__':
    app.run(debug=True)
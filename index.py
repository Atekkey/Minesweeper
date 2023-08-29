from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button-clicked', methods=['POST'])
def button_clicked():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
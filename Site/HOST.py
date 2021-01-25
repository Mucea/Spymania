from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HOME.html')

@app.route('/contributors')
def contributors():
    return 'David Ghergut', 'Mihai Pangratie'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

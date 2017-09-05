from flask import Flask, render_template
app = Flask(__name__, template_folder="views")

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/table')
def table():
    return render_template('table.html')

if __name__ == '__main__':
    app.run(debug=True)

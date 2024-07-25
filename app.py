from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    option = request.form.get('option')

    if option == 'velocity':
        return redirect(url_for('velocity'))
    elif option == 'force':
        return redirect(url_for('force'))
    elif option == 'power':
        return redirect(url_for('power'))
    else:
        return redirect(url_for('home'))

@app.route('/velocity')
def velocity():
    return render_template('velocity.html')

@app.route('/force')
def force():
    return render_template('force.html')

@app.route('/power')
def power():
    return render_template('power.html')

if __name__ == '__main__':
    app.run(debug=True)

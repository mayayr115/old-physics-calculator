from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     message = request.form.get('message')
    
#     # Process the data (e.g., save to database, send email, etc.)
#     # For now, we'll just print it to the console
#     print(f'Name: {name}, Email: {email}, Message: {message}')
    
#     return redirect(url_for('home'))

@app.route('/velocity')
def velocity():
    return render_template('velocity.html')

if __name__ == '__main__':
    app.run(debug=True)

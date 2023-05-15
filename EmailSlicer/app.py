from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            username, domain = email.split("@")
            return render_template('index.html', username=username, domain=domain)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

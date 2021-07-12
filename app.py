from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def second_page():
    return render_template('about.html')
  
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
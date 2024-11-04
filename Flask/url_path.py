from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/app")
def my_app():
    return "<p>This is my app page!</p>"

@app.route("/username/<name>")
def user(name):
    return f"Hello new user {name}"

# converting URL variable into any datatypes
@app.route("/username/<name>/<int:number>")
def user_age(name, number):
    return f"Hello new user {name} and your age is {number}"

# run app in debug mode to auto reload
app.run(debug=True)
from flask import Flask
from flask import render_template
from random import choice, randint

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

def random_color():
    a, b, c = (randint(30,255), randint(30,255), randint(30,255))
    return f"({a}, {b}, {c})"

def random_tidbit():
    sayings = [
    	"git along little doggy",
    	"hello out there :)",
    	"hello ma baby hello ma honey hello ma ragtime gal"]
    return choice(sayings)

app.jinja_env.globals.update(random_tidbit=random_tidbit, random_color=random_color)

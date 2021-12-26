from flask import Flask
from flask import render_template
from random import choice, randint

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/faster')
def faster():
    return render_template("index.html", faster = True)

@app.errorhandler(404)
def not_found(e):
    list_of_insults = ["nincompoop", "dumby", "sport", "gabby"]
    return "404: Yeah right, you wish, {0}.".format(choice(list_of_insults))

def random_color():
    min_color, max_color = 100, 255
    a, b, c = (randint(min_color, max_color), randint(min_color, max_color), randint(min_color, max_color))
    return f"({a}, {b}, {c})"

def random_tidbit():
    sayings = [
    	"git along little doggy",
    	"hello out there :)",
    	"hello ma baby hello ma honey hello ma ragtime gal"]
    return choice(sayings)

def your_new_year_forecast():
    output = "Your new year's forecast: "
    outcomes = ["ABSOLUTE HOGWASH",
    	"alright i guess",
    	"simply stupendous nothing bad could possibly happen",
    	"probably become a hermit or something",
    	"you will be promoted to eagle scout",
    	"i''m thinkin bout thos beans"]
    output += choice(outcomes)
    return output

def faster_forecast():
    output = "Your new year's forecast: "
    outcomes = ["<b>CERTAIN DEATH</b>",
    	"you will get a spik up ur butt",
    	"you will be bit by monkeys more than you have in previous years",
    	"you will rob a baby at gunpoint for its candy",
    	"BANISHMENT",
    	"TRENCH WARFARE",
    	"your eyeballs will be gouged out by a dropbear",
    	"eat my frosted shitflakes"]
    output += choice(outcomes)
    return output


app.jinja_env.globals.update(random_tidbit=random_tidbit, random_color=random_color)
app.jinja_env.globals.update(your_new_year_forecast = your_new_year_forecast, faster_forecast = faster_forecast)

from asyncio.windows_events import NULL
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import database

app = Flask(__name__)
app.static_folder = 'static'


# change to name of database
db_name = "data.db"

@app.route("/", methods=["POST", "GET"])
def home():

    char1 = None
    char2 = None

    if request.method == "POST":
        char1 = database.get_random()
        char2 = database.get_random()

        return render_template("home.html", char1=char1, char2=char2)

    return render_template("home.html", char1=char1, char2=char2)
    
@app.route("/data")
def data():

    characters = database.list_all()
    
    return render_template("data.html", characters=characters)

@app.route("/add-character", methods=["POST", "GET"])
def enter_name():
    if request.method == "POST":
        name = request.form["name"]
        fandom = request.form["fandom"]
        media = request.form["media"]

        print(name, fandom, media)

        database.add_character(name, fandom, media)
        return render_template("add-character.html")
    else:
        return render_template("add-character.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
        
if __name__ == "__main__":
    app.run()
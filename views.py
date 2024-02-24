from flask import Blueprint, render_template,  redirect, request, url_for
from favourites import favourite_bands

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2", methods=["GET", "POST"])
def page2():
    if request.method == "POST":
        new_band = request.form["add_band"]
        favourite_bands.append(new_band)

    return render_template("page2.html", favourite_bands = favourite_bands)

@my_view.route("/page3")
def page3():
    my_name = "Raf"
    return render_template("page3.html", my_name = my_name)

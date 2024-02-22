from flask import Blueprint, render_template,  redirect, request, url_for

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html")

@my_view.route("/page3")
def page3():
    my_name = "Raf"
    return render_template("page3.html", my_name = my_name)

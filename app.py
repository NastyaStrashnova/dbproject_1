
from flask import Flask, render_template, url_for, request, abort,  redirect
app = Flask(__name__)


@app.route('/<action>', methods = ['GET'])
def actinfo(action):
    if action == "menu":
        return render_template("menu.html")

    elif action == "order":
        return render_template("order.html")

    elif action == "reserv":
        return render_template("reserv.html")

    elif action == "coment":
        return render_template("coment.html")

    elif action == "profile":
        return render_template("profile.html")

    elif action == "sign_in":
        return render_template("sign_in.html")

    elif action == "sign_up":
        return render_template("sign_up.html")

    else:
        return render_template("404.html")


if __name__ == '__main__':
    app.run(port=5000)

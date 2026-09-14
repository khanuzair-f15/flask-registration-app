from flask import Flask, request
from flask import render_template

web = Flask(__name__)


# maping
@web.route('/')
def home():
    return render_template("home_page.html")


@web.route('/web')
def scrap():
    return render_template("web.html")


@web.route("/confirmation", methods=['POST', 'GET'])
def confirmation_page():
    if request.method == "POST":
        n = request.form.get("name")
        p = request.form.get("phone")
        c = request.form.get("city")
        return render_template("confirmation_page.html", name=n, city=c, phonenumber=p)


if __name__ == "__main__":
    web.run(debug=True)

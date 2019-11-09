import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"]='1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"]='1'

from flask import Flask,render_template,redirect,url_for
from flask_dance.contrib.google import make_google_blueprint,google

app=Flask(__name__)

app.config["SECRET_KEY"]="mykey"

blueprint=make_google_blueprint(client_id='91961509858-1kcnmdqbr3p336e1rsrc32k45ftun1vl.apps.googleusercontent.com',
                                client_secret='huFrrBm3-knROX5nSixoPrub',
                                offline=True,
                                scope=["profile","email"])

app.register_blueprint(blueprint,url_prefix='/login')

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/welcome")
def welcome():
    response = google.get("/oauth2/v2/userinfo")
    assert response.ok, response.text
    email = response.json()["email"]
    return render_template("welcome.html",email=email)

@app.route("/login/google")
def login():

    if not google.authorized:
        return redirect(url_for('google.login'))

    response=google.get("/oauth2/v2/userinfo")
    assert response.ok,response.text
    email=response.json()["email"]

    return render_template("welcome.html",email=email)
import os
from flask import Flask, request, render_template, redirect
from flask.scaffold import F
from instaloader import Instaloader
from os import listdir, path
from shutil import move, rmtree


def CreateDir():
    if os.path.exists("static/Profiles/"):
        print("Folder Exists")
    else:
        os.makedirs("static/Profiles/")
        print("Folder Created")


insta_username = Instaloader()
file_dir = path.dirname(__file__)

app = Flask(__name__)


@app.route("/")
def index():
    CreateDir()
    return render_template("form.html")


@app.route("/submit")
def showResult():
    username = request.args.get("username", "No Username")
    insta_username.download_profile(username, profile_pic_only=True)
    picName = listdir(username)[0]

    fullPathSRC = file_dir + "\\" + username + "\\" + picName
    fullPathDEC = file_dir + "\\" + "static\Profiles"
    try:
        move(fullPathSRC, fullPathDEC)
        isSubmit = True
    except:
        isSubmit = False
    rmtree(username)
    return redirect(f"/static/Profiles/{picName}")

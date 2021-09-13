from flask import Flask, request, render_template, send_file, redirect
from instaloader import Instaloader
from os import listdir, rmdir, path
from shutil import move, rmtree


insta_username = Instaloader()
file_dir = path.dirname(__file__)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/submit")
def showResult():
    username = request.args.get("username", "No Username")
    insta_username.download_profile(username, profile_pic_only=True)
    pathList = listdir(username)
    picName = pathList[0]
    fullPathSRC = file_dir + "\\" + username + "\\" + pathList[0]
    fullPathDEC = file_dir + "\\" + "static\Profiles"
    try:
        move(fullPathSRC, fullPathDEC)
        isSubmit = True
    except:
        isSubmit = False
    rmtree(username)
    return redirect(f"/static/Profiles/{picName}")

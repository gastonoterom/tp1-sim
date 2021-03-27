from app import app
from flask import Flask, render_template, send_from_directory


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./frontend/dist/css', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./frontend/dist/js', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('./frontend/dist/img', path)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory("./frontend/dist", "favicon.ico")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

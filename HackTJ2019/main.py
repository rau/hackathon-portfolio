from flask import Flask, render_template, request
import os
import getrep
import tweetTo


os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        address = request.form['zip']
        name = request.form['name']
        message = request.form['message']
        rep = getrep.getTwitter(address)
        representativeName = getrep.getName(address)
        tweetTo.tweet(message, name, rep)
        return render_template('indexwithrep.html', representativeName=representativeName)
    return render_template('index.html')

if __name__ == "main":
    app.run(debug=True)

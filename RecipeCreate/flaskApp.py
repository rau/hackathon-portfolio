from flask import Flask, render_template, request
import downloadImgurImages
import getImageLabels
import recipeGetter
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        imgurAlbum = request.form['imgur']
        folderName = downloadImgurImages.downloadImages(imgurAlbum)
        foodList = getImageLabels.getLabels(folderName)
        print(foodList)
        recipeHTML = recipeGetter.getHTML(foodList)
        return render_template('indexWithRecipe.html', foodList=foodList, recipeHTML=recipeHTML)
    return render_template('index.html')

if __name__ == "main":
    app.run(debug=True)

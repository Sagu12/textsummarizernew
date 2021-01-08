from flask import Flask, render_template,request
import requests
from bs4 import BeautifulSoup
import nltk 
import pandas as pd
from newspaper import Article
nltk.download("punkt")


app = Flask(__name__)

def get_wiki_content(url):
    article= Article(url)

    article.download()
    article.parse()
    article.nlp()
    articletext= article.text
    articlesum= article.summary

    return articlesum


#def top_sent(url):
#	article= Article(url)
#	article.download()
 #   article.parse()
  #  article.nlp()
	#top_sum= article.summary

	#return top_sum


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        url_content = get_wiki_content(url)
        return url_content
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
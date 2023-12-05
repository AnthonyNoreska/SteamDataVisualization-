from flask import Flask, jsonify, render_template
import pandas as pd
import csv 

app = Flask(__name__)

@app.route("/")
def Index():
    return "Steam DataBase Analysis"

@app.route("/top10gamespercountry")
def api_top_10():
    df1 = pd.read_csv("top_10_games_per_country.csv")
    return jsonify(df1.to_dict())

@app.route("/genrereview")
def genre_review_ratios():
    df2 = pd.read_csv("genre_reviews_ratios.csv")
    return jsonify(df2.to_dict())

@app.route("/genre_totals")
def genre_totals():
    df3 = pd.read_csv("genre_totals.csv")
    return jsonify(df3.to_dict())


if __name__ == "__main__":
    app.run()
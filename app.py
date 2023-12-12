import os
from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Get the directory where app.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/other_features")
def other_features():
    return render_template("other_features.html")


@app.route("/top10gamespercountry")
def api_top_10():
    csv_file = os.path.join(base_dir, "top_10_games_per_country.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/genrereview")
def api_genre_review_ratios():
    csv_file = os.path.join(base_dir, "genre_reviews_ratios.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/genre_totals")
def api_genre_totals():
    csv_file = os.path.join(base_dir, "genre_totals.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/ccu_ratio")
def api_ccu_ratio():
    csv_file = os.path.join(base_dir, "ccu_ratio.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/adventure")
def api_adventure():
    csv_file = os.path.join(base_dir, "adventure_data_converted.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/action")
def api_action():
    csv_file = os.path.join(base_dir, "action_data_converted.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/indie")
def api_indie():
    csv_file = os.path.join(base_dir, "indie_data_converted.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/rpg")
def rpg():
    csv_file = os.path.join(base_dir, "rpg_data_converted.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/simulation")
def api_simulation():
    csv_file = os.path.join(base_dir, "simulation_data_converted.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/sports")
def api_sports():
    csv_file = os.path.join(base_dir, "sports_data_converted.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/strategy")
def api_strategy():
    csv_file = os.path.join(base_dir, "strategy_data_converted.csv")
    df = pd.read_csv(csv_file)
    df = df.fillna("null")
    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)

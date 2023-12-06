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

@app.route("/ccu_ratio")
def ccu_ratio():
    ccu_ratio_output = pd.read_csv("ccu_ratio.csv")
    return jsonify(ccu_ratio_output.to_dict())

@app.route("/api/adventure")
def adventure_api():
    adventure_output = pd.read_csv("Adventure_data_converted.csv")
    return jsonify(adventure_output.to_dict())

@app.route("/api/action")
def action_api():
    action_output = pd.read_csv("Action_data_converted.csv")
    return jsonify(action_output.to_dict())

@app.route("/api/indie")
def indie_api():
    indie_output = pd.read_csv("Indie_data_converted.csv")
    return jsonify(indie_output.to_dict())

@app.route("/api/RPG")
def RPG():
    rpg_output = pd.read_csv("RPG_data_converted.csv")
    return jsonify(rpg_output.to_dict())

@app.route("/api/simulation")
def simulation():
    simulation_output = pd.read_csv("Simulation_data_converted.csv")
    return jsonify(simulation_output.to_dict())

@app.route("/api/sports")
def sports():
    sports_output = pd.read_csv("Sports_data_converted.csv")
    return jsonify(sports_output.to_dict())

@app.route("/api/strategy")
def strategy():
    strategy_output = pd.read_csv("Strategy_data_converted.csv")
    return jsonify(strategy_output.to_dict())


if __name__ == "__main__":
    app.run()
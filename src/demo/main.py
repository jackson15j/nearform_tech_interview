"""
Using your IDE of choice and any technical documentation online that you need, please screenshare the following live code exercise with your interviewer. The goal of this exercise is to complete as many tasks as possible (in order) while still organizing the code reasonably well, and using good development patterns. Don't rush or worry about completing all of the tasks, we're interested in seeing how you implement these features within the given timeframe. Please talk through your thinking as you go along to help the interviewer follow your process.

Using Python and the following starter template, create a REST API that retrieves data from another API and manipulates the output. If you feel more comfortable using a different approach than this template, feel free to do so.


    The coins endpoint should return the market data for 10 crypto currency coins from the follow API and transform the data into the following format

// ref: <https://www.coinlore.com/cryptocurrency-data-api>
<https://api.coinlore.net/api/tickers/>

Output Format:

[
  {
    "id": "the data.id field",
    "name": "the data.name field"
    "price": "the data.price_usd field, formatted as a USD currency string with commas"
    "at": "the info.Timestamp" field, formatted as an ISO8601 datetime string
  },
]

    Create a new REST API endpoint to return a single coin by its id
    Improve the REST API for coins by allowing consumers to sort by price or date
    Improve the REST API by ensuring the remote API is only accessed one time during the lifecycle of the application
    Create a new REST API endpoint that returns data grouped into the following bins by its data.percent_change_24h field for use in a histogram

Bins: -5 to -1, -1 to 1, 1 to 5

// example response
[
  {
    "binLabel": "-5 to -1",
    "numberOfCoins": "15",
    "coinIds": [1,18,30,44,60]
  },
  {
    "binLabel": "-1 to 1",
    "numberOfCoins": "35",
    "coinIds": [3,7,8,15]
  },
  {
    "binLabel": "1 to 5",
    "numberOfCoins": "19",
    "coinIds": [4,6,22,99]
  }
]




TODO: Nearform Main docstring."""

from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/coins', methods=['GET'])
    def get_coins():
        return jsonify({ 'example': 'data' })

    return app


app = create_app()


def parser(data = {}):
    d = data.get("data", {})[0]
    ret_dict = {
        "id": d.get("id", -1),
        "name": d.get("name", ""),
        "price": d.get("price", ""),
    }
    return ret_dict




if __name__ == '__main__':
    app.run(debug=True)

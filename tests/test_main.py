"""TODO"""
import json
from src.demo.main import parser
from datetime import datetime


URL = "http://127.0.0.1:5000"
DATA = {
  "data": [
    {
      "id": "90",
      "symbol": "BTC",
      "name": "Bitcoin",
      "nameid": "bitcoin",
      "rank": 1,
      "price_usd": "67685.02",
      "percent_change_24h": "-0.92",
      "percent_change_1h": "0.57",
      "percent_change_7d": "-1.30",
      "price_btc": "1.00",
      "market_cap_usd": "1329563158682.30",
      "volume24": 44449178556.27036,
      "volume24a": 54015580091.57545,
      "csupply": "19643390.00",
      "tsupply": "19643390",
      "msupply": "21000000"
    },
  ],
  "info": {
    "coins_num": 12230,
    "time": 1710780122
  }
}





class TestMain:
    def test_a(self):
        assert True


    def test_coins_200(self, client):
        exp = {"example":"data"}
        ret_val = client.get("/coins")
        print(ret_val.data)

        assert json.loads(ret_val.data) == exp
        assert ret_val.status_code == 200


    def test_parser(self):


        assert parser(DATA) == {
            "id": "90",
            "name": "Bitcoin",
            "price": "67685.02",
            "at": datetime.fromtimestamp(1710780122).isoformat(),
        }

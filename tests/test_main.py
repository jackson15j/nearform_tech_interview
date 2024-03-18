"""TODO"""
import json


URL = "http://127.0.0.1:5000"

class TestMain:
    def test_a(self):
        assert True


    def test_coins_200(self, client):
        exp = {"example":"data"}
        ret_val = client.get("/coins")
        print(ret_val.data)

        assert json.loads(ret_val.data) == exp
        assert ret_val.status_code == 200

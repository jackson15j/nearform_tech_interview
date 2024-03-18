"""TODO"""
from src.demo.main import Query
import graphene


class TestMain:
    def test_a(self):
        assert True

    def test_graphene_graphql_example(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute("{ hello }")
        assert result.data["hello"] == "Hello World"

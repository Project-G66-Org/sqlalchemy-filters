from sqlalchemy import func
from sqlalchemy_filters import get_query_models
from test.models import Bar, Foo, Qux


class TestGetQueryModels(object):

    def test_query_with_no_models(self, session):
        query = session.query()

        entities = get_query_models(query)

        assert {} == entities

    def test_query_with_one_model(self, session):
        query = session.query(Bar)

        entities = get_query_models(query)

        assert {'Bar': Bar} == entities

    def test_query_with_multiple_models(self, session):
        query = session.query(Bar, Qux)

        entities = get_query_models(query)

        assert {'Bar': Bar, 'Qux': Qux} == entities

    def test_query_with_duplicated_models(self, session):
        query = session.query(Bar, Qux, Bar)

        entities = get_query_models(query)

        assert {'Bar': Bar, 'Qux': Qux} == entities

    def test_query_with_one_field(self, session):
        query = session.query(Foo.id)

        entities = get_query_models(query)

        assert {'Foo': Foo} == entities

    def test_query_with_multiple_fields(self, session):
        query = session.query(Foo.id, Bar.id, Bar.name)

        entities = get_query_models(query)

        assert {'Foo': Foo, 'Bar': Bar} == entities

    def test_query_with_aggregate_func(self, session):
        query = session.query(func.count(Foo.id))

        entities = get_query_models(query)

        assert {'Foo': Foo} == entities
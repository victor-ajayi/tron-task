from app.models import Request


class TestDatabase:
    def test_add_requests(self, session):
        data = {
            "account_name": "account",
            "address": "address",
        }
        session.add(Request(**data))
        session.commit()

        assert len(session.query(Request).all()) == 1

import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip(reason="Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "meuNome222",
        "email": "email22@email.com",
        "evento_id": 2
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip(reason="Select in DB")
def test_select_subscriber():
    email = "email@email.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)

@pytest.mark.skip(reason="Ranking")
def test_ranking():
    evento_id = 2
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(evento_id)

    for elemento in resp:
        print(f"Link: {elemento.link}, total de inscritos: {elemento.total}")

import pytest
from .eventos_link_repository import EventosLinkRepository

@pytest.mark.skip(reason="Insert in DB")
def test_insert_eventos_link():
    event_id = 2
    subscriber_id = 1
    event_link_repo = EventosLinkRepository()

    event_link_repo.insert(event_id, subscriber_id)

from flask import Flask, Blueprint, jsonify, request
from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.eventos_link_repository import EventosLinkRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

events_link_route_bp = Blueprint("events_link_route", __name__)

@events_link_route_bp.route("/events_link", methods=["POST"])
def create_new_link():
    eventos_link_repo = EventosLinkRepository()
    events_link_creator = EventsLinkCreator(events_link_repo)
    
    http_request = HttpRequest(body=request.json)
    
    http_response = events_link_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code

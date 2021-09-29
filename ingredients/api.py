import uuid
from flask import Blueprint, request

from ingredients.dataclass import IngredientsRequests

api = Blueprint('ingredients_api', __name__, url_prefix='/ingredients')

ingredients = {}


@api.route('/', methods=['POST'])
def create_ingredient():
    input_data = IngredientsRequests.from_json(request.data)
    unique_key = str(uuid.uuid4())
    ingredients[unique_key] = input_data
    return {"StatusCode": 200, "request_id": unique_key, "Status": "Ingredient Created Successfully."}


@api.route('/', methods=['GET'])
def get_ingredient():
    return {"StatusCode": 200, "Ingredients": ingredients, "Status": "Ingredients Fetched Successfully."}


@api.route('/<request_id>/', methods=['GET'])
def get_ingredients(request_id):
    return {"StatusCode": 200, "Ingredients": ingredients[request_id], "Status": "Ingredients Fetched Successfully."}


@api.route('/<request_id>/', methods=['DELETE'])
def delete_ingredients(request_id):
    ingredients.pop(request_id)
    return {"StatusCode": 200, "Status": "Successfully Removed Ingredients."}


@api.errorhandler
def handle_bad_request(e):
    return {
               'status': 'BAD_REQUEST',
               'message': str(e)
           }, 400


@api.errorhandler
def handle_bad_request(e):
    return {
        'status': 'ERROR',
        'message': str(e)
    }, 500

from flask import request, jsonify
from app import app
from .models import Orders
from .const import *

@app.route('/')
def index():
    return "<h1>Welcome to Connector</p>"

@app.route('/api/v1/test', methods=['GET', 'POST'])
async def all_orders():
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'orders': await Orders.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    return response
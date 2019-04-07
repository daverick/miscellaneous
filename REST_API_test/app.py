'''verse: test tramnsfer API'''

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from flask_httpauth import HTTPBasicAuth,HTTPTokenAuth
auth = HTTPBasicAuth()
auth2 = HTTPTokenAuth()

app = Flask(__name__)
api = Api(app)

BALANCE = 100

@auth.verify_password
def verify_password(username, password):
    '''verify that the password is correct  and set the user
    TODO implement correctly
    '''
    if username != 'test-user':
        return False
    if password != 'correct-password':
        return False
    return True

@auth2.verify_token
def verify_token(token):
    '''verify that the token is correct and set the user
    TODO implement correctly
    '''
    if token == 'TODO':
        return True
    return False

class Token(Resource):
    '''
        token resource
    '''
    @auth.login_required
    def get(self):
        '''
        return the token associated with the authenticated user
        TODO: create a real token for this user
        '''
        return jsonify({'token':'TODO'})

class Balance(Resource):
    '''
    balance resource
    '''
    @auth2.login_required
    def get(self):
        '''
        return the balance for the real user
        TODO: looks for the real balance for this user
        '''
        return jsonify({'balance':BALANCE})

class Transfer(Resource):
    '''
    transfer resource
    '''
    @auth2.login_required
    def post(self):
        '''
        create a transfer from the connected user
        TODOs:
        - check the real balance of the authenticated user
        - check that the recipient really exists
        - create a real transfer ID
        '''
        json_data = request.get_json(force=True)
        recipient_id = json_data['recipientId']
        amount = json_data['amount']
        if recipient_id == -1:
            resp = jsonify({
                'error': f'The recipient with id:{recipient_id} does not exists'})
            resp.status_code = 409
            return resp
        if amount > BALANCE:
            resp = jsonify({
                'error': f'You cannot make a transfer greater than your current balance'})
            resp.status_code = 409
            return resp
        return jsonify({'recipientId':recipient_id,
                        'amount':amount,
                        'transferId':1})

api.add_resource(Token, '/api/v1/token')
api.add_resource(Balance, '/api/v1/balance')
api.add_resource(Transfer, '/api/v1/transfers')

from flask import make_response
from flask_restful import Resource
from werkzeug.exceptions import NotFound
from config import app, api
from models import User


class Users( Resource ):
    def post( self ):
        return make_response( 
            { 'we': 'want to create a new user, i.e. signup' } 
        )

api.add_resource( Users, '/users' )


@app.route( '/login', methods = [ 'POST' ] )
def login():
    return make_response( { 'we':'want to log in' } )





@app.errorhandler( NotFound )
def not_found( e ):
    return { 'error': 'route not found' }


if __name__ == '__main__':
    app.run( port = 5555, debug = True )
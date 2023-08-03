from flask import make_response, request, session
from flask_restful import Resource
from werkzeug.exceptions import NotFound
from config import app, api, db
from models import User


class Users( Resource ):
    def post( self ):
        data = request.json
        the_username = data['name']
        text_password = data['password']

        new_user = User( name = the_username, password_hash = text_password )

        db.session.add( new_user )
        db.session.commit()

        return make_response( new_user.to_dict(), 201 )

api.add_resource( Users, '/users' )


@app.route( '/login', methods = [ 'POST' ] )
def login():

    data = request.json
    username = data['name']
    password = data['password']

    # is the username one that we have in the database already
    user = User.query.filter_by( name = username ).first()
    if not user:
        return make_response( { 'error': 'user not found' }, 404 )

    if not user.authenticate( password ):
        return make_response( { 'error': 'wrong password' }, 401 )

    # we can put a cookie in the browser!
    session['user_id'] = user.id
    return make_response( user.to_dict() )





@app.errorhandler( NotFound )
def not_found( e ):
    return { 'error': 'look elsewhere for thy backend route! ' + str( e ) }


if __name__ == '__main__':
    app.run( port = 5555, debug = True )
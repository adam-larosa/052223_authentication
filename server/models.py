from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt


class User( db.Model, SerializerMixin ):
    __tablename__ = 'users'

    serialize_rules = ( '-_password_hash', )

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )

    _password_hash = db.Column( db.String )

    @property
    def password_hash( self ):
        return self._password_hash

    @password_hash.setter
    def password_hash( self, new_password_string ):

        # take the plaintext string and convert to "byte object"
        plain_byte_obj = new_password_string.encode( 'utf-8' )

        # create new encrypted object
        encrypted_hash_object = bcrypt.generate_password_hash( plain_byte_obj )
        
        # generate string of characters from encrypted instance
        hash_object_as_string = encrypted_hash_object.decode( 'utf-8')

        # finally, change instance attribute
        self._password_hash = hash_object_as_string
    

    # a tool to check to see if a password given, is the real password
    def authenticate( self, some_string ):
        return bcrypt.check_password_hash( 
            self.password_hash, 
            some_string.encode( 'utf-8' )
        )




    # # fake hashing tool
    # def fake_hash_maker( self, plaintext_string ):
    #     list_of_integers_obj = bytearray( 
    #         'random text no one will think of' + plaintext_string, 
    #         encoding = 'utf-8' 
    #     )
    #     return sum( list_of_integers_obj )
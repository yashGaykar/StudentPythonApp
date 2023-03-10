from marshmallow import Schema,fields

class UserSchema(Schema):
    """User Login Schema"""
    email=fields.Email(required=True)
    password=fields.Str(required=True)
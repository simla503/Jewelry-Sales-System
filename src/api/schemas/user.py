from marshmallow import Schema, fields

class RegisterRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    role = fields.Str(load_default='user')   # sửa missing → load_default

class LoginRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)

class UserResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Email()
    role = fields.Str()

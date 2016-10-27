from marshmallow import Schema, fields, ValidationError


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class UserSchema(Schema):
    name = fields.Str(validate=must_not_be_blank)
    email = fields.Str(validate=must_not_be_blank)
    password = fields.Str(validate=must_not_be_blank)

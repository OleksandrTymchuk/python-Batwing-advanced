from marshmallow import Schema, fields


class AuthorSchema(Schema):
    author_id = fields.Integer(required=True, dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)

from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    author = fields.String(required=True)

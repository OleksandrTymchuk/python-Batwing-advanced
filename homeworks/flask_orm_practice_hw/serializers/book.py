from marshmallow import Schema, fields


class BookSchema(Schema):
    book_id = fields.Integer(required=True, dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
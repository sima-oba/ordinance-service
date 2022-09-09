from marshmallow import Schema, fields


class FineInfractionSchema(Schema):
    amount = fields.Float(required=True)

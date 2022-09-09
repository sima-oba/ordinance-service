from marshmallow import Schema, fields


class CancelOrdinanceSchema(Schema):
    origin_ordinance = fields.String(required=True)

from marshmallow import Schema, fields


class ExtendedTermSchema(Schema):
    origin_ordinance = fields.String(required=True)
    extend_by = fields.Int(required=True)

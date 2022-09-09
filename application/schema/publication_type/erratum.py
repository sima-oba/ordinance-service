from marshmallow import Schema, fields


class ErratumSchema(Schema):
    origin_ordinance = fields.String(required=True)
    publish_date = fields.DateTime(format='%Y-%m-%d', required=True)
    concession = fields.String(required=True)
